"""Vitamin Deficiency Prediction & Food Recommendation."""
import os
import re
import secrets
from functools import wraps
from pathlib import Path

from flask import (Flask, abort, flash, g, redirect, render_template, request,
                   send_file, session, url_for)
from io import BytesIO
from werkzeug.security import check_password_hash, generate_password_hash

import db
from knowledge import DISCLAIMER, FOOD_GROUPS, ORDER, VITAMINS
from predictor import predictor
from report import build_report

BASE = Path(__file__).parent


def _secret_key() -> str:
    if os.environ.get("SECRET_KEY"):
        return os.environ["SECRET_KEY"]
    path = BASE / "instance" / "secret_key"
    path.parent.mkdir(exist_ok=True)
    if not path.exists():
        path.write_text(secrets.token_hex(32))
    return path.read_text().strip()


app = Flask(__name__)
app.config.update(SECRET_KEY=_secret_key(), SESSION_COOKIE_HTTPONLY=True,
                  SESSION_COOKIE_SAMESITE="Lax")
db.init_db()

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# ---------- helpers ----------
def csrf_token() -> str:
    if "csrf" not in session:
        session["csrf"] = secrets.token_hex(16)
    return session["csrf"]


app.jinja_env.globals["csrf_token"] = csrf_token


@app.before_request
def load_user_and_check_csrf():
    g.user = db.get_user(session["uid"]) if "uid" in session else None
    if request.method == "POST":
        if not secrets.compare_digest(request.form.get("csrf", ""), session.get("csrf", "x")):
            abort(400, "Invalid or missing security token. Please reload the page.")


def login_required(view):
    @wraps(view)
    def wrapped(*a, **kw):
        if g.user is None:
            flash("Please sign in to continue.", "info")
            return redirect(url_for("login", next=request.path))
        return view(*a, **kw)
    return wrapped


def safe_next(target):
    return target if target and target.startswith("/") and not target.startswith("//") else url_for("dashboard")


@app.context_processor
def inject():
    return {"VITAMINS": VITAMINS, "ORDER": ORDER, "FOOD_GROUPS": FOOD_GROUPS,
            "ranges": predictor.ranges, "cutoffs": predictor.cutoffs}


# ---------- public pages ----------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if g.user:
        return redirect(url_for("dashboard"))
    form = {}
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        pw, pw2 = request.form.get("password", ""), request.form.get("confirm", "")
        form = {"name": name, "email": email}
        error = None
        if len(name) < 2:
            error = "Please enter your name."
        elif not EMAIL_RE.match(email):
            error = "Please enter a valid email address."
        elif len(pw) < 8:
            error = "Password must be at least 8 characters."
        elif pw != pw2:
            error = "Passwords do not match."
        if not error:
            uid = db.create_user(name, email, generate_password_hash(pw))
            if uid is None:
                error = "An account with this email already exists."
            else:
                session.clear()
                session["uid"] = uid
                flash(f"Welcome, {name.split()[0]}!", "success")
                return redirect(url_for("dashboard"))
        flash(error, "error")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if g.user:
        return redirect(url_for("dashboard"))
    email = ""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        user = db.get_user_by_email(email)
        if user and check_password_hash(user["password_hash"], request.form.get("password", "")):
            session.clear()
            session["uid"] = user["id"]
            return redirect(safe_next(request.args.get("next")))
        flash("Incorrect email or password.", "error")
    return render_template("login.html", email=email)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for("index"))


# ---------- app pages ----------
@app.route("/dashboard")
@login_required
def dashboard():
    recent = db.list_assessments(g.user["id"], limit=3)
    return render_template("dashboard.html", recent=recent)


@app.route("/check", methods=["GET", "POST"])
@login_required
def check():
    values = {}
    if request.method == "POST":
        errors = []
        for v in ORDER:
            raw = request.form.get(f"v_{v}", "").strip()
            try:
                num = float(raw)
                if not 0 < num <= predictor.ranges[v][1] * 3:
                    raise ValueError
                values[v] = num
            except ValueError:
                errors.append(f"{VITAMINS[v]['name']}: enter a positive number "
                              f"(typical range {predictor.ranges[v][0]:g} to {predictor.ranges[v][1]:g}).")
        if errors:
            for e in errors:
                flash(e, "error")
            return render_template("check.html", values=request.form)
        result = predictor.predict(values)
        aid = db.save_assessment(g.user["id"], values, result["flags"], result["group"])
        return redirect(url_for("result", aid=aid))
    return render_template("check.html", values=values)


@app.route("/result/<int:aid>")
@login_required
def result(aid):
    a = db.get_assessment(g.user["id"], aid)
    if not a:
        abort(404)
    deficient = [v for v in ORDER if a["flags"][v]]
    return render_template("result.html", a=a, deficient=deficient,
                           group=FOOD_GROUPS.get(a["food_group"]), disclaimer=DISCLAIMER)


@app.route("/history")
@login_required
def history():
    return render_template("history.html", items=db.list_assessments(g.user["id"]))


@app.route("/result/<int:aid>/delete", methods=["POST"])
@login_required
def delete(aid):
    db.delete_assessment(g.user["id"], aid)
    flash("Report deleted.", "info")
    return redirect(url_for("history"))


@app.route("/result/<int:aid>/report.pdf")
@login_required
def report_pdf(aid):
    a = db.get_assessment(g.user["id"], aid)
    if not a:
        abort(404)
    pdf = build_report(g.user, a, predictor.ranges, predictor.cutoffs)
    return send_file(BytesIO(pdf), mimetype="application/pdf", as_attachment=True,
                     download_name=f"vitamin-report-{aid:05d}.pdf")


@app.errorhandler(404)
def not_found(_):
    return render_template("error.html", code=404, msg="That page could not be found."), 404


@app.errorhandler(400)
def bad_request(e):
    return render_template("error.html", code=400, msg=getattr(e, "description", "Bad request.")), 400


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))

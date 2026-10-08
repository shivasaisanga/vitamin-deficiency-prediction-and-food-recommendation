"""SQLite storage (users + assessments)."""
import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "instance" / "vitamin.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at    TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS assessments (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    levels     TEXT NOT NULL,      -- JSON {"A": 3.1, ...}
    flags      TEXT NOT NULL,      -- JSON {"A": 1, ...}
    food_group INTEGER,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_assess_user ON assessments(user_id, created_at DESC);
"""


def connect():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with connect() as conn:
        conn.executescript(SCHEMA)


def create_user(name, email, password_hash):
    try:
        with connect() as conn:
            cur = conn.execute(
                "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                (name, email, password_hash))
            return cur.lastrowid
    except sqlite3.IntegrityError:
        return None


def get_user_by_email(email):
    with connect() as conn:
        return conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def get_user(user_id):
    with connect() as conn:
        return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()


def save_assessment(user_id, levels, flags, food_group):
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO assessments (user_id, levels, flags, food_group) VALUES (?, ?, ?, ?)",
            (user_id, json.dumps(levels), json.dumps(flags), food_group))
        return cur.lastrowid


def _row(r):
    d = dict(r)
    d["levels"], d["flags"] = json.loads(d["levels"]), json.loads(d["flags"])
    return d


def get_assessment(user_id, assessment_id):
    with connect() as conn:
        r = conn.execute("SELECT * FROM assessments WHERE id = ? AND user_id = ?",
                         (assessment_id, user_id)).fetchone()
    return _row(r) if r else None


def list_assessments(user_id, limit=100):
    with connect() as conn:
        rows = conn.execute(
            "SELECT * FROM assessments WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, limit)).fetchall()
    return [_row(r) for r in rows]


def delete_assessment(user_id, assessment_id):
    with connect() as conn:
        conn.execute("DELETE FROM assessments WHERE id = ? AND user_id = ?",
                     (assessment_id, user_id))

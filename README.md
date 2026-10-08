# 💊 Vitamin Deficiency Prediction & Food Recommendation

Vitamin deficiency prediction and food recommendation, built with Flask, scikit-learn and SQLite.

## Features
- Register / sign in (hashed passwords, CSRF protection, per-user data)
- Enter levels for vitamins A, B, C, D, E and K and get an instant low/normal result
- Food plan with specific foods, why each vitamin matters and possible signs of deficiency
- Every check is saved in SQLite; view history and delete reports
- Download any report as a PDF

## Run it
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py                    # open http://127.0.0.1:5000
```
The SQLite database (`instance/vitamin.db`) and a secret key are created automatically on first run.
Optional environment variables: `SECRET_KEY`, `PORT`, `FLASK_DEBUG=1`.

## Project layout
```
app.py          routes, auth, validation
db.py           SQLite access (parameterised queries)
predictor.py    KNN models trained once at start-up
report.py       PDF report (ReportLab)
knowledge.py    vitamin info, foods, food groups
data/           training data (CSV)
templates/ static/
```

## Notes on the model and data
- One KNN classifier per vitamin predicts low/normal from the level; a second KNN picks a food-group pattern from the combination of low vitamins.
- The dataset is synthetic with clean cut-offs, so test accuracy is ~100%. That does not mean clinical accuracy.
- The original dataset labelled **Vitamin D backwards** (20-40 marked "not deficient"). This is corrected in `predictor.py`.
- Values use the dataset's scale (no units are given in the source). Check your lab report's units before entering values.
- Educational tool only, not a medical diagnosis.

"""Machine-learning layer. Models are trained once at start-up (not per request)."""
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

DATA = Path(__file__).parent / "data"
VITS = ["A", "B", "C", "D", "E", "K"]


def _load_levels() -> pd.DataFrame:
    df = pd.read_csv(DATA / "vitamin_levels.csv")
    # The source dataset labels Vitamin D backwards (20-40 = "not deficient",
    # 41-80 = "deficient"), unlike every other vitamin. Low D is the deficient
    # side, so the label is flipped here.
    df["D_def"] = 1 - df["D_def"]
    return df


class Predictor:
    def __init__(self):
        levels = _load_levels()
        self.models, self.accuracy, self.ranges, self.cutoffs = {}, {}, {}, {}
        for v in VITS:
            X, y = levels[[v]], levels[f"{v}_def"]
            X_tr, X_te, y_tr, y_te = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y)
            clf = KNeighborsClassifier(n_neighbors=5).fit(X_tr, y_tr)
            self.models[v] = clf
            self.accuracy[v] = round(accuracy_score(y_te, clf.predict(X_te)) * 100, 1)
            self.ranges[v] = (float(levels[v].min()), float(levels[v].max()))
            self.cutoffs[v] = float(levels.loc[levels[f"{v}_def"] == 1, v].max())

        groups = pd.read_csv(DATA / "food_groups.csv")
        self.group_model = KNeighborsClassifier(n_neighbors=3).fit(
            groups[VITS], groups["group"])

    def predict(self, values: dict) -> dict:
        """values: {'A': 3.2, ...} -> deficiency flags + food-group id."""
        flags = {}
        for v in VITS:
            x = pd.DataFrame({v: [values[v]]})
            flags[v] = int(self.models[v].predict(x)[0])
        group = None
        if any(flags.values()):
            row = pd.DataFrame([[flags[v] for v in VITS]], columns=VITS)
            group = int(self.group_model.predict(row)[0])
        return {"flags": flags, "group": group}

    @property
    def overall_accuracy(self) -> float:
        return round(sum(self.accuracy.values()) / len(self.accuracy), 1)


predictor = Predictor()

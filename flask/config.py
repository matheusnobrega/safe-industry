import pandas as pd

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

COLUMN_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak",
    "slope", "ca", "thal", "target"
]

Z1 = pd.read_csv(URL, names=COLUMN_NAMES, sep=',')
Z1 = Z1.replace("?", 0.0)

X = Z1.drop("target", axis=1).values.tolist()
Y = Z1["target"].values.tolist()
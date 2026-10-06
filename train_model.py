from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib


X, y = load_iris(return_X_y=True)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=200))
])

model.fit(X, y)

joblib.dump(model, "model.joblib")

print("Model trained and saved.")
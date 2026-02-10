from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X, y):
    model = RandomForestClassifier(
        n_estimators=400,
        max_depth=10,
        class_weight="balanced"
    )
    model.fit(X, y)
    joblib.dump(model, "model/btts_model.pkl")

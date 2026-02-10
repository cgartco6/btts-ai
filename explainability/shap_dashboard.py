import shap
import joblib

def explain(model_path, X):
    model = joblib.load(model_path)
    explainer = shap.TreeExplainer(model)
    return explainer.shap_values(X)

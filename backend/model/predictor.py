import joblib
import pandas as pd
from pathlib import Path

MODELS = {
    "rf":    joblib.load(Path(__file__).parent / "rf_balanceado_refinado.pkl"),
}

def predict_price(model_key: str, input_data: dict) -> float:
    model = MODELS[model_key]           # ← obtiene el estimador correcto
    df = pd.DataFrame([input_data])
    pred = model.predict(df)[0]
    return round(float(pred), 2)

from fastapi import FastAPI, Query
from pydantic import BaseModel
from model.predictor import predict_price, MODELS

app = FastAPI(title="Vehicle Price API")

@app.get("/")
def read_root():
    return {"status": "OK", "endpoints": ["/predict", "/docs"]}

class Vehicle(BaseModel):
    year: int
    odometer: float
    cylinders: str
    manufacturer: str
    paint_color: str
    state: str

@app.post("/predict")
def get_prediction(
    vehicle: Vehicle,
    model: str = Query("rf", enum=list(MODELS.keys()))
):
    price = predict_price(model, vehicle.dict())
    return {"predicted_price": price}


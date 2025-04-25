import streamlit as st
import pandas as pd
import joblib
import json
import numpy as np

# Cargar nuestro .json
with open("options.json", "r") as f:
    options = json.load(f)

# Cargar modelo
model = joblib.load("modelo_pipeline.pkl")

st.title("🚘Bienvenido a Wagen SA")
st.subheader("🔮Predice el precio de tu vehículo usado")
st.markdown(
    """
    Esta aplicación te permite predecir el precio de un vehículo usado basado en sus características.
    Selecciona las opciones a continuación y haz clic en "Predecir precio".
    """
)

# Interfaz de usuario
brand = st.selectbox("Marca", options["brands"])
color = st.selectbox("Color", options["colors"])
cylinders = st.selectbox("Cilindros", options["cylinders"])
state = st.selectbox("Estado", options["states"])
# year = st.slider("Año", 1980, 2025, 2015)
# odometer = st.number_input("Odómetro (millas)", min_value=0, value=50000)
# type_ = st.selectbox("Tipo de vehículo", ["sedan", "SUV", "truck", "pickup", "coupe", "convertible", "other"])

# Procesamiento de entrada
input_data = pd.DataFrame({
    "brand": [brand],
    "color": [color],
    "cylinders": [cylinders],
    "state": [state],
   # "year": [year],
    # "odometer": [odometer],
    # "type": [type_],
})

# Aquí deberías aplicar cualquier preprocesamiento que usaste en entrenamiento

# Predicción
if st.button("Predecir precio"):
    try:
        pred_log = model.predict(input_data)[0]
        prediction = np.expm1(pred_log)  # ← aplicar postprocesamiento
        st.success(f"Precio estimado: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error al predecir: {e}")

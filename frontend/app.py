import streamlit as st
import pandas as pd
import joblib
import json
import numpy as np

# Configuración de la página
st.title("🚘 Bienvenido a Wagen SA")
st.subheader("🔮 Predice el precio de tu vehículo usado")

st.markdown("""
Esta aplicación te permite predecir el precio de un vehículo usado basado en sus características.
Selecciona las opciones a continuación y haz clic en "Predecir precio".
""")

# Cargar modelo (asegúrate que sea el modelo con Pipeline)
@st.cache_resource
def load_model():
    return joblib.load("modelo_pipeline.pkl") 

model = load_model()

# Función de postprocesamiento (si usaste log1p al entrenar)
def post_process(prediction):
    precio_real = np.expm1(prediction)  # destransformar predicción logarítmica
    return {
        "precio_estimado": f"${precio_real:,.2f}",
        "rango": f"${round(precio_real * 0.95):,} - ${round(precio_real * 1.05):,}"
    }

# Cargar opciones desde JSON
with open("options.json", "r") as f:
    options = json.load(f)

# Interfaz de usuario
brand = st.selectbox("Marca", options["brands"])
color = st.selectbox("Color", options["colors"])
cylinders = st.selectbox("Cilindros", options["cylinders"])
conditions = st.selectbox("Condición", options["conditions"])
state = st.selectbox("Estado (US)", options["states"])
year = st.slider("Año", 1980, 2025, 2015)
odometer = st.number_input("Odómetro (millas)", min_value=0, value=50000)

# Crear input para predicción
input_data = pd.DataFrame([{
    "brand": brand,
    "color": color,
    "cylinders": cylinders,
    "conditions": conditions,
    "state": state,
    "year": year,
    "odometer": odometer
}])

# Predicción
if st.button("Predecir precio"):
    try:
        pred_log = model.predict(input_data)[0]
        result = post_process(pred_log)

        st.success("✅ Predicción completada!")
        st.metric("Precio estimado", result["precio_estimado"])
        st.caption(f"Rango probable: {result['rango']}")

        with st.expander("🔍 Detalles técnicos"):
            st.write("Entrada:", input_data)
            st.write("Predicción (log):", pred_log)

    except Exception as e:
        st.error(f"❌ Error al predecir: {e}")

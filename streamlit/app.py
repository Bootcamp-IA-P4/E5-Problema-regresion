import streamlit as st
import pandas as pd
import joblib
import json
import numpy as np

# Configuración
st.title("🚘 Bienvenido a Wagen SA")
st.subheader("🔮 Predice el precio de tu vehículo usado")

st.markdown("""
Esta aplicación predice el precio de un vehículo usado basado en sus características.
Selecciona las opciones a continuación y haz clic en "Predecir precio".
""")

# Cargar modelo
@st.cache_resource
def load_model():
    return joblib.load("modelo_pipeline.pkl")

model = load_model()

# Función de postprocesamiento (si predices log(price))
def post_process(prediction):
    precio_real = np.expm1(prediction)  # Cambia si no usaste log1p
    return {
        "precio_estimado": f"${precio_real:,.2f}",
        "rango": f"${round(precio_real * 0.95):,} - ${round(precio_real * 1.05):,}"
    }

# Cargar opciones
with open("options.json", "r") as f:
    options = json.load(f)

# Opciones fijas adicionales
fuel_options = ["gas", "diesel", "electric", "hybrid", "other"]
type_options = ["sedan", "SUV", "pickup", "convertible", "truck", "other"]
drive_options = ["4wd", "fwd", "rwd", "other"]
transmission_options = ["automatic", "manual", "other"]
title_status_options = ["clean", "salvage", "rebuilt", "lien", "missing", "other"]
states_options = ["al", "ak", "az", "ar", "ca", "co", "ct", "dc", "de", "fl", "ga", "hi", "ia", "id", "il", "in",
                  "ks", "ky", "la", "ma", "md", "me", "mi", "mn", "mo", "ms", "mt", "nc", "nd", "ne", "nh", "nj",
                  "nm", "nv", "ny", "oh", "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "va", "vt", "wa",
                  "wi", "wv", "wy"]

# Formulario
manufacturer = st.selectbox("Marca", options["brands"])
condition = st.selectbox("Condición", options["conditions"])
fuel = st.selectbox("Tipo de combustible", fuel_options)
state = st.selectbox("Estado (EE.UU.)", states_options)
paint_color = st.selectbox("Color", options["colors"])
type_ = st.selectbox("Tipo de vehículo", type_options)
drive = st.selectbox("Tracción", drive_options)
transmission = st.selectbox("Transmisión", transmission_options)
title_status = st.selectbox("Estado del título", title_status_options)
year = st.slider("Año", 1980, 2025, 2015)
odometer = st.number_input("Odómetro (millas)", min_value=0, value=50000)
cylinders = st.selectbox("Cilindros", options["cylinders"])

# Crear input
input_data = pd.DataFrame([{
    "manufacturer": manufacturer,
    "condition": condition,
    "fuel": fuel,
    "state": state,
    "paint_color": paint_color,
    "type": type_,
    "drive": drive,
    "transmission": transmission,
    "title_status": title_status,
    "year": year,
    "odometer": odometer,
    "cylinders": cylinders
}])

# Predicción
if st.button("Predecir precio"):
    try:
        pred = model.predict(input_data)[0]
        result = post_process(pred)

        st.success("✅ Predicción completada!")
        st.metric("Precio estimado", result["precio_estimado"])
        st.caption(f"Rango probable: {result['rango']}")

        with st.expander("🔍 Detalles técnicos"):
            st.write("Entrada:", input_data)
            st.write("Predicción cruda:", pred)

    except Exception as e:
        st.error(f"❌ Error al predecir: {e}")

import streamlit as st
import pandas as pd
import joblib
import json
import pickle
import numpy as np

# Configuración de la página
st.title("🚘Bienvenido a Wagen SA")
st.subheader("🔮Predice el precio de tu vehículo usado")
st.markdown(
    """
    Esta aplicación te permite predecir el precio de un vehículo usado basado en sus características.
    Selecciona las opciones a continuación y haz clic en "Predecir precio".
    """
)

# Cargar modelo (con cache para mejor performance)
@st.cache_resource
def load_model():
    with open('rf_balanceado_refinado.pkl', 'rb') as f:
        return pickle.load(f)

model_data = load_model()
model = model_data['model']

# Función de post-procesamiento (opcional)
def post_process(prediction):
    # Ejemplo: redondear precio y formatear como moneda
    precio_redondeado = round(prediction, 2)
    return {
        "precio_estimado": f"${precio_redondeado:,.2f}",
        "rango": (
            f"${round(prediction*0.95):,} - ${round(prediction*1.05):,}"
            if prediction > 10000 
            else "Estimación precisa"
        )
    }
# Cargar nuestro .json
with open("options.json", "r") as f:
    options = json.load(f)

# Cargar modelo
#model = joblib.load("rf_balanceado_refinado.pkl")


# Interfaz de usuario
brand = st.selectbox("Marca", options["brands"])
color = st.selectbox("Color", options["colors"])
cylinders = st.selectbox("Cilindros", options["cylinders"])
conditions = st.selectbox("Estado", options["conditions"])


# Predicción
if st.button("Predecir precio"):
     # Crear DataFrame con el formato correcto
    input_data = pd.DataFrame({
        "brand": [brand],
        "color": [color],
        "cylinders": [cylinders],
        "conditions": [conditions],
    })
    try:
        # Preprocesamiento y predicción automáticos
        prediction = model.predict(input_data)[0]
        
        # Post-procesamiento
        result = post_process(prediction)
        
        # Mostrar resultados
        st.success("Predicción completada!")
        
        st.metric("Precio Estimado", result['precio_estimado'])
        st.caption(f"Rango probable: {result['rango']}")
        
        # Detalles técnicos (opcional)
        with st.expander("Detalles técnicos"):
            st.write("Valor bruto estimado:", prediction)
            st.write("Características usadas:", input_data.to_dict())
    
    except Exception as e:
        st.error(f"Error en la predicción: {str(e)}")
    
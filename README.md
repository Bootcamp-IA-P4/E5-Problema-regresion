[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Model Performance](https://img.shields.io/badge/R%C2%B2-0.85-green.svg)](#-resultados)  

---

## 📢 Proyecto “Wagen SA Price Predictor”

**Sistema inteligente de predicción de precios de vehículos usados** construido con técnicas de Machine Learning, enfocado en **Regresión Lineal** y comparativa con modelos avanzados.

> 🚀 **Impacto:** Ayuda a concesionarios y particulares a estimar con precisión el valor de autos usados, optimizando decisiones de compra/venta.

---

## 📋 Tabla de Contenidos

1. [🎯 Objetivo](#-objetivo)  
2. [✨ Características Clave](#-características-clave)  
3. [🛠️ Instalación & Ejecución](#️-instalación--ejecución)  
4. [📂 Estructura del Repositorio](#-estructura-del-repositorio)  
5. [📊 Dataset](#-dataset)  
6. [🔍 Análisis Exploratorio (EDA)](#-análisis-exploratorio-eda)  
7. [⚙️ Preprocesamiento](#️-preprocesamiento)  
8. [🤖 Modelado](#-modelado)  
9. [🔮 Resultados](#-resultados)
10. [📌 Conclusiones](#-conclusiones)  
11. [🚧 Trabajo Futuro](#-trabajo-futuro)  
12. [🤝 Contribuir](#-contribuir)    
13. [🤝 Contribución](#️-contribición)  

---

## 🎯 Objetivo

Construir un **modelo predictivo** que estime el precio de un vehículo usado en EE.UU. a partir de sus características (marca, año, condición, etc.), priorizando:

- **Interpretabilidad** (Regresión Lineal / Ridge)  
- **Precisión** (Comparativa con Random Forest)  

---

## ✨ Características Clave

- 📈 **Modelos Múltiples:**  
  - Regresión Lineal Simple y Múltiple  
  - Regresión Ridge (L2)  
  - Random Forest (benchmark no lineal)  
- ⚖️ **Regularización & Validación Cruzada:** Evita overfitting y ajusta hiperparámetros con GridSearchCV.  
- 🛠️ **Pipeline Reproducible:** Desde limpieza hasta despliegue con Streamlit.  
- 📊 **Visualizaciones Interactivas:** Entiende patrones de precio por marca, año y tipo de carrocería.  
- 🔒 **Producción Ligera:** Modelo Ridge serializado listo para integrarse en APIs o microservicios.  

---

## 🛠️ Instalación & Ejecución

> **Requisito:** Python ≥ 3.10

### 1️⃣ Clonar repo
```textplain
git clone https://github.com/Bootcamp-IA-P4/E5-Problema-regresion.git
cd E5-Problema-regresion
```
### 2️⃣ Crear y activar entorno virtual
``` textplain
python3.10 -m venv .venv
```
 macOS/Linux
```textplain
source .venv/bin/activate
``` 
 Windows
 ```
# .venv\Scripts\activateç
```   

### 3️⃣ Instalar dependencias
```textplain
pip install -r requirements.txt
```

> [!TIP]
> Con `pip list` puedes visualizar todas las dependencias descargadas.

### 4️⃣ Ejecutar dashboard
```textplain
streamlit run app.py
```

----

## 📂 Estructura del Repositorio
```
├── Datas
|──── Vehicles_prep.csv                 # Dataset preprocesado y limpio
├── Notebooks
|──── EDA.ipynb             # Notebook de Análisis Exploratorio de Datos (EDA)
├──── Regresión.ipynb         # Notebook del modelo de regresión
├──── Regresión_pipeline.ipynb         # Notebook del modelo de regresión con preprocesado pipeline
├── streamlit
├─── model
├────── rf_balanceado_refinado.pkl       # Modelo Random Forest entrenado y balanceado
├────── modelo_pipeline                  # Modelo Random Forest entrenado y balanceado con preprocesado
├────── model_pipeline                  # Modelo Random Forest entrenado y balanceado con preprocesado
├──── app.py                            # App Streamlit para predicción interactiva  
├──── options.json             # Listas de valores categóricos (marcas, colores, cilindros, estados)
├── README.md                         # Documentación del proyecto                 
└── requirements.txt 

```

---

## 📊 Dataset

Origen: Publicaciones reales de autos usados en línea (EE.UU.).

**Características Principales del Dataset:**
- Año de fabricación (`year`)
- Marca (`brand`)
- Modelo (`model`)
- Tipo de carrocería (`type`)
- Estado de publicación (`state`)
- Número de cilindros (`cylinders`)
- Condición del vehículo (`condition`)
- Transmisión (`transmission`)
- Color (`paint_color`)
- Precio (`price`, variable objetivo)

**Tamaño:** +400,000 registros antes del preprocesamiento.

---

## 🔍 Análisis Exploratorio de Datos (EDA)

Realizado en el notebook `EDA.ipynb`, donde se incluyen:

- Análisis univariado (distribuciones)
- Análisis bivariado (correlaciones, precios por tipo/marca/año)
- Identificación de outliers y valores nulos
- Transformaciones y limpieza de variables
- Visualizaciones interactivas para entender patrones

---

## ⚙️ Preprocesamiento

1. Eliminación de registros con valores faltantes críticos

2. One-Hot Encoding de variables categóricas

3. Normalización de variables numéricas

4. Balanceo para Random Forest

5. Exportación a vehicles_prep.csv

---

## 🤖 Modelado

Se entrenaron y evaluaron múltiples modelos:

### 📐 Modelos Implementados
- **Regresión Lineal Simple y Múltiple**
- **Regresión Ridge**
  - Regularización L2 para reducir el overfitting.
- **Random Forest**
  - Uso como modelo comparativo no lineal.
  - Mejor desempeño general, almacenado en `rf_balanceado_refinado.pkl`.
    
Modelo | Regularización | Validación | Hiperparámetros
Regresión Lineal | – | K-Fold (k=5) | –
Ridge | L2 | GridSearchCV | alpha ∈ [0.1, 1, 10, 100]
Random Forest | – | GridSearchCV | n_estimators, max_depth, min_samples_split

### 📏 Métricas de Evaluación
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de Determinación)

Modelo | R² Score | RMSE | MAE
Regresión Lineal | 0.68 | 3 500 $ | 2 500 $
Ridge | 0.70 | 3 400 $ | 2 400 $
Random Forest | 0.85 | 2 200 $ | 1 700 $

### 📈 Validación
- Validación cruzada K-Fold
- GridSearchCV para optimización de hiperparámetros

---

## 🔮 Resultados

| Modelo           | R² Score | RMSE    | MAE     |
|------------------|----------|---------|---------|
| Regresión Lineal | 0.68     | ~3500   | ~2500   |
| Ridge Regression | 0.70     | ~3400   | ~2400   |
| Random Forest    | **0.85** | **2200**| **1700**|

> El modelo Random Forest mostró el mejor desempeño general, pero la regresión Ridge fue efectiva y explicable, siendo ideal para producción ligera.

---

## 📆 Archivos de Configuración

El archivo `options.json` contiene las posibles opciones categóricas para facilitar la limpieza y validación de datos, incluyendo:

- `brands`: marcas válidas (e.g. toyota, ford, bmw...)
- `colors`: colores posibles
- `cylinders`: número de cilindros
- `states`: estados abreviados de EE.UU.

---

## 📌 Conclusiones

- La regresión lineal sigue siendo una técnica válida para problemas de regresión cuando se requiere interpretabilidad.
- La combinación de análisis exploratorio y regularización (Ridge) permite mejorar el desempeño y reducir el overfitting.
- El uso de modelos más complejos como Random Forest mejora notablemente las métricas pero a costa de interpretabilidad.

## 🚧 Trabajo Futuro
Integrar features de texto (descripciones de anuncios)

Despliegue en nube (Docker + AWS/GCP)

Probar XGBoost y LightGBM

Añadir AutoML para selección automática de modelo

---

## 🤝 Contribución  

¡Las contribuciones son bienvenidas! Para contribuir:  

1. Haz un fork del repositorio.
   
3. Crea una nueva rama:
    
   ```sh
   git checkout -b feature/nueva-funcionalidad
   ```
   
4. Realiza tus cambios y haz commit:
   
  ```sh
git commit -m "Añadir nueva funcionalidad"
```

4. Envía un pull request 🚀.
   
---
## 🚀 ¡Gracias por usar ! Si tienes preguntas, crea un issue en el repositorio o contáctanos.

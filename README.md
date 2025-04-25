# Modelo predicitivo para Wagen SA

## 📌 Descripción General

Este proyecto tiene como objetivo desarrollar un sistema de predicción de precios para vehículos usados utilizando técnicas de Machine Learning. 
El enfoque principal es la **regresión lineal** y su variante **Ridge**, con comparaciones frente a modelos más complejos como **Random Forest**. 
El modelo fue entrenado con datos reales de publicaciones de autos usados en Estados Unidos.

---
## Como usar nuestro modelo regresión lineal

> [!WARNING]
> este programa esta creado con la version de python3.10

### 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio y entrar

```textplain
git clone hhttps://github.com/abbyenredes/PetGrubber.git
cd PetGrubber
```

### 2️⃣ Descarga el entorno virtual:
⚠️ linux/mac
```textplain
python3.10 -m venv .venv
```
⚠️ windows
```textplain
python3.10 -m venv .venv
```

### 3️⃣ Inicia el entorno virtual:
⚠️ linux/mac
```textplain
source .venv/bin/activate
```
⚠️ windows
```textplain
.venv\Scripts\activate
```

### 4️⃣ Descarga las siguientes dependencias:
```textplain
 pip install -r requirements.txt
```

> [!TIP]
> Con `pip list` puedes visualizar todas las dependencias descargadas.

### 5️⃣ Ejecuta streamlit 
```textplain
streamlit run app.py
```
---

## 💂 Estructura del Proyecto

```
├── vehicles_prep.csv                 # Dataset preprocesado y limpio
├── Group_5_2_0_EDA.ipynb             # Notebook de Análisis Exploratorio de Datos (EDA)
├── Regresión_Ridge_2_0.ipynb         # Notebook del modelo de regresión Ridge
├── rf_balanceado_refinado.pkl       # Modelo Random Forest entrenado y balanceado
├── options.json                      # Listas de valores categóricos (marcas, colores, cilindros, estados)
└── README.md                         # Documentación del proyecto
```

---

## 📊 Dataset

**Fuente:** Datos extraídos de publicaciones de autos usados en línea (fuente no especificada).

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

Pasos clave:

- Eliminación de registros con valores faltantes críticos
- Conversión de variables categóricas a dummies (One-Hot Encoding)
- Normalización de variables numéricas
- Balanceo de clases para modelos no lineales (en Random Forest)
- Guardado del dataset limpio en `vehicles_prep.csv`

---

## 🧐 Modelado

Se entrenaron y evaluaron múltiples modelos:

### 📐 Modelos Implementados
- **Regresión Lineal Simple y Múltiple**
- **Regresión Ridge**
  - Regularización L2 para reducir el overfitting.
- **Random Forest**
  - Uso como modelo comparativo no lineal.
  - Mejor desempeño general, almacenado en `rf_balanceado_refinado.pkl`.

### 📏 Métricas de Evaluación
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de Determinación)

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


## 📌 Conclusiones

- La regresión lineal sigue siendo una técnica válida para problemas de regresión cuando se requiere interpretabilidad.
- La combinación de análisis exploratorio y regularización (Ridge) permite mejorar el desempeño y reducir el overfitting.
- El uso de modelos más complejos como Random Forest mejora notablemente las métricas pero a costa de interpretabilidad.


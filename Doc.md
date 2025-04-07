# Regresión por Mínimos Cuadrados Parciales (PLS)

Este documento es una introducción clara y sencilla al algoritmo de **Regresión por Mínimos Cuadrados Parciales (PLS)**.
---

## 📄 Introducción

La regresión por Mínimos Cuadrados Parciales (PLS, por sus siglas en inglés) es una técnica estadística que combina la reducción de dimensionalidad con la regresión. Se utiliza especialmente cuando hay muchas variables independientes que están altamente correlacionadas o cuando hay más variables que observaciones.

---

## 🔠 ¿Cuándo se usa?

- Cuando existe **multicolinealidad** entre las variables predictoras.
- Cuando el número de variables es **muy alto**.
- En contextos como la química, biología, economía y ciencias de datos:
  * Química (para predecir propiedades de mezclas)

  * Marketing (para predecir comportamiento del consumidor)

   * Bioinformática (con muchos genes y pocas muestras)
     
   * Machine learning cuando hay pocos datos y muchas columnas

---

## 🔢 Fundamento Matemático Básico

PLS transforma las variables originales \( X \) e \( Y \) en nuevos componentes latentes que explican la mayor parte de su covarianza.

```latex
X = T P^T + E 
Y = U Q^T + F
```

- \( T \), \( U \): Componentes latentes (scores)
- \( P \), \( Q \): Cargas (loadings)
- \( E \), \( F \): Residuos

PLS busca encontrar componentes que **maximicen la covarianza entre X y Y**.

---

## 🚀 Parámetros Principales

| Parámetro        | Descripción                                                  |
|------------------|-------------------------------------------------------------|
| `n_components`   | Número de componentes a extraer.                            |
| `scale`          | Si se estandarizan o no las variables.                      |
| `algorithm`      | Método de solución: 'nipals' (por defecto) o 'svd'.          |
| `max_iter`       | Máximo número de iteraciones.                              |
| `tol`            | Tolerancia para convergencia.                               |

---

## 🧪 Ejemplo en Python

```python
import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Datos simulados
np.random.seed(42)
X = np.random.normal(size=(100, 10))
y = X[:, 0]*3 + X[:, 1]*-2 + np.random.normal(size=100)
y = y.reshape(-1, 1)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear modelo
pls = PLSRegression(n_components=2)
pls.fit(X_train, y_train)

# Predicción
y_pred = pls.predict(X_test)

# Evaluación
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse:.2f}")

# Visualización
plt.scatter(y_test, y_pred)
plt.xlabel("Valores Reales")
plt.ylabel("Predicciones")
plt.title("PLS: Predicciones vs Reales")
plt.grid(True)
plt.show()
```

---

## ✅ Ventajas y ❌ Desventajas

### Ventajas
- Resuelve problemas de multicolinealidad.
- Reduce dimensionalidad.
- Funciona bien cuando hay pocas observaciones y muchas variables.

### Desventajas
- Menor interpretabilidad que modelos tradicionales.
- Elegir el número óptimo de componentes puede requerir validación cruzada.

---

## 📚 Bibliografía

1. Estadística ITM. (s.f.). *Regresión PLS*. https://estadisticaitm.github.io/pls.html  
2. del Val, D. *Modelos matemáticos PLS*. https://delvaldavid.com/files/tfg_math.pdf  
3. Vega Vilca, R. (2018). *Introducción a PLS*. https://www.uprm.edu/wp-content/uploads/sites/171/2018/12/vegavilca.pdf  
4. SCIELO Venezuela. (2003). *Comparación de regresiones multivariadas*. https://ve.scielo.org/ 
5. Universidad Nacional de Colombia. (2016). *Análisis de regresión PLS*. https://repositorio.unal.edu.co/handle/unal/57110



   No copiar esto! Solo para uso de busqueda de informacion
[PLS](https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S0254-07702003000300006)

[Mínimos cuadrados parciales (PLS)](https://delvaldavid.com/files/tfg_math.pdf)

[GENERALIZACIONES DE MINIMOS CUADRADOS PARCIALES CON APLICACIÓN EN CLASIFICACION SUPERVISADA](https://www.uprm.edu/wp-content/uploads/sites/171/2018/12/vegavilca.pdf)

[Regresión por Mínimos Cuadrados Parciales P LS Aplicada a Datos Variedad Valuados](https://repositorio.unal.edu.co/bitstream/handle/unal/57110/8105560.2016.pdf)

[¿Qué es la regresión de mínimos cuadrados parciales?](https://support.minitab.com/es-mx/minitab/help-and-how-to/statistical-modeling/regression/supporting-topics/partial-least-squares-regression/what-is-partial-least-squares-regression/)

[Regresión de mínimos cuadrados parciales](https://estadisticaitm.github.io/pls.html) este es el mas importante


dataset: [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)

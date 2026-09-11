# Taller: Análisis Exploratorio y PCA - Gestión de Recursos Humanos

## Información General
- **Curso:** Análisis de Datos Multivariado
- **Dataset:** IBM HR Analytics Employee Attrition & Performance
- **Puntaje Total:** 100 puntos (+10 puntos bonus)
- **Duración estimada:** 2-3 horas

---

## Descripción del Dataset

El dataset contiene información de empleados de una empresa, incluyendo variables demográficas, laborales y de desempeño. Las variables principales que utilizaremos son:

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `Age` | Edad del empleado | Numérica |
| `MonthlyIncome` | Ingreso mensual | Numérica |
| `YearsAtCompany` | Años en la empresa | Numérica |
| `TotalWorkingYears` | Años totales de experiencia laboral | Numérica |
| `DistanceFromHome` | Distancia del hogar al trabajo | Numérica |
| `NumCompaniesWorked` | Número de empresas en las que ha trabajado | Numérica |
| `Department` | Departamento (Sales, R&D, HR) | Categórica |
| `Attrition` | Si el empleado dejó la empresa (Yes/No) | Categórica |

**Descarga del dataset:** [IBM HR Analytics](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## Instrucciones Generales

1. Cree un nuevo Jupyter Notebook para desarrollar el taller
2. Documente su código con comentarios explicativos
3. Responda las preguntas teóricas en celdas Markdown
4. Incluya títulos y etiquetas en todos sus gráficos

---

## Parte 1: Exploración de Datos con Pandas (25 puntos)

### Preguntas Teóricas

**PT1.1** (2 puntos) ¿Cuál es la diferencia entre los métodos `.head()` y `.describe()` en Pandas? ¿Qué información proporciona cada uno?

**PT1.2** (2 puntos) Explique qué son los valores faltantes (NaN) en un DataFrame y mencione dos estrategias para manejarlos. ¿En qué casos utilizaría cada estrategia?

**PT1.3** (2 puntos) ¿Cuál es la diferencia entre `.loc[]` y `.iloc[]` para seleccionar datos en Pandas? Proporcione un ejemplo de uso de cada uno.

**PT1.4** (2 puntos) Explique el funcionamiento del método `.groupby()`. ¿Qué operaciones se pueden realizar después de agrupar los datos?

---

### Ejercicios Prácticos

**EP1.1 Exploración inicial** (5 puntos)

Cargue el dataset y realice las siguientes operaciones:

```python
# Importe las librerías necesarias
import pandas as pd
import numpy as np

# Cargue el dataset
df = pd.read_csv('IBM_HR_Employee.csv')

# a) Muestre las primeras 10 filas del dataset
# b) Muestre los tipos de datos de cada columna
# c) Genere estadísticas descriptivas de las variables numéricas
```

**EP1.2 Manejo de valores faltantes** (5 puntos)

```python
# a) Cuente el número de valores faltantes por columna
# b) Elimine las filas que contengan valores faltantes
# c) Verifique que ya no existen valores faltantes
```

**EP1.3 Selección y filtrado** (5 puntos)

```python
# a) Seleccione únicamente las 6 columnas numéricas: 
#    Age, MonthlyIncome, YearsAtCompany, TotalWorkingYears, 
#    DistanceFromHome, NumCompaniesWorked

# b) Filtre los empleados del departamento "Sales"

# c) Filtre los empleados con MonthlyIncome > 5000 
#    Y YearsAtCompany > 5
```

**EP1.4 Agrupación y agregación** (5 puntos)

```python
# a) Calcule el promedio de las variables numéricas 
#    agrupado por Department

# b) Cuente el número de empleados por Department y Attrition
```

**EP1.5 Pregunta de análisis** (3 puntos)

Basándose en los resultados anteriores, responda:
- ¿Qué departamento tiene el mayor ingreso promedio?
- ¿Qué departamento tiene la mayor tasa de rotación (Attrition)?
- Justifique sus respuestas con los valores numéricos obtenidos.

---

## Parte 2: Visualización de Datos (35 puntos)

### Preguntas Teóricas

**PT2.1** (2 puntos) ¿Qué es una curva de densidad (KDE) y por qué es útil agregarla a un histograma? ¿Qué ventaja tiene sobre un histograma simple?

**PT2.2** (2 puntos) ¿Cuál es la diferencia entre un boxplot y un violinplot? ¿Qué información adicional proporciona el violinplot?

**PT2.3** (2 puntos) ¿Qué es una matriz de correlación? ¿Cómo se interpreta un valor de correlación de +0.8 vs -0.8 vs 0?

**PT2.4** (2 puntos) ¿Qué es un mapa de calor (heatmap) y por qué es útil para visualizar matrices de correlación? ¿Qué características debe tener un buen mapa de calor?

---

### Ejercicios Prácticos

**EP2.1 Distribuciones univariadas** (10 puntos)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Cree una figura con 4 subplots (2 filas x 2 columnas)
# Cada subplot debe contener un histograma con KDE de:
# a) Age
# b) MonthlyIncome
# c) YearsAtCompany
# d) TotalWorkingYears

# Incluya títulos descriptivos en cada subplot
```

**EP2.2 Boxplots por categoría** (10 puntos)

```python
# a) Cree un boxplot de MonthlyIncome separado por Department

# b) Cree DOS gráficos comparativos usando YearsAtCompany coloreado por Attrition:
#    - Un boxplot
#    - Un violinplot
# Compare visualmente ambos gráficos

# c) Cree un boxplot de Age separado por Attrition
```

**EP2.3 Gráficos de dispersión** (10 puntos)

```python
# a) Cree un scatter plot de Age vs MonthlyIncome, 
#    coloreado por Department (use hue)

# b) Calcule la matriz de correlación de las 6 variables numéricas

# c) Visualice la matriz de correlación usando un heatmap
#    - Use annot=True para mostrar los valores
#    - Use una paleta de colores divergente (ej: 'coolwarm', 'RdBu')
```

**EP2.4 Preguntas de análisis** (5 puntos)

Basándose en sus visualizaciones, responda:

a) ¿Cuáles son las dos variables con mayor correlación positiva? ¿Y la variable con menor correlación con las demás?

b) Observando los boxplots/violinplots de Attrition, ¿qué diferencias observa entre los empleados que permanecen vs los que se van? ¿Qué implicaciones tiene esto para el área de Recursos Humanos?

---

## Parte 3: Análisis de Componentes Principales - PCA (40 puntos)

### Preguntas Teóricas

**PT3.1** (3 puntos) ¿Qué es el Análisis de Componentes Principales (PCA)? Explique en sus propias palabras cuál es el objetivo de esta técnica y cuándo es útil aplicarla.

**PT3.2** (3 puntos) ¿Por qué es **obligatorio** estandarizar los datos antes de aplicar PCA? ¿Qué problemas pueden ocurrir si no se estandarizan? Ilustre con un ejemplo usando las variables MonthlyIncome y Age.

**PT3.3** (3 puntos) ¿Qué representa la "varianza explicada" de un componente principal? Si PC1 tiene 40% de varianza explicada y PC2 tiene 25%, ¿qué significa esto?

**PT3.4** (3 puntos) ¿Qué son las "cargas" (loadings) en PCA? ¿Cómo se utilizan para interpretar el significado de cada componente principal?

**PT3.5** (3 puntos) ¿Cuál es la diferencia entre usar PCA para **reducción de dimensionalidad** vs usarlo para **visualización exploratoria**? ¿Cuántos componentes seleccionaría en cada caso?

---

### Ejercicios Prácticos

**EP3.1 Preparación de datos para PCA** (10 puntos)

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# a) Seleccione las 6 variables numéricas y guárdelas en un DataFrame X

# b) Aplique StandardScaler para estandarizar los datos
#    - Ajuste el scaler y transforme los datos
#    - Guarde los datos escalados en X_scaled

# c) Verifique la estandarización:
#    - Calcule la media de cada variable (debe ser ≈ 0)
#    - Calcule la desviación estándar (debe ser ≈ 1)
```

**EP3.2 Aplicación de PCA** (10 puntos)

```python
# a) Cree un objeto PCA (sin especificar número de componentes)
#    y ajústelo a los datos estandarizados

# b) Cree un DataFrame con:
#    - Componente (PC1, PC2, ..., PC6)
#    - Varianza explicada individual (%)
#    - Varianza explicada acumulada (%)

# c) Cree un gráfico de líneas mostrando:
#    - Varianza acumulada en el eje Y
#    - Número de componentes en el eje X
#    - Agregue una línea horizontal al 80% de varianza
#    - Títulos y etiquetas apropiados
```

**EP3.3 Visualización de resultados PCA** (10 puntos)

```python
# a) Transforme los datos usando PCA y cree un DataFrame 
#    con las puntuaciones de los componentes (PC1, PC2, ...)

# b) Cree un scatter plot de PC1 vs PC2:
#    - Coloreado por Department
#    - Incluya el % de varianza explicada en los ejes
#    - Título: "Proyección PCA - Departamentos"

# c) Cree otro scatter plot de PC1 vs PC2:
#    - Coloreado por Attrition
#    - Analice si hay separación visible entre grupos

# d) Cree un DataFrame con las cargas (loadings):
#    - Filas: nombres de las variables originales
#    - Columnas: PC1, PC2, PC3, ...
#    Hint: use pca.components_.T

# e) Visualice las cargas con un heatmap:
#    - Use annot=True
#    - Use cmap='RdBu' o similar (divergente)
#    - Incluya título y etiquetas
```

**EP3.4 Preguntas de análisis** (10 puntos)

Basándose en sus resultados de PCA, responda las siguientes preguntas:

**a) Selección de componentes** (2.5 puntos)
¿Cuántos componentes principales necesita para explicar al menos el 80% de la varianza total? Justifique su respuesta con los valores de varianza acumulada.

**b) Interpretación de PC1** (2.5 puntos)
Observe las cargas del primer componente principal (PC1):
- ¿Qué variables tienen mayor peso (positivo o negativo)?
- ¿Qué concepto o dimensión subyacente podría representar PC1? 
- Proponga un nombre descriptivo para este componente.

**c) Separación de grupos** (2.5 puntos)
Observando el gráfico de PC1 vs PC2 coloreado por Attrition:
- ¿Existe una separación clara entre empleados que se van vs los que permanecen?
- ¿Qué implicaciones tiene esto para predecir la rotación de empleados?

**d) Importancia de la estandarización** (2.5 puntos)
Considerando las escalas originales de las variables:
- MonthlyIncome: valores en miles (ej: 5000-20000)
- Age: valores en decenas (ej: 25-60)
- DistanceFromHome: valores pequeños (ej: 1-30)

Explique qué pasaría si aplicara PCA **sin** estandarizar los datos. ¿Qué variable dominaría el análisis y por qué?

---

## Ejercicio Bonus: Biplot (10 puntos extra)

Un **biplot** es una visualización avanzada que combina:
- Las puntuaciones de las observaciones (scatter de PC1 vs PC2)
- Los vectores de carga de las variables originales (flechas)


# Interprete: ¿Qué variables apuntan en la misma dirección?
# ¿Qué variables son opuestas? ¿Qué significa esto?
```

---

## Entrega

- **Formato:** Jupyter Notebook (.ipynb)
- **Nombre del archivo:** `Taller_PCA_Apellidos_Nombres.ipynb`
- **Contenido esperado:**
  - Código ejecutable sin errores
  - Respuestas a preguntas teóricas en celdas Markdown
  - Gráficos con títulos y etiquetas
  - Análisis e interpretaciones justificadas
- **Fecha de entrega:** [13-04-2026]
---


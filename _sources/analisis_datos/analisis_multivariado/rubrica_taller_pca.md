# Rúbrica de Evaluación: Taller de PCA y Visualización

## Información General
- **Curso:** Análisis de Datos Multivariado
- **Taller:** Análisis Exploratorio y PCA - Gestión de Recursos Humanos
- **Dataset:** IBM HR Analytics Employee Attrition & Performance
- **Puntaje Total:** 100 puntos (+10 puntos bonus)

---

## Parte 1: Exploración de Datos con Pandas (25 puntos)

### 1.1 Exploración inicial (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Uso correcto de `head()`, `dtypes`, `describe()` | Utiliza correctamente las tres funciones con sintaxis apropiada | Utiliza las funciones correctamente con errores menores | Utiliza al menos dos funciones correctamente | Utiliza solo una función o con errores significativos | No realiza la exploración |

### 1.2 Manejo de valores faltantes (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Conteo de valores faltantes | Usa `isnull().sum()` correctamente | Cuenta valores faltantes con método alternativo válido | Identifica que hay valores faltantes pero método incompleto | Intento incorrecto | No realiza |
| Eliminación de filas con NaN | Usa `dropna()` correctamente | Método alternativo válido | Elimina parcialmente los NaN | Elimina incorrectamente | No realiza |

### 1.3 Selección y filtrado (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Selección de columnas numéricas | Selecciona correctamente las 6 columnas numéricas | Selecciona con sintaxis diferente pero válida | Selecciona parcialmente las columnas | Selección incorrecta | No realiza |
| Filtrado por departamento (Sales) | Filtro correcto y eficiente | Filtro correcto pero verboso | Filtro funcional con errores menores | Filtro incorrecto | No realiza |
| Filtrado con múltiples condiciones | Usa operadores lógicos correctamente (`&`) para MonthlyIncome y YearsAtCompany | Funcional con sintaxis alternativa | Una condición correcta, otra incorrecta | Ambas condiciones incorrectas | No realiza |

### 1.4 Agrupación y agregación (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Uso de groupby con media | `groupby('Department').mean()` correcto con columnas seleccionadas | Método alternativo válido | Agrupa pero usa estadístico incorrecto | groupby incorrecto | No realiza |
| Conteo por Department y Attrition | Conteo correcto con dos variables | Conteo correcto pero presentación confusa | Agrupa solo por una variable | Agrupación incorrecta | No realiza |

### 1.5 Pregunta de análisis (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Identificación correcta | Identifica correctamente departamento con mayor ingreso y mayor rotación | Identifica uno correctamente | Identifica aproximadamente pero sin datos exactos | Identificación incorrecta | No responde |
| Justificación con datos | Cita valores numéricos específicos del análisis | Menciona los datos pero sin valores exactos | Justificación vaga | Sin justificación | No responde |

---

## Parte 2: Visualización de Datos (35 puntos)

### 2.1 Distribuciones univariadas (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Histogramas con KDE | 4 histogramas correctos con `kde=True` | 3-4 histogramas, algunos sin KDE | 2-3 histogramas correctos | Solo 1 histograma o errores graves | No realiza |
| Uso de subplots | Estructura 2x2 correcta, bien organizada | Subplots funcionales pero desorganizados | Gráficos separados sin subplots | Intento fallido de subplots | No realiza |
| Títulos y estética | Títulos descriptivos en cada subplot | Algunos títulos faltantes | Títulos genéricos | Sin títulos | No aplica |

### 2.2 Boxplots por categoría (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Boxplot de MonthlyIncome por Department | `sns.boxplot` correcto con Department | Boxplot funcional con estética básica | Boxplot sin separación por departamento | Gráfico incorrecto | No realiza |
| Comparación boxplot vs violinplot por Attrition | Ambos gráficos correctos (YearsAtCompany y Age), bien comparados | Ambos gráficos pero uno con errores | Solo un tipo de gráfico | Gráficos incorrectos | No realiza |
| Etiquetas y títulos | Títulos descriptivos, etiquetas claras | Algunos elementos faltantes | Etiquetas mínimas | Sin etiquetas | No aplica |

### 2.3 Gráficos de dispersión (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Scatter plot con hue | `sns.scatterplot` con `hue='Department'` correcto (Age vs MonthlyIncome) | Scatter funcional, colores manuales | Scatter sin diferenciación por departamento | Gráfico incorrecto | No realiza |
| Matriz de correlación | `.corr()` + `sns.heatmap` con `annot=True` para las 6 variables | Heatmap correcto sin anotaciones | Correlación calculada, visualización básica | Cálculo incorrecto | No realiza |
| Presentación visual | Colores apropiados, cmap divergente | Funcional pero estética básica | Legible pero mejora necesaria | Difícil de interpretar | No aplica |

### 2.4 Pregunta de análisis (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Insuficiente (1-2) | No realizado (0) |
|----------|---------------|-----------|-------------------|-------------------|------------------|
| Identificación de correlaciones | Identifica correctamente mayor (Age-TotalWorkingYears) y menor correlación (DistanceFromHome) | Una correlación correcta | Identificación aproximada | Identificación incorrecta | No responde |
| Análisis Attrition y retención | Explica diferencias entre empleados que se van vs permanecen, implicaciones para RRHH | Observación correcta pero explicación básica | Observación parcial | Análisis incorrecto | No responde |

---

## Parte 3: Análisis de Componentes Principales (40 puntos)

### 3.1 Preparación de datos para PCA (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Extracción de variables numéricas | Selección correcta de las 6 columnas (Age, MonthlyIncome, YearsAtCompany, etc.) | Selección correcta con sintaxis diferente | Algunas columnas faltantes o extras | Selección incorrecta de datos | No realiza |
| Estandarización | `StandardScaler.fit_transform()` correcto, media≈0, std≈1 | Estandarización correcta verificada | Estandarización sin verificación | Datos no estandarizados correctamente | No realiza |

### 3.2 Aplicación de PCA (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Creación y ajuste de PCA | `PCA().fit_transform()` correcto | PCA funcional con sintaxis alternativa | PCA aplicado pero transformación incorrecta | Errores en la aplicación | No realiza |
| DataFrame de varianza explicada | DataFrame completo con varianza individual y acumulada (6 componentes) | DataFrame con varianza pero formato básico | Solo varianza explicada sin acumular | Cálculo incorrecto | No realiza |
| Gráfico de varianza acumulada | Gráfico correcto con línea al 80%, títulos y etiquetas | Gráfico correcto sin línea referencia | Gráfico básico funcional | Gráfico incorrecto o no informativo | No realiza |

### 3.3 Visualización de resultados PCA (10 puntos)

| Criterio | Excelente (10) | Bueno (8) | Satisfactorio (6) | Insuficiente (3-4) | No realizado (0) |
|----------|----------------|-----------|-------------------|-------------------|------------------|
| Scatter PC1 vs PC2 (Department) | Gráfico correcto con departamentos diferenciados, % varianza en ejes | Gráfico correcto sin % varianza | Gráfico funcional, diferenciación parcial | Gráfico incorrecto | No realiza |
| Scatter PC1 vs PC2 (Attrition) | Gráfico adicional coloreado por rotación, análisis de separación | Gráfico correcto pero sin análisis | Gráfico básico | Gráfico incorrecto | No realiza |
| DataFrame de cargas (loadings) | DataFrame correcto con variables como filas, PCs como columnas | Cargas mostradas en formato diferente | Cargas parcialmente correctas | Cargas incorrectas | No realiza |
| Heatmap de cargas | Heatmap con anotaciones, cmap divergente | Heatmap funcional, estética básica | Visualización alternativa de cargas | Visualización incorrecta | No realiza |

### 3.4 Preguntas de análisis (10 puntos)

| Pregunta | Excelente (2.5) | Bueno (2) | Satisfactorio (1.5) | Insuficiente (0.5-1) | No realizado (0) |
|----------|-----------------|-----------|---------------------|---------------------|------------------|
| **1. Número de componentes para 80%** | Respuesta correcta (~3-4 componentes para 80%), justificación con valores | Respuesta correcta, justificación básica | Número cercano, justificación vaga | Número incorrecto | No responde |
| **2. Interpretación PC1** | Identifica variables con mayor peso (Age, TotalWorkingYears, YearsAtCompany), interpreta como "experiencia/antigüedad" | Identifica variables correctamente, interpretación básica | Identificación parcial | Identificación incorrecta | No responde |
| **3. Separación Attrition en PCA** | Analiza si hay separación visible, discute implicaciones para predicción de rotación | Observación correcta, explicación básica | Observación parcial | Análisis incorrecto | No responde |
| **4. Importancia estandarización** | Explica escala diferente de variables, dominio de MonthlyIncome (miles vs decenas) | Explicación correcta pero incompleta | Mención básica de escalas | Respuesta incorrecta | No responde |

---

## Ejercicio Bonus (10 puntos extra)

| Criterio | Excelente (10) | Bueno (7-8) | Satisfactorio (4-6) | Insuficiente (1-3) | No realizado (0) |
|----------|----------------|-------------|---------------------|-------------------|------------------|
| Biplot completo | Observaciones + vectores de carga escalados + etiquetas de variables | Gráfico funcional, algunos elementos faltantes | Solo observaciones o solo vectores | Intento con errores múltiples | No realiza |

---

## Criterios Generales de Evaluación

### Calidad del código
- **Código limpio y legible:** Variables con nombres descriptivos
- **Comentarios:** Código comentado cuando es necesario
- **Eficiencia:** Uso apropiado de funciones de pandas/numpy

### Ejecución
- **Sin errores:** El notebook se ejecuta completamente sin errores
- **Orden:** Las celdas se ejecutan en el orden correcto

---

## Escala de Calificación

| Rango de puntos | Calificación |
|-----------------|--------------|
| 95-100 (+bonus) | 5.0 |
| 85-94 | 4.5 |
| 75-84 | 4.0 |
| 65-74 | 3.5 |
| 55-64 | 3.0 |
| 45-54 | 2.5 |
| 35-44 | 2.0 |
| < 35 | 1.0-1.9 |


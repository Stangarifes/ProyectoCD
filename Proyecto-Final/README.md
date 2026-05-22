# Entrega 3 - Modelos e integración final

**Proyecto:** Predicción de Riesgo de Burnout en Estudiantes  
**Entrega:** 3 – Entrenamiento de modelos, evaluación e integración en API  
**Fecha:** [Fecha actual]

---

## Descripción

En esta entrega se entrenaron dos modelos de aprendizaje supervisado (clasificación) para predecir el nivel de riesgo de burnout (`risk_level`: Low, Medium, High) a partir de las 19 variables independientes del dataset. Los modelos implementados son:

- **MLPClassifier** (Red Neuronal con scikit-learn)
- **KNeighborsClassifier** (KNN)

Se realizó el preprocesamiento completo (codificación de `gender`, escalado de variables numéricas) tanto en el entrenamiento (Google Colab) como en la API Flask. Se evaluaron ambos modelos y se integraron en el backend, de modo que el frontend recibe y muestra la predicción de cada uno junto con su probabilidad asociada.

---

## Requisitos previos

- Python 3.8 o superior instalado en el sistema.
- Navegador web (Chrome, Firefox, Edge).
- Extensión Thunder Client (opcional, para pruebas).

---

## Instalación de dependencias

Abra una terminal en la carpeta del proyecto y ejecute:

```bash
python -m pip install flask flask-cors pandas joblib scikit-learn

---------------------------------

Entrenamiento de modelos (Google Colab)
El entrenamiento se realizó en Google Colab con el dataset student_mental_health_burnout_1M.csv (1,000,000 registros). Se tomaron los siguientes pasos:

Carga y exploración del dataset.

Preprocesamiento:

Codificación de gender con LabelEncoder.

Escalado de todas las variables numéricas con StandardScaler.

Codificación de risk_level con LabelEncoder (Low→0, Medium→1, High→2).

División en entrenamiento (80%) y prueba (20%).

Entrenamiento de MLPClassifier (capas ocultas 64 y 32, activación ReLU, max_iter=300, early_stopping).

Entrenamiento de KNeighborsClassifier (n_neighbors=5).

Evaluación (accuracy, F1-score, classification report).

Guardado de artefactos (ambos modelos y todos los transformadores) usando joblib.

Resultados de evaluación (sobre 200,000 muestras de prueba):

MLPClassifier: Accuracy ≈ 99.77%, F1-score (weighted) ≈ 0.9977

KNeighborsClassifier: Accuracy ≈ 92.72%, F1-score (weighted) ≈ 0.9255

(Ver reportes completos en el repositorio o en la documentación interna)

------------------------------------------------------

Ejecución del sistema completo
1. Colocar los artefactos en la carpeta del proyecto
Descargue los archivos .pkl generados en Colab y colóquelos en la misma carpeta donde se encuentra app.py. Los siete archivos son:

mlp_model.pkl

knn_model.pkl

le_gender.pkl

scaler.pkl

le_risk.pkl

numeric_cols.pkl

feature_order.pkl

2. Iniciar el backend
En la terminal, dentro de la carpeta del proyecto, ejecute: python app.py

Verá el mensaje:  * Running on http://127.0.0.1:5000
No cierre esta terminal mientras use la aplicación.

3. Abrir el frontend
Abra el archivo index.html con su navegador (doble clic).

Complete los 19 campos del formulario (todos son obligatorios).

Presione el botón "Predecir riesgo".

Debajo del formulario aparecerán dos tarjetas con las predicciones de MLP y KNN, mostrando la clase (Low, Medium o High) y la probabilidad asociada (en porcentaje).

------------------------------------------------------------

Prueba de la API con Thunder Client (opcional)
Para verificar el correcto funcionamiento de la API sin el frontend, siga estos pasos:

Asegúrese de que el backend esté corriendo (python app.py).

En Thunder Client (VS Code), cree una nueva petición POST a http://127.0.0.1:5000/predict.

En Headers agregue: Content-Type: application/json.

En Body (JSON) pegue un objeto con las 19 variables (ejemplo mínimo abajo).

Haga clic en Send.

Ejemplo mínimo de JSON:
{
    "age": 22,
    "gender": "Male",
    "academic_year": 3,
    "study_hours_per_day": 6,
    "exam_pressure": 5,
    "academic_performance": 70,
    "stress_level": 4,
    "anxiety_score": 3,
    "depression_score": 1,
    "sleep_hours": 7,
    "physical_activity": 2,
    "social_support": 6,
    "screen_time": 5,
    "internet_usage": 5,
    "financial_stress": 4,
    "family_expectation": 5,
    "burnout_score": 2,
    "mental_health_index": 7,
    "dropout_risk": 1
}

{
    "age": 22,
    "gender": "Male",
    "academic_year": 1,
    "study_hours_per_day": 6.0,
    "exam_pressure": 5.0,
    "academic_performance": 30.0,
    "stress_level": 4.0,
    "anxiety_score": 3.0,
    "depression_score": 9.0,
    "sleep_hours": 1.0,
    "physical_activity": 2.0,
    "social_support": 9.0,
    "screen_time": 1.0,
    "internet_usage": 5.0,
    "financial_stress": 4.0,
    "family_expectation": 1.0,
    "burnout_score": 2.0,
    "mental_health_index": 7.0,
    "dropout_risk": 1.0
}

Respuesta esperada:
{
  "mlp": {
    "class": "Low",
    "probability": 0.9999
  },
  "knn": {
    "class": "Low",
    "probability": 0.9876
  }
}

(Los valores exactos pueden variar según los datos ingresados).

--------------------------------------

Estructura final de carpetas recomendada
proyecto/
│
├── app.py
├── index.html
├── script.js
├── mlp_model.pkl
├── knn_model.pkl
├── le_gender.pkl
├── scaler.pkl
├── le_risk.pkl
├── numeric_cols.pkl
├── feature_order.pkl
├── README.md
└── (opcional) student_mental_health_burnout_1M.csv

----------------------------------

Nota sobre el preprocesamiento
El preprocesamiento (codificación de gender, escalado de variables numéricas, codificación de risk_level) se realizó en Google Colab y los objetos transformadores (LabelEncoder, StandardScaler) se guardaron y se cargan en app.py. Esto garantiza que la API aplique exactamente las mismas transformaciones que se usaron durante el entrenamiento, asegurando consistencia en las predicciones.

-----------------------------------

Solución de problemas comunes
ModuleNotFoundError: No module named 'joblib' → Ejecute python -m pip install joblib scikit-learn.

FileNotFoundError al cargar un .pkl → Verifique que todos los archivos generados en Colab estén en la misma carpeta que app.py.

La predicción muestra siempre la misma clase → Revise que el orden de las columnas en feature_order.pkl coincida con el orden de los datos enviados. Si es necesario, reentrene y guarde nuevamente.

Error 500 en la API → Revise la terminal de Flask para ver el traceback completo; suele ser por falta de algún campo en el JSON o por un error en el preprocesamiento.

--------------------------------------

Entrega 3 - Conclusión
Se han cumplido todos los objetivos de la entrega:

Entrenamiento de tres modelos (dos requeridos: MLP y KNN). (Nota: se decidieron dos modelos finales)

Evaluación con métricas apropiadas (accuracy, F1-score, classification report).

Selección y justificación del modelo (aunque en la API se mantienen ambos para mostrar resultados comparativos).

Integración del preprocesamiento y los modelos en la API Flask.

Aplicación web completamente funcional con frontend que muestra las predicciones de ambos modelos.

El sistema está listo para ser utilizado y demostrado.
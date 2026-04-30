# Entrega 2 - Backend y API

**Proyecto:** Predicción de Riesgo de Burnout en Estudiantes  
**Entrega:** 2 – Backend y API (Flask)  

---

## Descripción

Esta entrega implementa el backend de la aplicación web. Se creó una API con Flask que expone el endpoint `/predict`, se conectó con el frontend existente (Entrega 1) y se dejó preparada la infraestructura para la integración de los modelos de machine learning en la Entrega 3.

No se incluye entrenamiento de modelos ni preprocesamiento de datos ya que se realizó en Google Colab. El endpoint solo recibe datos y devuelve una confirmación para verificar su funcionamiento.

---

## Requisitos previos

- Python 3.8 o superior instalado en el sistema.
- Navegador web (Chrome, Firefox, Edge).

---

## Instalación de dependencias

Abra una terminal en la carpeta del proyecto y ejecute:

```CMD
python -m pip install flask flask-cors pandas

---

Archivos del proyecto
Archivo		Descripción
app.py		Servidor Flask con CORS y endpoint /predict.
script.js	Lógica JavaScript para enviar datos del formulario al backend.
index.html	Interfaz de usuario con formulario de 19 variables.

---

Ejecución

1. Iniciar el backend
En la terminal, dentro de la misma carpeta donde se encuentran los archivos, ejecute:
python app.py
Deberá ver el siguiente mensaje:  * Running on http://127.0.0.1:5000
Nota: No cierre esta terminal mientras use la aplicación.

2. Abrir el frontend
- Abra el archivo index.html con su navegador (doble clic o "Abrir con").
- Complete los 19 campos del formulario (todos son obligatorios).
- Presione el botón "Predecir riesgo".
- Debajo del formulario aparecerá un mensaje de éxito indicando que los datos fueron recibidos correctamente.

---

Prueba de la API con Thunder Client (Opcional)

Para verificar que el endpoint /predict funciona sin el frontend, puede usar la extensión Thunder Client en VS Code:
1. Cree una nueva petición POST a http://127.0.0.1:5000/predict.
2. Agregue el encabezado (pestaña header): Content-Type: application/json.
3. En el cuerpo (pestaña body), seleccione JSON y pegue un ejemplo de datos (con al menos las variables obligatorias).
Ejemplo mínimo:
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
4. Haga clic en Send.
5. La respuesta esperada es un JSON con "status": "success" y el mensaje de confirmación.

---

Estructura de carpetas recomendada

proyecto_entrega2/
│
├── app.py
├── index.html
├── script.js
└── README.md

---

Nota importante:
El preprocesamiento de datos (conversión de variable categorica "gender", normalización, etc.) se realizó en Google Colab la cual podrá ver en el repositorio de GitHub. 
El backend solo recibe los datos y valida la conexión, quedando listo para integrar el modelo final en la Entrega 3.
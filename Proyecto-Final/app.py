# Importamos las librerías necesarias
from flask import Flask, request, jsonify   # Framework web, manejo de peticiones y respuestas JSON
from flask_cors import CORS                 # Permite que el frontend (HTML) pueda comunicarse con la API
import pandas as pd                         # Se usará para manejar los datos
import joblib
import numpy as np

# Crear la aplicación Flask
app = Flask(__name__)

# Habilitar CORS para todas las rutas (permite peticiones desde cualquier origen, como el frontend local)
CORS(app)

# Cargar artefactos
mlp = joblib.load('mlp_model.pkl')
knn = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')
le_gender = joblib.load('le_gender.pkl')
le_risk = joblib.load('le_risk.pkl')
numeric_cols = joblib.load('numeric_cols.pkl')
feature_order = joblib.load('feature_order.pkl')

# Mapeo de clases (para mostrar texto)
CLASSES = le_risk.classes_.tolist()  # ['High', 'Low', 'Medium'] según el orden

# Endpoint principal para recibir datos del formulario y responder con confirmación
@app.route("/predict", methods=['POST'])
def predict():
    """
    Recibe los datos del estudiante en formato JSON, los procesa, 
    y devuelve un mensaje de éxito junto con los datos recibidos para verificar su conexión con la API.
    En la Entrega 3 se integrará el modelo entrenado.
    """
    try:
        # Recibir datos del frontend
        data = request.get_json()
        # Convertir a DataFrame de una fila (para manejar columnas)
        input_df = pd.DataFrame([data])
        
        # Preprocesar igual que en entrenamiento
        # 1. Codificar género
        input_df['gender'] = le_gender.transform(input_df['gender'])
        
        # 2. Escalar columnas numéricas
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])
        
        # 3. Reordenar columnas según feature_order
        input_df = input_df[feature_order]
        
        # Convertir a array numpy (para el modelo)
        X = input_df.to_numpy()
        
        # Predicciones con MLP
        pred_mlp = mlp.predict(X)[0]
        proba_mlp = mlp.predict_proba(X)[0]
        clase_mlp = CLASSES[pred_mlp]
        proba_max_mlp = round(float(max(proba_mlp)), 4)
        
        # Predicciones con KNN
        pred_knn = knn.predict(X)[0]
        proba_knn = knn.predict_proba(X)[0]
        clase_knn = CLASSES[pred_knn]
        proba_max_knn = round(float(max(proba_knn)), 4)
        
        return jsonify({
            'mlp': {
                'class': clase_mlp,
                'probability': proba_max_mlp
            },
            'knn': {
                'class': clase_knn,
                'probability': proba_max_knn
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
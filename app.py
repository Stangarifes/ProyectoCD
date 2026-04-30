# Importamos las librerías necesarias
from flask import Flask, request, jsonify   # Framework web, manejo de peticiones y respuestas JSON
from flask_cors import CORS                 # Permite que el frontend (HTML) pueda comunicarse con la API
import pandas as pd                         # Se usará para manejar los datos

# Crear la aplicación Flask
app = Flask(__name__)

# Habilitar CORS para todas las rutas (permite peticiones desde cualquier origen, como el frontend local)
CORS(app)

# Endpoint principal para recibir datos del formulario y responder con confirmación
@app.route("/predict", methods=['POST'])
def predict():
    """
    Recibe los datos del estudiante en formato JSON, los procesa, 
    y devuelve un mensaje de éxito junto con los datos recibidos para verificar su conexión con la API.
    En la Entrega 3 se integrará el modelo entrenado.
    """
    try:
        # Obtener los datos enviados por el frontend (formato JSON)
        datos_json = request.get_json()

        # Verificar que se recibieron datos
        if not datos_json:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Opcional: Convertir a DataFrame de pandas para validar estructura más adelante
        # Esto será útil en la Entrega 3 cuando se necesite preprocesar y pasar al modelo que se vaya a implementar.
        # Aquí solo se hace para demostrar que se importa correctamente.
        df = pd.DataFrame([datos_json])

        # Por ahora, simplemente se devuelve un mensaje de éxito junto con los datos recibidos
        # (así el frontend puede confirmar que la comunicación funciona)
        return jsonify({
            "status": "success",
            "mensaje": "Datos recibidos correctamente. Todo listo para la integración del modelo en la Entrega 3.",
            "datos_recibidos": datos_json   # Opcional: eco de los datos para depuración
        }), 200

    except Exception as e:
        # Capturar cualquier error inesperado y devolverlo como respuesta de error
        return jsonify({"error": str(e)}), 500

# Punto de entrada para ejecutar el servidor
if __name__ == "__main__":
    # Ejecutar la aplicación en modo debug (recarga automática y mensajes detallados)
    # El servidor correrá en http://127.0.0.1:5000
    app.run(debug=True, host='0.0.0.0', port=5000)
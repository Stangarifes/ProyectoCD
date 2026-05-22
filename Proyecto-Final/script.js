// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formularioPrediccion');
    const resultadoDiv = document.getElementById('resultadoArea');

    formulario.addEventListener('submit', async function(event) {
        event.preventDefault(); // Evita recargar la página

        // Recoger todos los datos del formulario
        const datos = {};
        const campos = formulario.querySelectorAll('input, select');
        campos.forEach(campo => {
            datos[campo.name] = campo.value;
        });

        // Mostrar mensaje de carga
        resultadoDiv.style.display = 'block';
        resultadoDiv.innerHTML = '<div class="alert alert-info">Enviando datos al servidor, espere...</div>';

        try {
            const respuesta = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datos)
            });

            if (!respuesta.ok) {
                const errorData = await respuesta.json();
                throw new Error(errorData.error || 'Error en la petición');
            }

            const resultado = await respuesta.json();

            // Construir HTML para mostrar ambas predicciones
            let html = `
                <div class="card mb-2">
                    <div class="card-header bg-primary text-white">
                        <strong>Predicciones</strong>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="card bg-light">
                                    <div class="card-body">
                                        <h5 class="card-title">Red Neuronal (MLP)</h5>
                                        <p class="card-text">
                                            <strong>Clase:</strong> ${resultado.mlp.class}<br>
                                            <strong>Probabilidad:</strong> ${(resultado.mlp.probability * 100).toFixed(2)}%
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="card bg-light">
                                    <div class="card-body">
                                        <h5 class="card-title">KNN</h5>
                                        <p class="card-text">
                                            <strong>Clase:</strong> ${resultado.knn.class}<br>
                                            <strong>Probabilidad:</strong> ${(resultado.knn.probability * 100).toFixed(2)}%
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            resultadoDiv.innerHTML = html;
        } catch (error) {
            resultadoDiv.innerHTML = `<div class="alert alert-danger">❌ Error: ${error.message}. Asegúrate de que el backend Flask esté corriendo en http://127.0.0.1:5000</div>`;
        }
    });
});
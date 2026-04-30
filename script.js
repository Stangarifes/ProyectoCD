// Espera a que todo el contenido HTML esté cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function() {

    // Obtener el formulario por su ID
    const formulario = document.getElementById('formularioPrediccion');

    // Obtener el div donde se mostrará el resultado
    const resultadoDiv = document.getElementById('resultadoArea');

    // Escuchar el evento 'submit' del formulario (cuando se presiona el botón)
    formulario.addEventListener('submit', async function(event) {
        // Prevenir el comportamiento por defecto (recargar la página)
        event.preventDefault();

        // Crear un objeto vacío para almacenar los datos del formulario
        const datos = {};

        // Seleccionar todos los campos de entrada (input y select) dentro del formulario
        const campos = formulario.querySelectorAll('input, select');

        // Recorrer cada campo y guardar su valor en el objeto 'datos'
        // El atributo 'name' de cada campo se usa como clave
        campos.forEach(campo => {
            datos[campo.name] = campo.value;
        });

        // Mostrar mensaje de "cargando" en el área de resultado
        resultadoDiv.style.display = 'block';
        resultadoDiv.innerHTML = '<div class="alert alert-info">Enviando datos al servidor, espere...</div>';
        resultadoDiv.className = 'mt-4';

        try {
            // Realizar la petición POST al backend Flask
            // La URL debe coincidir con la del servidor (puerto 5000 por defecto)
            const respuesta = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',          // Método HTTP
                headers: {
                    'Content-Type': 'application/json'   // Indicamos que enviamos JSON
                },
                body: JSON.stringify(datos)  // Convertir el objeto a JSON
            });

            // Si la respuesta no es correcta (código diferente de 200)
            if (!respuesta.ok) {
                // Intentar obtener el mensaje de error del backend
                const errorData = await respuesta.json();
                throw new Error(errorData.error || 'Error en la petición');
            }

            // Convertir la respuesta a JSON
            const resultado = await respuesta.json();

            // Mostrar el mensaje de éxito devuelto por el backend
            resultadoDiv.innerHTML = `<div class="alert alert-success"> ${resultado.mensaje}</div>`;

        } catch (error) {
            // En caso de error (red, servidor caído, etc.)
            resultadoDiv.innerHTML = `<div class="alert alert-danger"> Error: ${error.message}. Asegúrate de que el backend Flask esté corriendo en http://127.0.0.1:5000</div>`;
        }
    });
});
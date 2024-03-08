from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Endpoint de la API de la NASA APOD (Astronomy Picture of the Day)
api_url = "https://api.nasa.gov/planetary/apod"
api_key = "tu_api_key"  # Reemplaza con tu propia API key de la NASA

# Ruta principal que muestra la imagen astronómica del día
@app.route('/')
def index():
    # Parámetros de la solicitud a la API
    params = {
        'api_key': api_key
    }

    # Hacer una solicitud a la API de la NASA APOD
    response = requests.get(api_url, params=params)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()

        # Renderizar la plantilla HTML con la información de la imagen astronómica
        return render_template('index.html', data=data)
    else:
        return f"Error al hacer la solicitud a la API de la NASA. Código de estado: 
        {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)

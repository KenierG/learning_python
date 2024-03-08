from flask import Flask, render_template
import requests

app = Flask(__name__)

api_url = "https://api.nasa.gov/planetary/apod"
api_key = "t5u4Rmymd0b3wdNbAQ3QszcXhEVlBbd6pvFyUXRo"

@app.route('/')

def index():
    params = {
        'api_key': api_key
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        return render_template('index.html', data=data)
    else:
        #return "Error {response.status_code}"
        print("Error")
    
    if __name__ == '__main__':
        app.run(debug=True)
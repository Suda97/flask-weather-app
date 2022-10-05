from flask import Flask, render_template, request
import requests

app = Flask(__name__)

if __name__ == '__main__':
   app.run(host='0.0.0.0')

@app.route('/')
def index():
    r = request.get(url='https://api.open-meteo.com/v1/forecast?latitude=50.08&longitude=19.98&current_weather=true')
    data = r.json()
    print(data)
    return 'Hello World!'
from flask import Flask,render_template,request
from dotenv import load_dotenv
import requests
import os

#load api key
load_dotenv()
api_key = os.getenv("TOKEN")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather',methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    if response.get('cod') != 200:
        return render_template('index.html',error='City Not Found')

    weather_data = {
        'city':city,
        'temperature':response['main']['temp'],
        'description':response['weather'][0]['description'],
        'humidity':response['main']['humidity'],
        'wind_speed':response['wind']['speed'],
        'icon':response['weather'][0]['icon']
    }
    return render_template('result.html',weather=weather_data)
if __name__ == '__main__':
    app.run(debug=True)    

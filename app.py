from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "debd882a8f7c007b5be2287e9c1034f4"

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'country': data['sys']['country']
            }
        else:
            weather_data = {'error': 'City not found 😢'}
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

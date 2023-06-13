import os
import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__ ,template_folder='template')

#api
app_id = 'APY_KEY'
url = '7118bdd38f8f7fd52ecf716e503df7f6'
# http://api.openweathermap.org/data/2.5/weather

#view
@app.route('/', methods=['GET', 'POST'])
def weather():
    error = None
    if request.method == 'POST':
        city = request.form['city']
        url_final = url + '?appid=' + app_id + '&q='+city
        response = requests.get(url_final).json()
        if response['cod'] == 200:  
            description = response['weather'][0]['description']
            temperature = response['main']['temp']
            feels_like = response['main']['feels_like']
            min_temp = response['main']['temp_min']
            max_temp = response['main']['temp_max']
            pressure = response['main']['pressure']
            humidity = response['main']['humidity']
            return render_template('index.html', description=description, temperature=temperature, feels_like=feels_like, min_temp=min_temp, max_temp=max_temp, pressure=pressure, humidity=humidity)
        else:
            error = "City not found"
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
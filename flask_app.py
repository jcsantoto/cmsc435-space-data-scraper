from flask import Flask, render_template
from solar_weather_plotter import SolarWeatherPlotter

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/temperature")
def temperature():
    temperature = SolarWeatherPlotter._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "temperature")
    time =  SolarWeatherPlotter._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json","time_tag")
    return render_template("test.html",data1=temperature, data2=time)

if __name__ == "__main__":
    app.run(debug=True)
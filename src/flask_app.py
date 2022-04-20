from flask import Flask, render_template
from src.solar_weather_fetcher import SolarWeatherFetcher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/temperature")
def temperature():
    temperature = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "temperature")
    time =  SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json","time_tag")
    return render_template("test.html",data1=temperature, data2=time)

@app.route("/density")
def density():
    density = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "density")
    time =  SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json","time_tag")
    return render_template("test.html",data1=density, data2=time)

@app.route("/speed")
def speed():
    speed = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "speed")
    time =  SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json","time_tag")
    return render_template("test.html",data1=speed, data2=time)

if __name__ == "__main__":
    app.run(debug=True)

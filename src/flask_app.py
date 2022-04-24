from flask import Flask, render_template
from src.solar_weather_fetcher import SolarWeatherFetcher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")

#@app.errorhandler(Exception)
#def error_handler(error):
#    return ("<h1> That page does not exist. </h1>")

@app.route("/wind")
def solar_wind():
    return render_template("graphs.html")

@app.route("/wind/<data>")
def solar_wind_graphs(data):
    if(data == "all"):
        temperature = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "temperature")
        density = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "density")
        speed = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "speed")
        time = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json", "time_tag")
        return render_template("activities.html", temperature=temperature, density=density, speed=speed, time=time)
    else:
        data1 = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", data)
        time = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "time_tag")
        return render_template("test.html", data1=data1, data2=time)

if __name__ == "__main__":
    app.run(debug=True)

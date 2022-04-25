from flask import Flask, render_template
from src.solar_weather_fetcher import SolarWeatherFetcher
from src.solar_flare_fetcher import SolarFlareFetcherSWL
from src.solar_flare_fetcher import SolarFlareFetcherNOAA
from src.alerts_backend import Alerts

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html")

#@app.errorhandler(Exception)
#def error_handler(error):
#    return ("<h1> That page does not exist. </h1>")

@app.route("/wind")
def solar_wind():
    return render_template("graph.html")

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

        if data == 'temperature':
            axis = 'Temperature (K)'
        elif data == 'density':
            axis = 'Density (1/cm^3)'
        elif data == 'speed':
            axis = 'Speed (km/s)'

        return render_template("test.html", data1=data1, data2=time, data3=axis)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/solarflare")
def solar_flare():
    swl_data = SolarFlareFetcherSWL.fetch_website_data()
    noaa_data = SolarFlareFetcherNOAA.fetch_website_data()
    return render_template("solar_flare.html", data1=swl_data[0], data2=swl_data[1], data3=swl_data[2], data4=noaa_data[0],
                           data5=swl_data[1], data6=noaa_data[2], data7=noaa_data[3])


@app.route("/feed/<selection>")
def feed(selection):
    al = Alerts()
    temperature = False
    speed = False
    density = False

    selection = int(selection)

    if selection & 1 == 1:
        temperature = True
    if (selection >> 1) & 1 == 1:
        speed = True
    if (selection >> 2) & 1 == 1:
        density = True

    al.customize_alerts(density, speed, temperature)
    response = al.get_custom_alert()

    return render_template("feed.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

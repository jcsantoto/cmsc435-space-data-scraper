import datetime
import string
from solar_weather_fetcher import SolarWeatherFetcher


class Alerts:

    def __init__(self):
        pass

    @staticmethod
    def get_alert():

        current_data = SolarWeatherFetcher.fetch_website_data()[-1]
        solar_density = current_data[1]
        solar_wind = current_data[2]
        solar_temperature = current_data[3]

        current_time = datetime.datetime.strptime(current_data[0], "%Y-%m-%d %H:%M:%S.%f")
        current_year = current_time.year
        current_month = current_time.strftime("%B")
        current_day = current_time.day
        current_hour = int(current_time.hour)
        current_minute = current_time.minute
        am_or_pm = " am"

        if current_hour == 0:
            current_hour = 12
        elif current_hour >= 12:
            am_or_pm = " pm"

        return_string = "As of " + str(current_month) + " " + str(current_day) + ", " + str(current_year) + " at "
        return_string = return_string + str(current_hour) + ":" + str(current_minute) + " " + am_or_pm
        return_string = return_string + " Greenwich Mean Time, the current weather in space is:" + '\n'
        return_string = return_string + "Solar Wind Density: " + solar_density + " (1/cm^3)" + '\n'
        return_string = return_string + "Solar Wind Speed: " + solar_wind + " (km/s)" + '\n'
        return_string = return_string + "Solar Wind Temperature: " + solar_temperature + " (K)" + '\n'

        return return_string

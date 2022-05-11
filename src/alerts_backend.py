import datetime
import string
from src.solar_weather_fetcher import SolarWeatherFetcher


class Alerts:

    def __init__(self):
        self.density = True
        self.wind = True
        self.temperature = True
        self.sunspot = True
        self.density_threshold = 0
        self.wind_threshold = 0
        self.temperature_threshold = 0

    def customize_alerts(self, custom_density, custom_wind, custom_temperature, custom_sunspot):
        """ Allows user to customize alerts to show various weather attributes
                Args:
                    custom_density: user input to show or not show density
                    custom_wind: user input to show or not show wind
                    custom_temperature: user input to show or not show temperature
                    custom_sunspot: user input to show or not show sunspot
        """
        self.density = custom_density
        self.wind = custom_wind
        self.temperature = custom_temperature
        self.sunspot = custom_sunspot

    def customize_thresholds(self, custom_density, custom_wind, custom_temperature):
        """ Allows user to customize thresholds to show various weather attributes
                    Args:
                        custom_density: user input for density threshold
                        custom_wind: user input for wind threshold
                        custom_temperature: user input for temperature threshold
        """
        self.density_threshold = custom_density
        self.wind_threshold = custom_wind
        self.temperature_threshold = custom_temperature

    def get_custom_alert(self):
        """
        Shows general information about solar weather which is based off the user's custom settings on what to show
        """

        current_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json")[-1]
        solar_density = current_data[1]
        solar_wind = current_data[2]
        solar_temperature = current_data[3]

        sunspot_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/json/sunspot_report.json")
        total_sunspot = sunspot_data[0]["Numspot"] + sunspot_data[1]["Numspot"] + sunspot_data[3]["Numspot"]

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

        if len(str(current_minute)) == 1:
            current_minute = "0" + str(current_minute)

        return_string = "As of " + str(current_month) + " " + str(current_day) + ", " + str(current_year) + " at "
        return_string = return_string + str(current_hour) + ":" + str(current_minute) + " " + am_or_pm
        return_string = return_string + " Greenwich Mean Time, the current weather in space is:" + '<br>'
        if self.density:
            return_string = return_string + "Solar Wind Density: " + solar_density + " (1/cm^3)" + '<br>'
        if self.wind:
            return_string = return_string + "Solar Wind Speed: " + solar_wind + " (km/s)" + '<br>'
        if self.temperature:
            return_string = return_string + "Solar Wind Temperature: " + solar_temperature + " (K)" + '<br>'
        if self.sunspot:
            return_string = return_string + "Sunspot Number: " + str(total_sunspot) + '<br>'

        return return_string


    @staticmethod
    def get_alert():
        """
            Obsolete method
        """
        current_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json")[-1]
        solar_density = current_data[1]
        solar_wind = current_data[2]
        solar_temperature = current_data[3]

        sunspot_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/json/sunspot_report.json")
        total_sunspot = sunspot_data[0]["Numspot"] + sunspot_data[1]["Numspot"] + sunspot_data[3]["Numspot"]

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
        return_string = return_string + "Sunspot Number: " + str(total_sunspot) + ' \n'

        return return_string


    def get_threshold_alert(self):
        """
            Shows information about solar weather which is based off the user's custom threshold settings
        """

        current_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json")[-1]
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

        if len(str(current_minute)) == 1:
            current_minute = "0" + str(current_minute)

        return_string = ""

        if float(solar_density) >= self.density_threshold:
            return_string = return_string + "Solar Wind Density is at " + solar_density + " (1/cm^3)" + '<br>'
        if float(solar_wind) >= self.wind_threshold:
            return_string = return_string + "Solar Wind Speed: " + solar_wind + " (km/s)" + '<br>'
        if float(solar_temperature) >= self.temperature_threshold:
            return_string = return_string + "Solar Wind Temperature: " + solar_temperature + " (K)" + '<br>'

        if return_string.__eq__(""):
            return_string = "Hooray! No alerts to display."
        else:
            return_string = "ALERT! The following values have exceeded the thresholds at: " + str(current_hour) + ":" \
                            + str(current_minute) + " " + am_or_pm + " <br> " + return_string

        return_string = "Your current thresholds: <br>" + "Solar Wind Density: " + str(
            self.density_threshold) + "<br>" + \
                        "Solar Wind Speed:" + str(self.wind_threshold) + "<br> Solar Wind Temperature: " + str(
            self.temperature_threshold) \
                        + "<br><br>" + return_string

        return return_string

    @staticmethod
    def get_warning():
        """
            Shows information about dangerous solar weather conditions if thresholds are met
        """

        current_data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-1-day.json")[-1]
        solar_density = current_data[1]
        solar_wind = current_data[2]
        solar_temperature = current_data[3]

        return_string = ""
        if float(solar_density) >= 20:
            return_string = "Solar Wind Density is currently at " + solar_density + "(1/cm^3), which can cause a geomagnetic storm."
        if float(solar_wind) >= 550:
            return_string = "Solar Wind Speed is currently at " + solar_wind + "(km/s), which can cause a satelitte to go out of orbit."
        if float(solar_temperature) >= 1000000:
            return_string = "Solar Wind Temperature is currently at " + solar_temperature + "(K), which may affect satelitte functionality."
        if return_string.__eq__(""):
            return_string = "Solar Weather conditions are safe for satelittes!"

        return return_string

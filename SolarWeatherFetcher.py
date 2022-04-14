import requests
import string
from bs4 import BeautifulSoup
import ast


class SolarWeatherFetcher:
    """ Class for fetching the solar weather data that comes from the NOAA website.
    """

    @staticmethod
    def fetch_website_data(url: string) -> list:
        """ Requests the HTML content from the NOAA website containing the data for solar weather in the last 24 hours
        Args:
            url: the url that we want to fetch
        Returns:
            lst: a list of each minute of solar weather data (time, density, speed, temperature) for the last 24 hours
        """
        website = requests.get(url)
        content = str(BeautifulSoup(website.content, 'html.parser'))
        lst = ast.literal_eval(content)

        return lst

    @staticmethod
    def format_website_data() -> string:
        """ Gets the list of solar weather data from the NOAA website and converts it into a more readable string

        Returns:
            formatted_str: string containing the data formatted in a readable way
        """

        content = SolarWeatherFetcher.fetch_website_data("")
        content[0][1] = 'density (1/cm^3)'
        content[0][2] = 'speed (km/s)'
        content[0][3] = 'temperature (K)'

        formatted_str = ""

        for data in content:
            formatted_str = formatted_str + '\n' + str(data)

        return formatted_str

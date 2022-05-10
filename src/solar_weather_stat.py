from src.solar_weather_fetcher import SolarWeatherFetcher
import numpy as np
from sklearn.linear_model import LinearRegression

class SolarWeatherStat:
    """ Class for performing stat operations on solar weather data..
    """
    def __init__(self, url: str):
        self.url = url

    def get_min(self, col: str) -> int:
        """ Retrieves data and return minimum value
            Args:
                col: The column name of the column of data that is to be used.
            Returns:
                int: minimum value of list
        """
        data = SolarWeatherFetcher._get_solar_wind_data(self.url, col)
        return min(data)

    def get_max(self, col: str) -> int:
        """ Retrieves data and return maximum value
            Args:
                col: The column name of the column of data that is to be used.
            Returns:
                int: maximum value of list
        """
        data = SolarWeatherFetcher._get_solar_wind_data(self.url, col)
        return max(data)

    def get_average(self, col: str) -> int:
        """ Retrieves data and return average value
            Args:
                col: The column name of the column of data that is to be used.
            Returns:
                int: average value of list
        """
        data = SolarWeatherFetcher._get_solar_wind_data(self.url, col)
        return round(sum(data)/len(data), 2)

    def linear_regression_slope(self, col: str) -> int:
        """ Retrieves data, performs linear regression, returns the slope of the line
            Args:
                col: The column name of the column of data that is to be used.
            Returns:
                int: slope of linear regression on data
        """
        data = SolarWeatherFetcher._get_solar_wind_data(self.url, col)
        length = len(data)
        y = np.array(data)
        x = np.array(list(range(length))).reshape((-1, 1))

        model = LinearRegression()
        model.fit(x, y)
        slope = round(model.coef_[0], 4)

        return slope

    def get_all(self, col: str) -> list:
        return [self.get_min(col), self.get_max(col), self.get_average(col), self.linear_regression_slope(col)]


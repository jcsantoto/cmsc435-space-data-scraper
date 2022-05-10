import src.solar_weather_stat
import unittest

class TestSolarFlareFetcher(unittest.TestCase):
    """ Class to contain unit tests for methods in the SolarWeatherStat class. """

    def test_get_min_returns_minimum_value(self):
        data = [55, 22,  33,  77,  99,  100, 50 , 52]
        min_ = solar_weather_stat.get_min(data)
        self.assertTrue(min_ == 22)

    def test_get_min_rounds_to_two_decimal_places(self):
        data = [55.654, 22.2341, 33.4324, 77.777, 99.123, 100.654, 50.7563, 52.2344]
        min_ = solar_weather_stat.get_min(data)
        self.assertTrue(min_ == 22.23)

    def test_get_max_returns_maximum_value(self):
        data = [55, 22, 33, 77, 99, 100, 50, 52]
        max_ = solar_weather_stat.get_max(data)
        self.assertTrue(max_ == 100)

    def test_get_max_rounds_to_two_decimal_places(self):
        data = [55.654, 22.2341, 33.4324, 77.777, 99.123, 100.654, 50.7563, 52.2344]
        max_ = solar_weather_stat.get_max(data)
        print(max_)
        self.assertTrue(max_ == 100.65)

    def test_get_average_returns_average_value(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        avg = solar_weather_stat.get_average(data)
        self.assertTrue(avg == 5.50)

    def test_get_average_rounds_to_two_decimal_places(self):
        data = [2, 4, 6, 8, 10, 12, 14, 19]
        avg = solar_weather_stat.get_average(data)
        self.assertTrue(avg == 9.38)

    def test_linear_regression_slope_returns_negative_value_with_decreasing_dataset(self):
        data = [100, 20, 80, 70, 10, 60, 50, 30, 20]
        slope = solar_weather_stat.linear_regression_slope(data)
        self.assertTrue(slope < 0)

    def test_linear_regression_slope_returns_positive_value_with_increasing_dataset(self):
        data = [20, 30, 0 ,50, 70, 100, 10, 90, 110]
        slope = solar_weather_stat.linear_regression_slope(data)
        self.assertTrue(slope >= 0)

    def test_linear_regression_slope_rounds_to_four_decimals(self):
        data = [55.654, 22.2341, 33.4324, 77.777, 99.123, 100.654, 50.7563, 52.2344]
        slope = str(solar_weather_stat.linear_regression_slope(data))
        decimal = slope.split('.')[1]
        self.assertTrue(len(decimal) <= 4)



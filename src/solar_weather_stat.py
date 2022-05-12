import numpy as np
from sklearn.linear_model import LinearRegression


def get_min(data: list) -> int:
    """ Retrieves data and return minimum value
        Args:
            data: A list of the data to be operated on
        Returns:
            int: minimum value of list
    """
    return round(min(data), 2)


def get_max(data: list) -> int:
    """ Retrieves data and return maximum value
        Args:
            data: A list of the data to be operated on
        Returns:
            int: maximum value of list
    """
    return round(max(data), 2)


def get_average(data: list) -> int:
    """ Retrieves data and return average value
        Args:
            data: A list of the data to be operated on
        Returns:
            int: average value of list
    """
    return round(np.sum(data)/len(data), 2)


def linear_regression_slope(data: list) -> int:
    """ Retrieves data, performs linear regression, returns the slope of the line
        Args:
            data: A list of the data to be operated on
        Returns:
            int: slope of linear regression on data
    """
    length = len(data)
    y = np.array(data)
    x = np.array(list(range(length))).reshape((-1, 1))

    model = LinearRegression()
    model.fit(x, y)
    slope = round(model.coef_[0], 4)

    return slope


def get_all(data: list) -> list:
    return [get_min(data), get_max(data), get_average(data), linear_regression_slope(data)]




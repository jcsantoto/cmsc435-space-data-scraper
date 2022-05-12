[![coverage report](https://cmsc435.garrettvanhoy.com/jsantoto/space-data-scraper/badges/develop/coverage.svg)](https://cmsc435.garrettvanhoy.com/jsantoto/space-data-scraper/-/commits/develop)
[![pipeline status](https://cmsc435.garrettvanhoy.com/jsantoto/space-data-scraper/badges/develop/pipeline.svg)](https://cmsc435.garrettvanhoy.com/jsantoto/space-data-scraper/-/commits/develop)

# space-data-scraper
This is a scraper program that scrapes space data from various sources
such as spaceweatherlive and NOAA. The user can do various things with this data that
is scraped, which includes viewing the raw data and viewing them in graphs.

The repository contains several files which contain the backend and frontend for the scraping of these various 
datasets. The flask_app file is the main program that runs the web application. The web application is how you interact with our program.
# Running the Program
To use our space data scraper you can visit our website <a href = "http://96.255.219.52/">here</a>
<br>
To run the tests: Tests are run in CI/CD pipeline.

# Navigating the Website
First begin by visiting the website listed in the section above. This will take you to the home page.
From there, there are numerous tabs you can visit which are described below:
* Home: Brief overview of website functionality
* Feed: Live updated (updated approximately every minute with the latest available data from NOAA) space weather data is shown here. You must log in to be able to customize the thresholds and data displayed.
* About: Displays general information about the website including sources of the data
* Solar Wind: Displays graphs of solar weather activity along with a 24 hour summary of this activity.
* Solar Flares: Displays information about solar flares
* Register: You can register for an account here
* Login: You can login to your account here
* Help: You can get help for using the website here <br>
<b>TABS BELOW REQUIRE LOGIN</b>
* Account: Update your account information here
* Community: See what other users have posted on the website <br>
* History: See community posts that you have looked at previously

# Developer Documentation
The `docs` folder contains the project's automatically-generated Sphinx documentation. To access the Sphinx documentation,
open on the `index.html` file in a browser. This will open the main page that links to the specific module pages.

### src
- `alerts_backend`: Python module that contains implementation for alerts feed and functions
- `data_fetcher`: Python module that contains implementation for data fetcher functions
- `flask_app`: Python flask app that has the implementation for the web app
- `follow_user`: Python module for that has the implementation for the follow user forms
- `forms`: Python module that contains the implementation of the forms
- `solar_flare_fetcher`: Python module that contains implementation for the solar flare fetcher
- `solar weather fetcher`: Python module that contains the implementation for the weather fetcher
- `solar weather stat`: Python module that contains the implementation for the solar weather stat

### tests
Within the `tests` folder is the following:
- `test_alerts.py`: the Python unit test file that tests all of the functions in alerts
- `test_data_fetcher.py`: the Python unit test file that tests all of the functions in data fetcher module
- `test_graph_weather_fetcher.py`: the Python unit test file that test all of functions in graph weather fetcher module
- `test_solar_flare_fetcher.py`: the Python test unit file that tests all functions in the solar flare fetcher module
- `test_solar_weather_stat.py`: the python test unit file that tests all of the functions in the solar weather stat module

# Group Efforts and Tasks

#### Abhinav: 16%
Added backend code for determining dangerous satellite conditions. Added tab in feed to display these dangerous satellite conditions.
#### Derek: 21%
Designed better page and content layouts. Used BootStrap to make all pages have better styling so that it is easier to look at. Made navigation to pages more intuitive. Added community page.
#### Maurice: 21%
Added login and registration functionality. Created accounts page and added functionality for updating user info. Added code coverage and test coverage badge. Wrote sphinx documentation
#### John: 21%
Scraped sunspot number data and displayed in feed. Created a class to calculate statistics for solar wind activity. 
Used that class to display a 24 hour summary for solar wind. Wrote tests for solar_wind_stat class. Added space weather alert announcements to the top of the feed. Added post history.
#### Johnny: 21%
Added AJAX to the website in order to display live data updates without the page needing to be refreshed. Added feed options for adding
thresholds for solar weather data to display. Integrated feed customization options with user database.
Updated README.


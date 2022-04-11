# space-data-scraper

# Running the Program
To run the program, we provided a Dockerfile which can generate an image in Docker. This will
add all the required libraries and will run the program for you. The following commands are needed:

#### Generating image for the program
docker build -t space-scraper .

#### Available Command Line Arguments for the Program
| Command Option | Description
|---| --- |
| -h, --help | show this help message and exit |
|  -show SHOW |    Enter "Categories" to navigate a list of the available space data categories |
|-get GET      |      Enter "SolarData" to view information about solar weather activity |
|  -download DOWNLOAD | Enter "30daySolar" to download file of 30 day data |
|  -view VIEW    |      Enter "DailySolarFlare" to see daily solar flare activity data |
|  -check CHECK   |     Enter "Feed" to be alerted of changes in the solar wind speed |

#### Running the program (running the image) with examples for all currently available commands
docker run space-scraper -h 

docker run space-scraper --help 

docker run space-scraper -show Categories 

docker run space-scraper -get SolarData 

docker run space-scraper -download 30daySolar 

docker run space-scraper -view DailySolarFlare

docker run space-scraper -check Feed


# Group Efforts and Tasks
#### Abhinav: 20%
Wrote code to alert the user about various solar data such as solar wind speed.
#### Derek: 20%
Wrote code to generate a url and download 30 day solar wind datasets.
#### Maurice: 20%
Wrote the CLI for the program. Recorded and wrote the scrum logs.
#### John: 20%
Scraped information from spaceweatherlive and NOAA for solar flare activity.
#### Johnny: 20% 
Scraped information about solar weather including: solar wind speeds, density, and temperatures. 
Wrote tests for this portion of the program.
Dockerized the program and updated README.


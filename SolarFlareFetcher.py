from bs4 import BeautifulSoup
import requests
import json
import time

class SolarFlareFetcher:
	""" Class for fetching solar flare activity from spaceweatherlive
	"""

	@staticmethod
	def _fetch_website_data() -> list:
		""" Requests the HTML content from the spaceweatherlive website containing the current and highest solar flare 
				classifications for the past 24 and 72 hours.
	
	      Returns:
	      	lst: a list of each minute of solar weather data (time, density, speed, temperature) for the last 24 hours
	  """
	
		URL = "https://www.spaceweatherlive.com/includes/live-data.php?object=solar_flare_3d&lang=EN"
		
		headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", 
			"Accept-Encoding": "gzip, deflate, br"
		}
		
		response = requests.get(URL, headers=headers)
		
		while(response.status_code == 403):
			time.sleep(5)
			response = requests.get(URL, headers=headers)
		
		content = BeautifulSoup(response.content, "html.parser")
		flare_activity_json = json.loads(content.text)
		
		current_flare = flare_activity_json["val"].strip("</div>")
		max_flare_24_hours = flare_activity_json["val24"].strip("</div>")
		max_flare_72_hours = flare_activity_json["val72"].strip("</div>")
	
		return [current_flare, max_flare_24_hours, max_flare_72_hours]
	
		
	@staticmethod
	def _format_website_data() -> str:
		""" Converts the solar flare data from spaceweatherlive into a more readable string

        Returns:
            formatted_str: string containing the data formatted in a readable way
    """

		flare_data = SolarFlareFetcher._fetch_website_data()

		formatted_str = "The current solar flare class is: " + flare_data[0]
		formatted_str = formatted_str + "\n The largest solar flare class in the past 24 hours is: " + flare_data[1]
		formatted_str = formatted_str + "\n The largest solar flare class in the past 72 hours is: " + flare_data[2]
		
		return formatted_str
		

	
		
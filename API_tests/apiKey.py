import requests
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv("APIKEY")
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'q':'Seattle,US', 'appid': SECRET_KEY}
response = requests.get(baseUrl, params=parameters)
print(response.url)
print(response.content)
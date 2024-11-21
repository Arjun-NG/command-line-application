import argparse
import pyfiglet
from simple_chalk import chalk
import requests

# Your OpenWeatherMap API key
API_KEY = "28a186918bb998ca2ab70509997e337f"

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Weather icons dictionary for different weather conditions
WEATHER_ICONS = {
    "01d": "☀️", "02d": "⛅️", "03d": "☁️", "04d": "☁️",
    "09d": "🌧", "10d": "🌦", "11d": "⛈", "13d": "🌨", "50d": "🌫",
    "01n": "🌙", "02n": "☁️", "03n": "☁️", "04n": "☁️",
    "09n": "🌧", "10n": "🌦", "11n": "⛈", "13n": "🌨"
}

# Setting up argparse for country and city arguments
parser = argparse.ArgumentParser(description="Check the weather for a specific city in a country")
parser.add_argument("city", help="The city to check weather for")
parser.add_argument("country", help="The country code (ISO 3166 format, e.g., 'IN' for India)")
args = parser.parse_args()

# Constructing the API request URL with city and country code
url = f"{BASE_URL}?q={args.city},{args.country}&appid={API_KEY}&units=metric"

# Making the API request
response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve the weather information"))
    exit()

# Parsing the JSON data from the response
data = response.json()

# Extracting relevant weather information
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Fetching the corresponding weather icon
weather_icon = WEATHER_ICONS.get(icon, "")

# Formatting the output with ASCII art for the city name only
output = f"{pyfiglet.figlet_format(city)}\n{country}\n\n"
output += f"{weather_icon} {description.capitalize()}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"
output += f"Humidity: {humidity}%\n"

print(chalk.green(output))

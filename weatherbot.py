import datetime as dt
import requests # very popular non-standard library used to send HTTP requests easily
import nltk

# Tomorrow.io API was supposed to fetch data for future days, 
# but testing it warranted server errors that I can't do anything about
url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"
querystring = {"lat":"42.8237618","lon":"-71.2216286","unit_system":"si","fields":"humidity"}
headers = {
    'x-rapidapi-key': "f6e1fa457fmshb41ad21c20aef8cp1f7ec2jsne084f3cee852",
    'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

# followed basic OpenWeatherMap api tutorial by NeuralNine on YouTube
# https://www.youtube.com/watch?v=9P5MY_2i7K8
weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
forecast_base_url = "http://api.openweathermap.org/data/2.5/forecast?"
geocode_base_url = "http://api.openweathermap.org/geo/1.0/direct?"
api_key = "667918a604d22ec3f546c210f65d3842"
city = input("What city do you live in?")


def kelToCel(kel_temp):
    """Converts a temperature value from Kelvin to Celsius"""
    celsius = kel_temp - 273
    return celsius


# URLs below written with guidance on OpenWeatherMap API documentation on their website:
# https://openweathermap.org/api/one-call-3

geocode_url = geocode_base_url + "q=" + city + "&limit=5&appid=" + api_key
geocode_response = requests.get(geocode_url).json()
city_lat = geocode_response[0]['lat']
city_lon = geocode_response[0]['lon']

forecast_url = forecast_base_url + "lat=" + str(city_lat) + "&lon=" + str(
    city_lon) + "&appid=" + api_key + "&units=metric"
forecast_response = requests.get(forecast_url).json()

weather_url = weather_base_url + "appid=" + api_key + "&q=" + city
weather_response = requests.get(weather_url).json()

temp_kel = weather_response['main']['temp']
temp_cel = kelToCel(temp_kel)  # weather API dictionary returns temperatures in Kelvin by default
description = weather_response['weather'][0]['description']
windspeed = weather_response['wind']['speed']

print(f"The temperature in {city} is {temp_cel:.1f}°C.") # returns current temperature in Celsius to one decimal place
if temp_cel < 10:
    print("A bit chilly! Consider wearing a few extra layers.")
elif temp_cel > 20:
    print("It's hot! Be sure to drink plenty of water.")
else:
    print("It seems like a nice temperature! Why don't you go outside for a walk?")
print(f"General weather in {city}: {description}")
print(f"Here's a fun fact: the latitude and longitude coordinates of {city} are {city_lon}, {city_lat}!")
print(f"The current wind speed in {city} is {windspeed} knots.")

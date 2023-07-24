import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv('config.env')
# user_api = os.environ['current_weather_data']
user_api = os.getenv('user_api')
location = input("Enter the city name : ")

# pasted from website : http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London

complete_api_link = "http://api.weatherapi.com/v1/current.json?key=" + str(user_api) +"&q="+str(location)

api_link = requests.get(complete_api_link)
api_data = api_link.json()
# print(api_data)

if api_data['location'] == '404':
    print("Invalid City : {} , Please check your City name".format(location))
else:
    city = api_data['location']['name']
    state = api_data['location']['region']
    country = api_data['location']['country']
    time = api_data['location']['localtime']
    temp_city_C = api_data['current']['temp_c']
    temp_city_f = api_data['current']['temp_f']
    weather_desc = api_data['current']['condition']['text']
    humidity = api_data['current']['humidity']
    wind_speed_mph = api_data['current']['wind_mph']
    wind_speed_kph = api_data['current']['wind_kph']


print("-----------------------------------------")
print("Weather Stats for - {} || {} ".format(location.upper(), time))
print("State and Country- {} , {} ".format(state.upper(), country))
print("Current temperature (C) is :{} , Current temperature (f) is :{}".format(temp_city_C, temp_city_f))
print("Current weather desc :", weather_desc)
print("Current Humidity :", humidity)
print("Current Wind Speed (mph) is : {} , Current Wind Speed (kph) is : {}".format(wind_speed_mph, wind_speed_kph))

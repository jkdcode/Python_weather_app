import requests
from rich import print
from datetime import datetime

def display_current_weather(city):
  """Displays the current weather"""
  api_key = "7a1b7bb3a54afd03ao8ta3f7b40acb43"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
  response = requests.get(api_url)
  current_weather_data = response.json()
  current_weather_city = current_weather_data['city']
  current_weather_temperature = current_weather_data['temperature']['current']
    
  print(f"[cadet_blue]Today:[/cadet_blue] {round(current_weather_temperature)}ºC")

def display_forecast_weather(city_name):
  """Displays the forecast"""
  api_key = "7a1b7bb3a54afd03ao8ta3f7b40acb43"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

  response = requests.get(api_url)
  forecast_weather_data = response.json()

  for day in forecast_weather_data['daily']:
    timestamp = day['time']
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime('%A:')
    temperature = day['temperature']['day']

    if date.date() != datetime.today().date():    
      print(f"[light_cyan3]{formatted_day}[/light_cyan3] {round(temperature)}ºC")

print(f"[bold magenta]✨ Welcome to my weather app ✨[/bold magenta]")
city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
  display_current_weather(city_name)
  print(f"\n[thistle1 underline]Forecast[/thistle1 underline]")
  display_forecast_weather(city_name)
  print(f"\n[light_steel_blue3 italic]This app was built by Julie Didriksen[/light_steel_blue3 italic]")
else:
  print(f"Please enter a city")
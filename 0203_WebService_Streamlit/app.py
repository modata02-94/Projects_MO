import os 
from pathlib import Path
import requests
from pprint import pprint
from datetime import datetime
from dotenv import load_dotenv
from sql import create_table, insert_weather # import functions from sql.py

os.chdir(Path(__file__).parent)

load_dotenv()

# Get the API Key from .env

API_KEY = os.getenv("API_KEY") 

# Define parameters (cities, languages)

cities = ["Berlin", "Aachen", "Stuttgart"]
languages = ["en", "de"]

# Define the URL

URL = "https://api.openweathermap.org/data/2.5/weather"

# Data Collection (Loop over cities and languages and get info from them all via the weather app)

def get_weather_data():

    data=[] # empty list for the loop
    final_data={} # empty dict with predefined keys etc to insert the values later

    # Create the empty dict
    for city in cities:
        final_data[city] = {
            "city": city,
            "temperature": None,
            "weather_de": None,
            "weather_en": None
        }

    # Now get the values from different cities with the loop
    for city in cities:
        for lang in languages: # inner loop bc 2 lang per 1 city
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric",
                "lang": lang
            }
            response = requests.get(URL, params=params)


            if response.status_code == 429: # Rate limit (if we are too fast?)
                print("Rate limit exceeded. Sleeping...")
                time.sleep(60) # pause the script for 1 min
                continue

            if response.status_code != 200: # Check the HTTP status code (if not 200 and there is a problem)
                print(f"Error {response.status_code} for {city} ({lang})")
                continue

            data = response.json() # temporarily store the values for that city / language
            final_data[city]["temperature"] = data["main"]["temp"] # access the temperature (--> main ---> temp)

            # Seperately store the different descriptions (Eng / Ger)
            if lang == "de":
                final_data[city]["weather_de"] = data["weather"][0]["description"]
            elif lang == "en":
                final_data[city]["weather_en"] = data["weather"][0]["description"]

    return final_data



def save_to_db(final_data):
    create_table() # Create / Initialize the table
    for entry in final_data.values(): # Now instert the data collected
        insert_weather(
            entry["city"],
            entry["temperature"],
            entry["weather_de"],
            entry["weather_en"]
        )

if __name__ == "__main__":
    data = get_weather_data()
    save_to_db(data)
    

# The table is saved in the project folder
import os, requests
from dotenv import load_dotenv

# Load our env variables
# Make sure you're storing your API keys in a .env file!
load_dotenv()


def get_weather_data():
    # Pulls the data from the weather API
    city = "New York"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("OPEN_WEATHER_API_KEY")}' #os.getenv("API_KEY_NAME_HERE") pulls our API key for us.

    try:
        response = requests.get(url)
    except:
        raise Exception(f"API Request Failed!")
    if response.status_code != 200:
        raise Exception(f"Error in Open Weather API request: {response.status_code}")

    data = response.json()

    # Return the entire data response from Open Weather API in json format
    return data

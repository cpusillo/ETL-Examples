from utils.extract import get_weather_data
from utils.transform import transform_data
from utils.load import load

"""
    This is a super basic example of an ETL. It's meant to give a very
    easy introduction to pulling API data, transforming it, and doing *something* with it.
    We are not technically "loading" the data into a database in this example (check the next one!)
    
    This application simply produces a nicely formatted CSV for us.
"""

if __name__ == "__main__":

    # STEP 1: EXTRACT
    # Extract data from the Open Weather API
    weather_data = get_weather_data()

    # STEP 2: TRANSFORM
    # Transform the data into a dict object
    transformed_data = transform_data(weather_data)

    # STEP 3: LOAD
    # "Load" the data into a CSV
    load(transformed_data)

import pandas as pd


def load(weather: dict):
    # Build a dataframe from the weather object built in transform.py
    df = pd.DataFrame([weather])
    # Dump our dataframe to a csv, where "weather_data.csv" is what we want the name to be
    df.to_csv("weather_data.csv", index=False)
    return None

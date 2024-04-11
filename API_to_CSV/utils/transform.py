from utils.helpers import convert_k_f, convert_timestamp


def transform_data(data: dict):
    # Return a newly built dict object containing the relevant data
    return {
        "city": f'{data.get("name")} ({data.get("sys").get("country")})',
        "lat": data.get("coord").get("lat"),
        "long": data.get("coord").get("lon"),
        "temp": f'{convert_k_f(data.get("main").get("temp"))} F',
        "feels_like": f'{convert_k_f(data.get("main").get("feels_like"))} F',
        "min": f'{convert_k_f(data.get("main").get("temp_min"))} F',
        "max": f'{convert_k_f(data.get("main").get("temp_max"))} F',
        "humidity": convert_k_f(data.get("main").get("humidity")),
        "wind_speed": data.get("wind").get("speed"),
        "sunrise": convert_timestamp(data.get("sys").get("sunrise")),
        "sunset": convert_timestamp(data.get("sys").get("sunset")),
    }

from datetime import datetime


def convert_k_f(temp):
    # Our API gives us temps in Kelvin, we should convert that to Fahrenheit.
    return float("{:.2f}".format((temp - 273.15) * 1.8 + 32))

def convert_timestamp(ts):
    # Our API gives us times in UTC timestamp format, we should make it readble.
    ts_new = int(ts)
    return datetime.fromtimestamp(ts_new).strftime("%I:%M %p")

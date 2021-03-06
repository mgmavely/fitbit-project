
from datetime import datetime as dt


def date_and_time():
    now = dt.now()

    year = now.strftime("%Y")

    month = now.strftime("%m")

    day = now.strftime("%d")

    date_time = now.strftime("%Y-%m-%d")
    return date_time


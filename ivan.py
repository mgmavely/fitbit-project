
from datetime import datetime as dt


def date_and_time():
    now = dt.now()

    date_time = now.strftime("%Y-%m-%d")
    return date_time



def time():
    now = dt.now()
    time = now.strftime("%H:%M")
    return time
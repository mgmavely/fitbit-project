# mann patel
from playsound import playsound


def time_and_level(data):
    date_time = data["sleep"][0]["levels"]["data"][-1]["dateTime"][11:19]
    level = data["sleep"][0]["levels"]["data"][-1]["level"]
    return [date_time, level]


def play_alarm():
    playsound('alarm.mp3')


play_alarm()

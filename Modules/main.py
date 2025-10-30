import datetime
import bday_messages

def today():
    release_time = datetime.date.today()
    return release_time

def next_birthday(year, month, day):
    user_birthday = datetime.date(year, month, day)
    days_away = user_birthday - today()
    if today() == user_birthday:
        print(bday_messages.random_messages())
    else:
        print('My next birthday is {} days away!'.format(days_away.days))
    return

next_birthday(2026, 10, 29)

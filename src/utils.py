import datetime

color_list = ["red", "green", "blue", "yellow", "pink", "purple", "orange", "white", "black"]

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def check_priority(priority):
    return priority >= 0 and priority <= 2

def check_status(status):
    return status == 0 or status == 1

def check_color(color):
    return color in color_list

def check_is_int(num):
    return type(num) == int
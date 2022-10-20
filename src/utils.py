import datetime

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def check_priority(priority):
    return 0 >= priority and priority <= 2

def check_status(status):
    return status == 0 or status == 1
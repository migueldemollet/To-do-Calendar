import datetime
import re
import hashlib
from user import User
from tag import Tag
from task import Task
from friends import Friend

color_list = ["red", "green", "blue", "yellow", "pink", "purple", "orange", "white", "black"]

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def check_priority(priority):
    return priority >= 0 and priority <= 2

def check_state(status):
    return status == 0 or status == 1

def check_color(color):
    return color in color_list

def check_is_int(num):
    return (type(num) == int and num > 0)

def check_username(username):
    return (len(username) > 0 and len(username) <= 16)

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def check_password(password):
    #password must be min 8 characters long, must contain at least 1 letter, 1 number and 1 special character
    regex = r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@.#$%^&*]{8,}$'
    return re.match(regex, password)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def list_to_users(list):
    return [User(user['id'], user['username'], user['email'], user['password']) for user in list]

def list_to_tags(list, user):
    return [Tag(tag['id'], tag['name'], tag['color'], user) for tag in list]

def list_to_tasks(list, tags, user, users_shared):
    result = []
    for task, tag, user_shared in zip(list, tags, users_shared):
        result.append(
            Task(
                task['id'], 
                task['name'], 
                task['description'], 
                task['state'], 
                task['date'], 
                task['priority'], 
                task['color'], 
                tag, 
                user,
                user_shared
            )
        )
    return result

def list_to_friends(list,users):
    return [Friend(friend['id'],user,friend['state']) for friend, user in zip(list, users)]
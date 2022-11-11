import datetime
import re
import hashlib
from user import User
from tag import Tag
from task import Task
from friends import Friend

color_list = ["red", "green", "blue", "yellow", "pink", "purple", "orange", "white", "black"]

def check_date(date: str) -> bool:
    """Check if date is valid

    Args:
        date (str): date in format DD/MM/YYYY

    Returns:
        bool: True date is valid
        bool: False date is not valid
    """

    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def check_priority(priority: int) -> bool:
    """Check if priority is valid

    Args:
        priority (int): priority must be between 0 and 2
    Returns:
        bool: True priority is valid
        bool: False priority is not valid
    """

    return priority >= 0 and priority <= 2

def check_state(state: str) -> bool:
    """Check if state is valid

    Args:
        status (str): state must be 0 or 1

    Returns:
        bool: True status is valid
        bool: False status is not valid
    """

    return state == 0 or state == 1

def check_color(color: str) -> bool:
    """Check if color is valid from color list

    Args:
        color (str): color to check

    Returns:
        bool: True color is valid
        bool: False color is not valid
    """

    return color in color_list

def check_is_int(num: int) -> bool:
    """Check if num is int valid

    Args:
        num (int): num to check must be an int and upper than 0

    Returns:
        bool: True num is valid
        bool: False num is not valid
    """

    return (type(num) == int and num > 0)

def check_username(username: str) -> bool:
    """Check if username is valid

    Args:
        username (str): username must be min 1 characters long and max 16 characters long

    Returns:
        bool: True username is valid
        bool: False username is not valid
    """

    return (len(username) > 0 and len(username) <= 16)

def check_email(email: str) -> bool:
    """Check if email is valid
    
    Args:
        email (str): email to check format test@domini.es

    Returns:
        bool: True email is valid
        bool: False email is not valid
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def check_password(password: str) -> bool:
    """Check if password is valid

    Args:
        password (str): password to check
        - min 8 characters long
        - must contain at least one letter
        - must contain at least one number
        - must contain at least one special character
    
    Returns:
        bool: True password is valid
        bool: False password is not valid
    """

    regex = r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@.#$%^&*]{8,}$'
    return re.match(regex, password)

def hash_password(password: str) -> str:
    """Hash password with md5

    Args:
        password (str): password to hash
    
    Returns:
        str: hashed password
    """

    return hashlib.md5(password.encode()).hexdigest()

def list_to_users(list: list, friend: Friend) -> list[User]:
    """Convert list of users in format text to list of User objects

    Args:
        list (list): list of users in format text
        friend (Friend): friend object
    
    Returns:
        list[User]: list of User objects
    """

    return [User(user['id'], user['username'], user['email'], user['password'], friend) for user in list]

def list_to_tags(list: list, user: User) -> list[Tag]:
    """Convert list of tags in format text to list of Tag objects

    Args:
        list (list): list of tags in format text
        user (User): user object
    
    Returns:
        list[Tag]: list of Tag objects
    """

    return [Tag(tag['id'], tag['name'], tag['color'], user) for tag in list]

def list_to_tasks(list: list, tags: list[Tag], user: User, users_shared: list[User]) -> list[Task]:
    """Convert list of tasks in format text to list of Task objects

    Args:
        list (list): list of tasks in format text
        tags (list[Tag]): list of Tag objects
        user (User): user object owner of the task
        users_shared (list[User]): list of User objects shared with the task
    
    Returns:
        list[Task]: list of Task objects
    """

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

def list_to_friends(list: list, users: list[User]) -> list[Friend]:
    """Convert list of friends in format text to list of Friend objects

    Args:
        list (list): list of friends in format text
        users (list[User]): list of User objects
    
    Returns:
        list[Friend]: list of Friend objects
    """
    
    return [Friend(friend['id'], user, friend['state']) for friend, user in zip(list, users)]
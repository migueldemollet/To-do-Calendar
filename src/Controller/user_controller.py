import sys
sys.path.insert(1, 'Src/')
from task import Task
from utils import *
sys.path.insert(2, 'Src/Model/')
from user_model import UserModel
from utils import *

class UserController:
    def __init__(self):
        self.user_model = UserModel("./DB/to_do_calendar_test.db")
        self.user = []

    def add(self, user):
        if (not check_is_int(user.id)):
            print("Invalid id")
            return 1
        if (not check_username(user.username)):
            print("Invalid username")
            return 1
        if (not check_email(user.email)):
            print("Invalid email")
            return 1
        if (not check_password(user.password)):
            print("Invalid password")
            return 1
        if(self.user_model.get_by_id(user.id) == []):
            return self.user_model.add(user)
        else:
            print("User already exists")
            return 0

    #-------------------------Id----------------------------------

    def get_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        self.user = self.user_model.get_by_id(id)
        if (self.user == []):
            print("User does not exist")
            return 0
        return list_to_users(self.user)[0]

    def delete_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (self.user_model.get_by_id(id) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_id(id)
    
    #-------------------------Username-------------------------------

    def get_by_username(self, username):
        if (not check_username(username)):
            print("Invalid username username lenght must be between 1 and 16")
            return 1
        self.user = self.user_model.get_by_username(username)
        if (self.user == []):
            print("User does not exist")
            return 0
        return list_to_users(self.user)[0]

    def change_username(self, user, new_username):
        if (not check_username(user.username) or not check_username(new_username)):
            print("Invalid username username lenght must be between 1 and 16")
            return 1
        if (user.username == new_username):
            print("Username is the same")
            return 1
        if (self.user_model.get_by_username(user.username) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_username(new_username) != []):
            print("Username already exists")
            return 0
        return self.user_model.change_username(user.id, new_username)
    
    def delete_by_username(self, username):
        if (not check_username(username)):
            print("Invalid username username lenght must be between 1 and 16")
            return 1
        if (self.user_model.get_by_username(username) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_username(username)

    #-------------------------Email-------------------------------

    def get_by_email(self, email):
        if (not check_email(email)):
            print("Invalid email")
            return 1
        self.user = self.user_model.get_by_email(email)
        if (self.user == []):
            print("User does not exist")
            return 0
        return list_to_users(self.user)[0]

    def change_email(self, user, new_email):
        if (not check_username(user.username) or not check_email(new_email)):
            print("Invalid username or email")
            return 1
        if (user.email == new_email):
            print("Email is the same")
            return 1
        if (self.user_model.get_by_username(user.username) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_email(new_email) != []):
            print("Email already exists")
            return 0
        return self.user_model.change_email(user.id, new_email)

    def delete_by_email(self, email):
        if (not check_email(email)):
            print("Invalid email")
            return 1
        if (self.user_model.get_by_email(email) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_email(email)

    #-------------------------Password-------------------------------

    def change_password(self, user, new_password):
        if (not check_username(user.username) or not check_password(new_password)):
            print("Invalid username or password")
            return 1
        if (self.user_model.get_by_username(user.username) == []):
            print("User does not exist")
            return 0
        return self.user_model.change_password(user.id, has_password(new_password))

    #-------------------------Friends-------------------------------

    def add_friend(self, username, friend_username):
        if (not check_username(username) or not check_username(friend_username)):
            print("Invalid username")
            return 1
        if (self.user_model.get_by_username(username) == [] or self.user_model.get_by_username(friend_username) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_username(username)[0].friends == []):
            self.user_model.add_friend(username, friend_username)
            return True
        if (friend_username in self.user_model.get_by_username(username)[4].friends):
            print("Friend already exists")
            return 0
        self.user_model.add_friend(username, friend_username)
        return True
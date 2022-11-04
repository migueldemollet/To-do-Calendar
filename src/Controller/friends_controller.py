import sys
from utils import *

sys.path.insert(1, 'Src/controller/')
from user_controller import UserController

sys.path.insert(2, 'Src/Model/')
from friends_model import FriendsModel


class FriendModel:
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.user_controller = UserController()
        self.friends_model = FriendsModel("./DB/to_do_calendar_test.db")
        self.friends = []
        self.users= []
        
    def add(self, friend):
        if (not check_is_int(friend.id)):
            print("Invalid id")
            return 1
        if (not check_is_int(friend.user)):
            print("Invalid user")
            return 1
        if (not check_is_int(friend.state)):
            print("Invalid state")
            return 1
        if(self.friends_model.get_by_id(friend.id) == []):
            return self.friends_model.add(friend)
        else:
            print("Friend already exists")
            return 0

    #-------------------------Id----------------------------------

    def get_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        self.friends = self.friends_model.get_by_id(id)
        if (self.friend == []):
            print("Friend does not exist")
            return 0

        #self.users = [self.user_controller.get_by_id(friend['id_user_2']) for friend in self.friends]
        self.users = self.user_controller.get_by_id(self.friends[0]['id_user_2'])
        return list_to_friends(self.friends, self.users)[0]

    def delete_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (self.friends_model.get_by_id(id) == []):
            print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_id(id)

    #-------------------------Username-------------------------------

    def get_by_user(self,user_id):
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        self.friends = self.friends_model.get_by_user(user_id)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = [self.user_controller.get_by_id(friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)

    def delete_by_user(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        if (self.friends_model.get_by_user(user_id) == []):
            print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_user(user_id)

    #-------------------------State-------------------------------

    def get_by_state(self, state):
        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        self.friends = self.friends_model.get_by_state(state)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = [self.user_controller.get_by_id(friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)

    def change_state(self, user_id_1,user_id_2, new_state):
        if (not check_is_int(user_id_1)):
            print("Invalid user")
            return 1
        if (not check_is_int(user_id_2)):
            print("Invalid user")
            return 1
        if (not check_is_int(new_state)):
            print("Invalid state")
            return 1
        if (self.friends_model.get_by_user(user_id_1) == []):
            print("Friend does not exist")
            return 0
        if (self.friends_model.get_by_user(user_id_2) == []):
            print("Friend does not exist")
            return 0
        id = self.friends_model.get_id(user_id_1,user_id_2)
        return self.friends_model.change_state(id, new_state)

    def delete_by_id(self, state, user_id_1, user_id_2):
        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        if (not check_is_int(user_id_1)):
            print("Invalid user")
            return 1
        if (not check_is_int(user_id_2)):
            print("Invalid user")
            return 1
        if (self.friends_model.get_by_state(state) == []):
            print("Friend does not exist")
            return 0
        id = self.friends_model.get_id(user_id_1,user_id_2)
        return self.friends_model.delete_by_id(id)

        
    

        
        

  

































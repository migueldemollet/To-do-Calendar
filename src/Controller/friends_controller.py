import sys
sys.path.insert(1, 'Src/controller/')
from utils import *
sys.path.insert(2, 'Src/Model/')
from friends_model import FriendsModel


class FriendController:
    def __init__(self) -> None:
        self.friends_model = FriendsModel("./DB/to_do_calendar_test.db")
        self.friends = []
        self.users= []
      
        
    def add(self, user_id_1, user_id_2):
        if (not check_is_int(user_id_1)):
            print("Invalid user")
            return 1
        if (not check_is_int(user_id_2)):
            print("Invalid user")
            return 1
        if (self.friends_model.check_relationship(user_id_1,user_id_2) != []):
            print("Friend already exist")
            return 0
        return self.friends_model.add(user_id_1, user_id_2)

    def delete(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (self.friends_model.get_by_id(id) == []):
            print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_id(id)

    #-------------------------Id----------------------------------

    def get_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        self.friends = self.friends_model.get_by_id(id)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = get_user(self.friends[0]['id_user_2'])
        return list_to_friends(self.friends, [self.users])[0]

    #-------------------------Username-------------------------------

    def get_by_user(self,user_id):
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        self.friends = self.friends_model.get_by_user(user_id)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = [get_user(friend['id_user_2']) for friend in self.friends]
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

    def get_by_state(self,user_id, state):
        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        self.friends = self.friends_model.get_by_state(user_id,state)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = [get_user(friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)
       
    
    def change_state(self, id, new_state):
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (not check_is_int(new_state)):
            print("Invalid state")
            return 1
        if (self.friends_model.get_by_id(id) == []):
            print("Friend does not exist")
            return 0
        return self.friends_model.change_state(id, new_state)
        
    def delete_by_state(self, user_id, state):
        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        if (self.friends_model.get_by_state(user_id,state) == []):
            print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_state(user_id,state)
    
    #-------------------------Find-------------------------------

    def find(self, user_id, user_friend_id):
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        if (not check_is_int(user_friend_id)):
            print("Invalid user")
            return 1
        if (user_id == user_friend_id):
            print("Sorry, you need to find a friend")
            return 1
        self.friends = self.friends_model.check_relationship(user_id, user_friend_id)
        if (self.friends == []):
            print("Friend does not exist")
            return 0
        self.users = [get_user(friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)[0]

def get_user(user_id):
    from user_controller import UserController
    return UserController().get_by_id(user_id)
        
    

        
        

  

































import sys
sys.path.insert(1, 'Src/controller/')
from utils import *
sys.path.insert(2, 'Src/Model/')
from friends_model import FriendsModel


class FriendController:
    def __init__(self, db_name: str = "./DB/to_do_calendar.db") -> None:
        self.db_name = db_name
        self.friends_model = FriendsModel(self.db_name)
        self.friends = []
        self.users= []
      
    def add(self, user_id_1: int, user_id_2: int) -> int | bool:
        """Add a new friend to the database

        Args:
            user_id_1 (int): you
            user_id_2 (int): friend

        Returns:
            int: 0 error check db
            int: 1 error check values
            bool: True success
        """

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

    def delete(self, id: int) -> int | bool:
        """Delete a friend from the database

        Args:
            id (int): id of the row to delete

        Returns:
            int: 0 error check db
            int: 1 error check values
            bool: True success
        """

        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (self.friends_model.get_by_id(id) == []):
            #print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_id(id)

    #-------------------------Id----------------------------------

    def get_by_id(self, id: int) -> int | Friend:
        """Get a friend by id

        Args:
            id (int): id of the friend row

        Returns:
            int: 0 error check db
            int: 1 error check values
            Friend: success
        """

        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        self.friends = self.friends_model.get_by_id(id)
        if (self.friends == []):
            #print("Friend does not exist")
            return 0
        self.users = get_user(self.db_name, self.friends[0]['id_user_2'])
        return list_to_friends(self.friends, [self.users])[0]

    #-------------------------Username-------------------------------

    def get_by_user(self, user_id: int) -> int | list[Friend]:
        """Get a friend by id user
        
        Args:
            user_id (int): id of the user

        Returns:
            int: 0 error check db
            int: 1 error check values
            list[Friend]: success
        """

        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        self.friends = self.friends_model.get_by_user(user_id)
        if (self.friends == []):
            #print("Friend does not exist")
            return 0
        self.users = [get_user(self.db_name, friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)

    def delete_by_user(self, user_id: int) -> int | bool:
        """Delete a friend from the database

        Args:
            user_id (int): id of the user

        Returns:
            int: 0 error check db
            int: 1 error check values
            bool: True success
        """

        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        if (self.friends_model.get_by_user(user_id) == []):
            #print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_user(user_id)

    #-------------------------State-------------------------------

    def get_by_state(self,user_id: int, state: int) -> int | list[Friend]:
        """Get a friend by id user

        Args:
            user_id (int): id of the user
            state (int): state of the friend

        Returns:
            int: 0 error check db
            int: 1 error check values
            list[Friend]: success
        """

        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        self.friends = self.friends_model.get_by_state(user_id,state)
        if (self.friends == []):
            #print("Friend does not exist")
            return 0
        self.users = [get_user(self.db_name, friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)
       
    
    def change_state(self, id: int, new_state: int) -> int | bool:
        """Change the state of a friend

        Args:
            id (int): id of the friend row
            new_state (int): new state

        Returns:
            int: 0 error check db
            int: 1 error check values
            bool: True success
        """
        
        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (not check_is_int(new_state)):
            print("Invalid state")
            return 1
        if (self.friends_model.get_by_id(id) == []):
            #print("Friend does not exist")
            return 0
        return self.friends_model.change_state(id, new_state)
        
    def delete_by_state(self, user_id: int, state: int) -> int | bool:
        """Delete a friend from the database

        Args:
            user_id (int): id of the user
            state (int): state of the friend

        Returns:
            int: 0 error check db
            int: 1 error check values
            bool: True success
        """

        if (not check_is_int(state)):
            print("Invalid state")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user")
            return 1
        if (self.friends_model.get_by_state(user_id,state) == []):
            #print("Friend does not exist")
            return 0
        return self.friends_model.delete_by_state(user_id,state)
    
    #-------------------------Find-------------------------------

    def find(self, user_id: int, user_friend_id: int) -> int | Friend:
        """Find a friend by id user and id friend

        Args:
            user_id (int): your id
            user_friend_id (int): id of the friend you want to find
        
        Returns:
            int: 0 error check db
            int: 1 error check values
            Friend: success
        """

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
            #print("Friend does not exist")
            return 0
        self.users = [get_user(self.db_name, friend['id_user_2']) for friend in self.friends]
        return list_to_friends(self.friends, self.users)[0]

def get_user(db_name, user_id: int) -> int | User:
    """Get a user by id

    Args:
        user_id (int): id of the user
    
    Returns:
        int: 0 error check db
        int: 1 error check values
        User: success
    """

    from user_controller import UserController
    return UserController(db_name).get_by_id(user_id)
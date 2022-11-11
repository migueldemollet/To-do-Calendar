import sys
sys.path.insert(1, 'Src/Controller/')
from friends_controller import FriendController
from utils import *
sys.path.insert(2, 'Src/Model/')
from user_model import UserModel


class UserController:
    def __init__(self):
        self.user_model = UserModel("./DB/to_do_calendar_test.db")
        self.friend_controller = FriendController()
        self.user = []
        self.friends = []

    def add(self, user: User) -> int | bool:
        """Add a user to the database

        Args:
            user (User): User to add
        
        Returns:
            int: 0 user already exists
            int: 1 user values invalid
            bool: True user added
        """

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
            user.password = hash_password(user.password)
            return self.user_model.add(user)
        else:
            print("User already exists")
            return 0

    #-------------------------Id----------------------------------

    def get_by_id(self, id: int) -> int | User:
        """Get a user by id

        Args:
            id (int): User id
        
        Returns:
            int: 0 user does not exist
            int: 1 id invalid
            User: User
        """

        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        self.user = self.user_model.get_by_id(id)
        if (self.user == []):
            print("User does not exist")
            return 0
        self.friends = self.friend_controller.get_by_user(id)
        return list_to_users(self.user, self.friends)[0]

    def delete_by_id(self, id: int) -> int | bool:
        """Delete a user by id

        Args:
            id (int): User id
        
        Returns:
            int: 0 user does not exist
            int: 1 id invalid
            bool: True user deleted
        """

        if (not check_is_int(id)):
            print("Invalid id")
            return 1
        if (self.user_model.get_by_id(id) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_id(id)
    
    #-------------------------Username-------------------------------

    def get_by_username(self, username: str) -> int | User:
        """Get a user by username

        Args:
            username (str): User username
        
        Returns:
            int: 0 user does not exist
            int: 1 username invalid
            User: User
        """

        if (not check_username(username)):
            print("Invalid username username lenght must be between 1 and 16")
            return 1
        self.user = self.user_model.get_by_username(username)
        if (self.user == []):
            print("User does not exist")
            return 0
        self.friends = self.friend_controller.get_by_user(self.user[0]['id'])
        return list_to_users(self.user, self.friends)[0]

    def change_username(self, user: User, new_username: str) -> int | bool:
        """Change a user username

        Args:
            user (User): User
            new_username (str): New username
        
        Returns:
            int: 0 user does not exist
            int: 1 username invalid
            bool: True username changed
        """

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
    
    def delete_by_username(self, username: str) -> int | bool:
        """Delete a user by username

        Args:
            username (str): User username
        
        Returns:
            int: 0 user does not exist
            int: 1 username invalid
            bool: True user deleted
        """

        if (not check_username(username)):
            print("Invalid username username lenght must be between 1 and 16")
            return 1
        if (self.user_model.get_by_username(username) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_username(username)

    #-------------------------Email-------------------------------

    def get_by_email(self, email: str) -> int | User:
        """Get a user by email

        Args:
            email (str): User email format test@domini.es
        
        Returns:
            int: 0 user does not exist
            int: 1 email invalid
            User: User
        """

        if (not check_email(email)):
            print("Invalid email")
            return 1
        self.user = self.user_model.get_by_email(email)
        if (self.user == []):
            print("User does not exist")
            return 0
        self.friends = self.friend_controller.get_by_user(self.user[0]['id'])
        return list_to_users(self.user, self.friends)[0]

    def change_email(self, user: User, new_email: str) -> int | bool:
        """Change a user email

        Args:
            user (User): User
            new_email (str): New email format test@domini.es
        
        Returns:
            int: 0 user does not exist
            int: 1 email invalid
            bool: True email changed
        """

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

    def delete_by_email(self, email: str) -> int | bool:
        """Delete a user by email

        Args:
            email (str): User email format test@domini.es

        Returns:
            int: 0 user does not exist
            int: 1 email invalid
            bool: True user deleted
        """

        if (not check_email(email)):
            print("Invalid email")
            return 1
        if (self.user_model.get_by_email(email) == []):
            print("User does not exist")
            return 0
        return self.user_model.delete_by_email(email)

    #-------------------------Password-------------------------------

    def change_password(self, user: str, new_password: str) -> int | bool:
        """Change a user password

        Args:
            user (User): User
            new_password (str): New password should be 
            - between 8 and 16 characters
            - contain at least one letter and one number
            - contain at least one special character
        
        Returns:
            int: 0 user does not exist
            int: 1 username or password invalid
            bool: True password changed
        """

        if (not check_username(user.username) or not check_password(new_password)):
            print("Invalid username or password")
            return 1
        if (self.user_model.get_by_username(user.username) == []):
            print("User does not exist")
            return 0
        return self.user_model.change_password(user.id, hash_password(new_password))

    #-------------------------Login-------------------------------

    def login(self, username: str, password: str) -> int | bool:
        """Login a user

        Args:
            username (str): User username
            password (str): User password
        
        Returns:
            int: 0 user does not exist
            int: 1 username or password invalid
            bool: True login success
        """

        if (not check_username(username) or not check_password(password)):
            print("Invalid username or password")
            return 1
        if (self.user_model.get_by_username(username) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_username(username)[0]['password'] != hash_password(password)):
            print("Incorrect password")
            return 0
        else:
            return True
        
    #-------------------------Friends-------------------------------

    def add_friend(self, user_id: int, user_friend_id: int) -> int | bool:
        """Add a friend to a user

        Args:
            user_id (int): your id
            user_friend_id (int): User friend id

        Returns:
            int: 0 user does not exist
            int: 1 user friend does not exist
            bool: True friend added
        """
        
        if (not check_is_int(user_id) or not check_is_int(user_friend_id)):
            print("Invalid id")
            return 1
        if (self.user_model.get_by_id(user_id) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_id(user_friend_id) == []):
            print("User friend does not exist")
            return 0
        return self.friend_controller.add(user_id, user_friend_id)

    def confirm_friend(self, user_id: int, user_friend_id: int) -> int | bool:
        """Confirm state of a relationship between two users

        Args:
            user_id (int): your id
            user_friend_id (int): User friend id
        
        Returns:
            int: 0 user does not exist
            int: 1 user friend does not exist
            bool: True friend confirmed
        """

        if (not check_is_int(user_id) or not check_is_int(user_friend_id)):
            print("Invalid id")
            return 1
        if (self.user_model.get_by_id(user_id) == []):
            print("User does not exist")
            return 0
        if (self.user_model.get_by_id(user_friend_id) == []):
            print("User friend does not exist")
            return 0
        self.friends = self.friend_controller.find(user_id, user_friend_id)
        if (type(self.friends) == int):
            return self.friends
        return self.friend_controller.change_state(self.friends.id, 1)

    def delete_friend(self, friend_id: int) -> int | bool:
        """Delete a friend

        Args:
            friend_id (int): Friend id
        
        Returns:
            int: 1 id friend invalid
            bool: True friend deleted
        """
        
        if (not check_is_int(friend_id)):
            print("Invalid id")
            return 1
        return self.friend_controller.delete(friend_id)
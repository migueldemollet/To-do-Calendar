class User():
    def __init__(self, id: int, username: str, email: str, password: str, friends=[]):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.friends = friends

    def __str__(self) -> str:
        return "Username: " + self.username + "\nEmail: " + self.email + "\nPassword: " + self.password + "\nTasks: " + str(self.tasks) + "\nFriends: " + str(self.friends)

    def __eq__(self, other) -> bool:
        return self.id == other.id
    
    def get_id(self) -> int:
        return self.id
    
    def set_id(self, id: int) -> None:
        self.id = id
    
    def get_username(self) -> str:
        return self.username
    
    def set_username(self, username: str) -> None:
        self.username = username
    
    def get_email(self) -> str:
        return self.email
    
    def set_email(self, email: str) -> None:
        self.email = email
    
    def get_password(self) -> str:
        return self.password
    
    def set_password(self, password: str) -> None:
        self.password = password
    
    def get_friends(self) -> list:
        return self.friends
    
    def set_friends(self, friends: list) -> None:
        self.friends = friends
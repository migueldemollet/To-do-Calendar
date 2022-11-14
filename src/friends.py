from user import User

class Friend():
    def __init__(self, id: int, user: User, state:int):
        self.id = id
        self.user = user
        self.state = state

    def __str__(self):
        return "Users: " + str(self.users) + "\nStates: " + str(self.states)

    def __eq__(self, other):
        return self.id == other.id

    def get_id(self) -> int:
        return self.id
    
    def set_id(self, id: int) -> None:
        self.id = id
    
    def get_user(self) -> User:
        return self.user
    
    def set_user(self, user: User) -> None:
        self.user = user
    
    def get_state(self) -> int:
        return self.state
    
    def set_state(self, state: int) -> None:
        self.state = state




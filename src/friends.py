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




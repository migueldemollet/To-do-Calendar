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
        return self.username == other.username


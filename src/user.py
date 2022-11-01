class User():
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return "Username: " + self.username + "\nEmail: " + self.email + "\nPassword: " + self.password + "\nTasks: " + str(self.tasks)

    def __eq__(self, other) -> bool:
        return self.username == other.username

    def change_username(self, new_username):
        self.username = new_username

    def change_email(self, new_email):
        self.email = new_email

    def change_password(self, new_password):
        self.password = new_password


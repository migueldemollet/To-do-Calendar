class User():
    def __init__(self, username: str, email: str, password: str, tasks: list = [], friends: list = []):
        self.username = username
        self.email = email
        self.password = password
        self.tasks = tasks
        self.friends = friends

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
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def remove_friend(self, friend):
        self.friends.remove(friend)


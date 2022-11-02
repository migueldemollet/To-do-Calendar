from user import User
from tag import Tag

class Task():
    def __init__(self, id:int, name: str, description: str, state: str, date: str, priority: int, color: str, tag: Tag, user: User):
        self.id = id
        self.name = name
        self.description = description
        self.state = state
        self.date = date
        self.priority = priority
        self.color = color
        self.tag = tag
        self.user = user

    def __str__(self):
        return "Task: " + self.name + " Description: " + self.description + " State: " + self.state + " Date: " + self.date + " Priority: " + str(self.priority) + " Color: " + self.color + " Tag: " + str(self.tag) + " User: " + str(self.user)
    
    def __eq__(self, other):
        return self.name == other.name

    def start(self):
        self.state = 0

    def finish(self):
        self.state = 1

    

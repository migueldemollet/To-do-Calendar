from user import User
from tag import Tag

class Task():
    def __init__(self, id:int, name: str, description: str, state: int, date: str, priority: int, color: str, tag: Tag, user: User, user_shared = []):
        self.id = id
        self.name = name
        self.description = description
        self.state = state
        self.date = date
        self.priority = priority
        self.color = color
        self.tag = tag
        self.user = user
        self.user_shared = user_shared

    def __str__(self):
        return "Task: " + self.name + " Description: " + self.description + " State: " + self.state + " Date: " + self.date + " Priority: " + str(self.priority) + " Color: " + self.color + " Tag: " + str(self.tag) + " User: " + str(self.user)
    
    def __eq__(self, other):
        return self.id == other.id
    
    def start(self):
        self.state = 0

    def finish(self):
        self.state = 1
    
    def get_id(self) -> int:
        return self.id
    
    def set_id(self, id: int) -> None:
        self.id = id
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description: str) -> None:
        self.description = description
    
    def get_state(self) -> int:
        return self.state
    
    def set_state(self, state: int) -> None:
        self.state = state
    
    def get_date(self) -> str:
        return self.date
    
    def set_date(self, date: str) -> None:
        self.date = date
    
    def get_priority(self) -> int:
        return self.priority
    
    def set_priority(self, priority: int) -> None:
        self.priority = priority
    
    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color: str) -> None:
        self.color = color
    
    def get_tag(self) -> Tag:
        return self.tag
    
    def set_tag(self, tag: Tag) -> None:
        self.tag = tag
    
    def get_user(self) -> User:
        return self.user
    
    def set_user(self, user: User) -> None:
        self.user = user
    
    def get_user_shared(self) -> list:
        return self.user_shared
    
    def set_user_shared(self, user_shared: list) -> None:
        self.user_shared = user_shared
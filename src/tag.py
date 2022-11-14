from user import User

class Tag():
    def __init__(self, id: int, name: str, color: str, user: User):
        self.id = id
        self.name = name
        self.color = color
        self.user = user
    
    def __str__(self):
        return "Tag: " + self.name + "\nColor: " + self.color

    def __eq__(self, other):
        return self.id == other.id
    
    def get_id(self) -> int:
        return self.id
    
    def set_id(self, id: int) -> None:
        self.id = id
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color: str) -> None:
        self.color = color
    
    def get_user(self) -> User:
        return self.user
    
    def set_user(self, user: User) -> None:
        self.user = user

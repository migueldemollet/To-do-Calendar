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

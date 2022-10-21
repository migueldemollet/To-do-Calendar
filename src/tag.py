class Tag():
    def __init__(self, name: str, color='#000000'):
        self.name = name
        self.color = color
    
    def __str__(self):
        return "Tag: " + self.name + "\nColor: " + self.color

    def __eq__(self, other):
        return self.name == other.name

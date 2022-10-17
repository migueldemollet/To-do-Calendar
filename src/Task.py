class Task():
    def __init__(self, name: str, tag=None, date=None, color=None , priority=0):
        '''
        Status: 0 - not done, 1 - done
        Tag: object type Tag
        Date: object type Date
        color: object type Color in hex format
        Priority: 0 - low, 1 - medium, 2 - high
        '''
        self.name = name
        self.status = 0
        self.tag = tag
        self.date = date
        self.color = color
        self.priority = priority

    def __str__(self):
        return "Task: " + self.name + "\nStatus: " + str(self.status) + "\nTag: " + str(self.tag) + "\nDate: " + str(self.date) + "\nColor: " + str(self.color) + "\nPriority: " + str(self.priority)

    def __eq__(self, other):
        return self.name == other.name

    def finish(self):
        self.status = 1
    
    def change_date(self, new_date):
        self.date = new_date
    
    def change_tag(self, new_tag):
        self.tag = new_tag
    
    def change_color(self, new_color):
        self.color = new_color
    
    def change_priority(self, new_priority: int):
        #PRIORITIES: 0 - low, 1 - medium, 2 - high
        if new_priority == 0 or new_priority == 1 or new_priority == 2:
            self.priority = new_priority
            return self.priority
        else:
            return self.priority
    
    def remove_tag(self):
        self.tag = None
    
    def remove_date(self):
        self.date = None
    
    def remove_color(self):
        self.color = None

    def remove_priority(self):
        self.priority = 0
import sys
sys.path.insert(1, 'Src/')
from tag import Tag
from utils import *
sys.path.insert(2, 'Src/Model/')
from tag_model import TagModel

class TagController:
    def __init__(self):
        self.tag_model = TagModel("./DB/to_do_calendar_test.db")

    def add(self, tag):
        if (not check_is_int(tag.user.id)):
            print("Invalid user id")
            return 1
        if (not check_color(tag.color)):
            print("Invalid color")
            return 1
        if(self.tag_model.get_by_id(tag.id) == []):
            self.tag_model.add(tag)
            return True
        else:
            print("Tag already exists")
            return 0

    def get_all(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        return self.tag_model.get_all(user_id)
    
    def delete_all(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        return self.tag_model.delete_all(user_id)

    #-------------------------Name-------------------------------

    def get_by_name(self, name, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        return self.tag_model.get_by_name(name, user_id)

    def change_name(self, name, new_name, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if(name == new_name):
            print("Tag already has this name")
            return 1

        if(self.tag_model.get_by_name(name, user_id) != []):
            return self.tag_model.change_name(name, new_name, user_id)
        else:
            print("Tag "+name+" does not exist")
            return 0
    
    def delete_by_name(self, name, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if(self.tag_model.get_by_name(name, user_id) != []):
            return self.tag_model.delete_by_name(name, user_id)
        else:
            print("Tag "+name+" does not exist")
            return 0

    #-------------------------Color-------------------------------
    
    def get_by_color(self, color, user_id):
        if (not check_color(color)):
            print("Invalid color")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        return self.tag_model.get_by_color(color, user_id)
    
    def change_color(self, tag, new_color):
        if (not check_color(new_color)):
            print("Invalid color")
            return 1

        if (not check_is_int(tag.user.id)):
            print("Invalid user id")
            return 1

        if (tag.color == new_color):
            print("Tag already has this color")
            return 1
        
        if(self.tag_model.get_by_id(tag.id) != []):
            return self.tag_model.change_color(tag.id, new_color)
        else:
            print("Tag "+tag.name+" does not exist")
            return 0
    
    def delete_by_color(self, color, user_id):
        if (not check_color(color)):
            print("Invalid color")
            return 1

        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1

        if(self.tag_model.get_by_color(color, user_id) != []):
            return self.tag_model.delete_by_color(color, user_id)
        else:
            print("Tag with color "+color+" does not exist")
            return 0
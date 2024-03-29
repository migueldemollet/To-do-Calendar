import sys
sys.path.insert(1, 'Src/Controller/')
from user_controller import UserController
from utils import *
sys.path.insert(2, 'Src/Model/')
from tag_model import TagModel

class TagController:
    def __init__(self, db_name: str = "./DB/to_do_calendar.db") -> None:
        self.tag_model = TagModel(db_name)
        self.user_controller = UserController(db_name)
        self.tags = []
        self.user = []

    def add(self, tag: Tag) -> int | bool:
        """Add a tag to the database

        Args:
            tag (Tag): Tag to be added

        Returns:
            int: 0 tag already exists
            int: 1 values are not valid
            bool: True Success
        """

        if (not check_is_int(tag.user.id)):
            print("Invalid user id")
            return 1
        if (tag.name == ""):
            print("Tag name cannot be empty")
            return 1
        if (not check_color(tag.color)):
            print("Invalid color")
            return 1
        if ([self.user_controller.get_by_id(tag.user.id)] == []):
            print("User does not exist")
            return 1
        if(self.tag_model.get_by_id(tag.id) == []):
            return self.tag_model.add(tag)
        else:
            print("Tag already exists")
            return 0

    #-------------------------id-------------------------------
    
    def get_by_id(self, id: int) -> int | Tag:
        """Get a tag by id

        Args:
            id (int): Tag id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            Tag: Success
        """

        if (not check_is_int(id)):
            print("Invalid tag id")
            return 1
        self.tags = self.tag_model.get_by_id(id)
        if (self.tags == []):
            print("Tag does not exist")
            return 0
        self.user = self.user_controller.get_by_id(self.tags[0]['id_user'])
        return list_to_tags(self.tags, self.user)[0]

    def delete_by_id(self, id: int) -> int | bool:
        """Delete a tag by id

        Args:
            id (int): Tag id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            bool: True Success
        """

        if (not check_is_int(id)):
            print("Invalid tag id")
            return 1
        if(self.tag_model.get_by_id(id) != []):
            return self.tag_model.delete_by_id(id)
        else:
            print("Tag does not exist")
            return 0

    #-------------------------Name-------------------------------

    def get_by_name(self, name: str, user_id: int) -> int | list[Tag]:
        """Get a tag by name

        Args:
            name (str): Tag name
            user_id (int): User id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            list[Tag]: Success
        """

        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (name == ""):
            print("Tag name cannot be empty")
            return 1
        self.tags = self.tag_model.get_by_name(name, user_id)
        if (self.tags == []):
            print("Tag does not exist")
            return 0
        self.user = self.user_controller.get_by_id(user_id)
        return list_to_tags(self.tags, self.user)

    def change_name(self, tag: int, new_name: str) -> int | bool:
        """Change a tag name
        
        Args:
            tag (Tag): Tag to be changed
            new_name (str): New tag name
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            bool: True Success
        """

        if (not check_is_int(tag.user.id)):
            print("Invalid user id")
            return 1
        if(tag.name == new_name):
            print("Tag already has this name")
            return 1

        if (tag.name == "" or new_name == ""):
            print("Tag name cannot be empty")
            return 1

        if(self.tag_model.get_by_id(tag.id) != []):
            return self.tag_model.change_name(tag.id, new_name)
        else:
            print("Tag "+tag.name+" does not exist")
            return 0
    
    def delete_by_name(self, name: str, user_id: int) -> int | bool:
        """Delete a tag by name

        Args:
            name (str): Tag name
            user_id (int): User id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            bool: True Success
        """

        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if(self.tag_model.get_by_name(name, user_id) != []):
            return self.tag_model.delete_by_name(name, user_id)
        else:
            print("Tag "+name+" does not exist")
            return 0

    #-------------------------Color-------------------------------
    
    def get_by_color(self, color: str, user_id: int) -> int | list[Tag]:
        """Get a tag by color

        Args:
            color (str): Tag color
            user_id (int): User id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            list[Tag]: Success
        """

        if (not check_color(color)):
            print("Invalid color")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        self.tags = self.tag_model.get_by_color(color, user_id)
        if (self.tags == []):
            print("Tag does not exist")
            return 0
        self.user = self.user_controller.get_by_id(user_id)
        return list_to_tags(self.tags, self.user)
    
    def change_color(self, tag: Tag, new_color: str) -> int | bool:
        """Change a tag color

        Args:
            tag (Tag): Tag to be changed
            new_color (str): New tag color
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            bool: True Success
        """

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
    
    def delete_by_color(self, color: str, user_id: int) -> int | bool:
        """Delete a tag by color

        Args:
            color (str): Tag color
            user_id (int): User id
        
        Returns:
            int: 0 tag does not exist
            int: 1 values are not valid
            bool: True Success
        """

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

    #-------------------------id_user-------------------------------

    def get_by_user(self, user_id: int) -> int | list[Tag]:
        """Get all tags from a user

        Args:
            user_id (int): User id

        Returns:
            int: 0 user does not exist
            int: 1 values are not valid
            list[Tag]: Success
        """

        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        self.user = self.user_controller.get_by_id(user_id)
        if(type(self.user) == int):
            print("User does not exist")
            return 0
        self.tags = self.tag_model.get_by_user(user_id)
        
        return list_to_tags(self.tags, self.user)
    
    def delete_by_user(self, user_id: int) -> int | bool:
        """Delete all tags from a user

        Args:
            user_id (int): User id
        
        Returns:
            int: 0 user does not exist
            int: 1 values are not valid
            bool: True Success
        """
        
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if(type(self.user_controller.get_by_id(user_id)) != int):
            return self.tag_model.delete_by_user(user_id)
        else:
            print("User does not exist")
            return 0
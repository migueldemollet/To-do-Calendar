import sys
sys.path.insert(1, 'Src/Controller/')
from tag_controller import TagController
from user_controller import UserController
from utils import *
sys.path.insert(2, 'Src/Model/')
from task_model import TaskModel
from tag_model import TagModel

class TaskController:
    def __init__(self):
        self.task_model = TaskModel("./DB/to_do_calendar_test.db")
        self.tag_controller = TagController()
        self.user_controller = UserController()
        self.tasks = []
        self.tags = []
        self.users = []

    def add(self, task):
        if (task.name == ""):
            print("Task name cannot be empty")
            return 1
        if (not check_state(task.state)):
            print("Invalid state must be 0 or 1")
            return 1
        if (not check_date(task.date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1
        if (not check_priority(task.priority)):
            print("Invalid priority must be 0, 1, or 2")
            return 1
        if (not check_color(task.color)):
            print("Invalid color must be"+str(color_list))
            return 1
        if ([self.tag_controller.get_by_id(task.tag.id)] == []):
            print("Tag with name "+str(task.tag.name)+" does not exist")
            return 0
        if ([self.user_controller.get_by_id(task.user.id)] == []):
            print("User with name "+str(task.user.name)+" does not exist")
            return 0
        
        if(self.task_model.get_by_id(task.id) == []):
            return self.task_model.add(task)
        else:
            print("Task already exists")
            return 0

    #-------------------------Id---------------------------------

    def get_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid user id")
            return 1
        self.tasks = self.task_model.get_by_id(id)
        if (self.tasks == []):
            print("Task with id "+str(id)+" does not exist")
            return 0
        self.user = self.user_controller.get_by_id(self.tasks[0]['id_user'])
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))
        
        return list_to_tasks(self.tasks, self.tags, self.user)[0]

    def delete_by_id(self, id):
        if (not check_is_int(id)):
            print("Invalid user id")
            return 1
        if(self.task_model.get_by_id(id) != []):
            return self.task_model.delete_by_id(id)
        else:
            print("Task with id "+str(id)+" does not exist")
            return 0

    #-------------------------Name-------------------------------

    def get_by_name(self, name, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (name == ""):
            print("Task name cannot be empty")
            return 1
        
        self.tasks = self.task_model.get_by_name(name, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))

        return list_to_tasks(self.tasks, self.tags, self.user)

    def change_name(self, task, new_name):
        if(task.name == new_name):
            print("Task already has this name")
            return 1
        if (task.name == "" or new_name == ""):
            print("Task name cannot be empty")
            return 1
        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_name(task.name, new_name, task.user.id)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_name(self, name, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (name == ""):
            print("Task name cannot be empty")
            return 1
        if(self.task_model.get_by_name(name, user_id) != []):
            return self.task_model.delete_by_name(name, user_id)
        else:
            print("Task "+name+" does not exist")
            return 0

    #-------------------------Description--------------------------

    def change_description(self, task, new_description):
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (task.description == new_description):
            print("Task already has this description")
            return 1

        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_description(task.id, new_description)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    #-------------------------State-------------------------------
    
    def get_by_state(self, status, user_id):
        if (not check_state(status)):
            print("Invalid status must be 0 or 1")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        
        self.tasks = self.task_model.get_by_state(status, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))
        
        return list_to_tasks(self.tasks, self.tags, self.user)

    def change_state(self, task, new_state):
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (not check_state(new_state)):
            print("Invalid status must be 0 or 1")
            return 1

        if (task.state == new_state):
            print("Task already has this status")
            return 1
        
        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_state(task.id, new_state)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_state(self, state, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_state(state)):
            print("Invalid status must be 0 or 1")
            return 1
        
        if(self.task_model.get_by_state(state, user_id) != []):
            return self.task_model.delete_by_state(state, user_id)
        else:
            print("Tasks with state "+str(state)+" does not exist")
            return 0

    #-------------------------Date-------------------------------

    def get_by_date(self, date, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_date(date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1
        self.tasks = self.task_model.get_by_date(date, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))
        
        return list_to_tasks(self.tasks, self.tags, self.user)

    def change_date(self, task, new_date):
        if (not check_date(new_date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1
        
        if (task.date == new_date):
            print("Task already has this date")
            return 1

        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_date(task.id, new_date)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_date(self, date, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_date(date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1
        if(self.task_model.get_by_date(date, user_id) != []):
            return self.task_model.delete_by_date(date, user_id)
        else:
            print("Task with date "+date+" does not exist")
            return 0

    #-------------------------Priority-------------------------------

    def get_by_priority(self, priority, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_priority(priority)):
            print("Invalid priority must be 0, 1 or 2")
            return 1
        self.tasks = self.task_model.get_by_priority(priority, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))
        
        return list_to_tasks(self.tasks, self.tags, self.user)


    def change_priority(self, task, new_priority):
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (not check_priority(new_priority)):
            print("Invalid priority must be 0, 1 or 2")
            return 1

        if (task.priority == new_priority):
            print("Task already has this priority")
            return 1

        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_priority(task.id, new_priority)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_priority(self, priority, user_id):
        if (not check_priority(priority)):
            print("Invalid priority must be 0, 1 or 2")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if(self.task_model.get_by_priority(priority, user_id) != []):
            return self.task_model.delete_by_priority(priority, user_id)
        else:
            print("Task with priority "+str(priority)+" does not exist")
            return 0

    #-------------------------Color-------------------------------

    def get_by_color(self, color, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_color(color)):
            print("Invalid color must be"+str(color_list))
            return 1

        self.tasks = self.task_model.get_by_color(color, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))
        
        return list_to_tasks(self.tasks, self.tags, self.user)

    def change_color(self, task, new_color):
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (not check_color(new_color)):
            print("Invalid color must be 0, 1 or 2")
            return 1

        if(task.color == new_color):
            print("Task already has this color")
            return 1

        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_color(task.id, new_color)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_color(self, color, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (not check_color(color)):
            print("Invalid color must be"+str(color_list))
            return 1
        if(self.task_model.get_by_color(color, user_id) != []):
            return self.task_model.delete_by_color(color, user_id)
        else:
            print("Task with color "+str(color)+" does not exist")
            return 0

    #-------------------------Tag-------------------------------
    
    def get_by_tag(self, tag_id, user_id):
        if (not check_is_int(tag_id)):
            print("Invalid tag id")
            return 1
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (type(self.tag_controller.get_by_id(tag_id)) == int):
            print("Tag with id "+str(tag_id)+" does not exist")
            return 0
        self.tasks = self.task_model.get_by_tag(tag_id, user_id)
        self.user = self.user_controller.get_by_id(user_id)
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))

        return list_to_tasks(self.tasks, self.tags, self.user)

    def change_tag(self, task, new_tag):
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (not check_is_int(new_tag)):
            print("Invalid tag id")
            return 1
        if (task.tag.id == new_tag):
            print("Task already has this tag")
            return 1
        if (type(self.tag_controller.get_by_id(new_tag)) == int):
            print("Tag with id "+str(new_tag)+" does not exist")
            return 0

        if(self.task_model.get_by_id(task.id) != []):
            return self.task_model.change_tag(task.id, new_tag)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def delete_by_tag(self, tag_id, user_id):
        if (not check_is_int(tag_id)):
            print("Invalid tag must be a number")
            return 1
        
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        
        if (tag_id <= 0):
            print("Invalid tag must be a positive number")
            return 1
            
        if (type(self.tag_controller.get_by_id(tag_id)) == int):
            print("Tag "+str(tag_id)+" does not exist")
            return 0
        
        if(self.task_model.get_by_tag(tag_id, user_id) != []):
            return self.task_model.delete_by_tag(tag_id, user_id)
        else:
            print("Task with tag "+str(tag_id)+" does not exist")
            return 0

    #-------------------------User-------------------------------

    def get_by_user(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        self.user = self.user_controller.get_by_id(user_id)
        if (type(self.user) == int):
            print("User with id "+str(user_id)+" does not exist")
            return 0
        self.tasks = self.task_model.get_by_user(user_id)
        
        for task in self.tasks:
            self.tags.append(self.tag_controller.get_by_id(task['id_tag']))

        return list_to_tasks(self.tasks, self.tags, self.user)

    def delete_by_user(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        if (type(self.user_controller.get_by_id(user_id)) != int):
            return self.task_model.delete_by_user(user_id)
        else:
            print("User with id "+str(user_id)+" does not exist")
            return 0

    
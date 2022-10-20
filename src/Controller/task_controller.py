import sys
sys.path.insert(1, 'Src/')
from task import Task
from utils import *
sys.path.insert(2, 'Src/Model/')
from task_model import TaskModel
from tag_model import TagModel

class TaskController:
    def __init__(self):
        self.task_model = TaskModel("./DB/to_do_calendar_test.db")
        self.tag_model = TagModel("./DB/to_do_calendar_test.db")

    def add_task(self, task):
        if(self.task_model.get_by_name(task.name) == []):
            self.task_model.add_task(task)
            return True
        else:
            print("Task already exists")
            return 0

    def get_all_tasks(self):
        self.task_model.get_all_tasks()
        return True

    def change_name(self, name, new_name):
        if(name == new_name):
            print("Task already has this name")
            return 1

        if(self.task_model.get_by_name(name) != []):
            self.task_model.change_name(name, new_name)
            return True
        else:
            print("Task "+name+" does not exist")
            return 0

    def change_status(self, task):
        if (not check_status(self.task.status)):
            print("Invalid status must be 0 or 1")
            return 1
        
        if(self.task_model.get_by_name(task.name) != []):
            if task.status == 0:
                return self.task_model.change_status(task.name, 1)
            else:
                return self.task_model.change_status(task.name, 0)
        else:
            print("Task "+task.name+" does not exist")
            return 0
    
    def change_tag(self, task, new_tag):
        if (not self.tag_model.get_by_id(new_tag)):
            print("Tag "+new_tag+" does not exist")
            return 0

        if(self.task_model.get_by_name(task.name) != []):
            return self.task_model.change_tag(task.name, new_tag)
        else:
            print("Task "+self.task.name+" does not exist")
            return 0

    def change_date(self, task, new_date):
        if (not check_date(new_date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1

        if(self.task_model.get_by_name(task.name) != []):
            return self.task_model.change_date(task.name, new_date)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def change_color(self, task, new_color):
        if(task.color == new_color):
            print("Task already has this color")
            return 1

        if(self.task_model.get_by_name(task.name) != []):
            return self.task_model.change_color(task.name, new_color)
        else:
            print("Task "+task.name+" does not exist")
            return 0

    def change_priority(self, task, new_priority):
        if (not check_priority(new_priority)):
            print("Invalid priority must be 0, 1 or 2")
            return 1

        if (task.priority == new_priority):
            print("Task already has this priority")
            return 0

        if(self.task_model.get_by_name(self.task.name) != []):
            self.task_model.change_priority(self.task.name, new_priority)
        else:
            print("Task "+self.task.name+" does not exist")

    def delete_all_tasks(self):
        self.task_model.delete_all_tasks()

    def delete_by_name(self, name):
        if(self.task_model.get_by_name(name) != []):
            return self.task_model.delete_by_name(name)
        else:
            print("Task "+name+" does not exist")
            return 0

    def delete_by_status(self, task, status):
        if (not check_status(status)):
            print("Invalid status must be 0 or 1")
            return 1
        if(self.task_model.get_by_status(task.status) != []):
            return self.task_model.delete_by_status(status)
        else:
            print("Tasks with status "+task.status+" does not exist")
            return 0

    def delete_by_tag(self, task):
        if(self.task_model.get_by_tag(task.tag) != []):
            return self.task_model.delete_by_tag(task.tag)
        else:
            print("Task with this tag does not exist")
            return 0

    def delete_by_date(self, date):
        if (not check_date(date)):
            print("Invalid date format (dd/mm/yyyy)")
            return 1
        if(self.task_model.get_by_date(date) != []):
            return self.task_model.delete_by_date(date)
        else:
            print("Task with date "+date+" does not exist")
            return 0
import sys
sys.path.insert(1, 'Src/Controller')
from user_controller import UserController
from utils import *
sys.path.insert(2, 'Src/Model/')
from user_task_model import UserTaskModel


class TaskActionController():
    def __init__(self):
        self.model_task_user = UserTaskModel("./DB/to_do_calendar_test.db")
        self.user_controller = UserController()
        self.users = []
        self.tasks = []

    def add(self, task):
        if (not check_is_int(task.id)):
            print("Invalid task id")
            return 1
        if (not check_is_int(task.user.id)):
            print("Invalid user id")
            return 1
        if (self.model_task_user.check_user_task(task.user.id, task.id, 0) != []):
            print("Task already exists")
            return 0
            
        return self.model_task_user.add(task.user, task, 0)
    
    def share(self, task, user):
        if (not check_is_int(task.id)):
            print("Invalid task id")
            return 1
        if (not check_is_int(user.id)):
            print("Invalid user id")
            return 1
        if (self.model_task_user.check_user_task(user.id, task.id, 1) != []):
            print("Task already shared")
            return 0
        return self.model_task_user.add(user, task, 1)
    
    def unshare(self, task, user):
        if (not check_is_int(task.id)):
            print("Invalid task id")
            return 1
        if (not check_is_int(user.id)):
            print("Invalid user id")
            return 1
        if (self.model_task_user.check_user_task(user.id, task.id, 1) == []):
            print("Task is not shared")
            return 0
        return self.model_task_user.delete_by_user_task_role(user.id, task.id)

    def get_users_by_task(self, task_id):
        if (not check_is_int(task_id)):
            print("Invalid task id")
            return 1
        self.tasks = self.model_task_user.get_by_task(task_id, 1)
        if (self.tasks == []):
            print("Task not found")
            return 0
        return [self.user_controller.get_by_id(task['user_id']) for task in self.tasks]
    
    def get_tasks_by_user(self, user_id):
        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        self.tasks = self.model_task_user.get_by_user(user_id, 1)
        if (self.tasks == []):
            print("User not found")
            return 0

        from task_controller import TaskController
        return [TaskController().get_by_id(task['task_id']) for task in self.tasks]
        
        
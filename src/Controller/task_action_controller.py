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

    def add(self, task: Task) -> int | bool:
        """Add a task to the database

        Args:
            task (Task): Task to be added
        
        Returns:
            int: 0 task already exists
            int: 1 values are not valid
            bool: True Success
        """

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
    
    def share(self, task: Task, user: User) -> int | bool:
        """Share a task with a user

        Args:
            task (Task): Task to be shared
            user (User): User to share the task with
        
        Returns:
            int: 0 task already shared
            int: 1 values are not valid
            bool: True Success
        """

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
    
    def unshare(self, task: Task, user: User) -> int | bool:
        """Unshare a task with a user

        Args:
            task (Task): Task to be unshared
            user (User): User to unshare the task with

        Returns:
            int: 0 task not shared
            int: 1 values are not valid
            bool: True Success
        """

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

    def get_users_by_task(self, task_id: int) -> int | list[User]:
        """Get the users that have access to a task

        Args:
            task_id (int): Task id

        Returns:
            int: 0 task not found
            int: 1 values are not valid
            list[User]: Success
        """

        if (not check_is_int(task_id)):
            print("Invalid task id")
            return 1
        self.tasks = self.model_task_user.get_by_task(task_id, 1)
        if (self.tasks == []):
            #print("Task not found")
            return 0
        return [self.user_controller.get_by_id(task['user_id']) for task in self.tasks]
    
    def get_tasks_by_user(self, user_id: int) -> int | list[Task]:
        """Get the tasks that a user has access to

        Args:
            user_id (int): User id
        
        Returns:
            int: 0 user not found
            int: 1 values are not valid
            list[Task]: Success
        """

        if (not check_is_int(user_id)):
            print("Invalid user id")
            return 1
        self.tasks = self.model_task_user.get_by_user(user_id, 1)
        if (self.tasks == []):
            print("User not found")
            return 0

        from task_controller import TaskController
        return [TaskController().get_by_id(task['task_id']) for task in self.tasks]
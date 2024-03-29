import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from task import Task
from tag import Tag
from user import User
sys.path.insert(1, 'Src/Controller/')
from task_action_controller import TaskActionController
from random import randint

class TestTaskActionController(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.controller = TaskActionController("./DB/to_do_calendar_test.db")
        self.user1 = User(1, "user1", "user1@tdcalendar.com", "password1", [])
        self.user2 = User(2, "user2", "user2@tdcalendar.com", "password1", [])
        self.user3 = User(3, "user3", "user3@tdcalendar.com", "password1", [])
        self.tag1 = Tag(1, "tag1", "red", self.user1)
        self.tag2 = Tag(2, "tag2", "blue", self.user1)
        self.tag3 = Tag(3, "tag3", "green", self.user2)
        self.task1 = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1, [self.user2])
        self.task2 = Task(2, "task2", "description2", 1, "01/01/2022", 1, "blue", self.tag2, self.user1, [])
        self.task3 = Task(3, "task3", "description3", 1, "01/01/2022", 2, "green", self.tag3, self.user2, [])

    def setUp(self):
        restore()
    
    def tearDown(self):
        restore()
    
    #-------------------------Create task-------------------------------
    
    def test_create_task_correct(self):
        priorities = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        tags = [self.tag1, self.tag3, self.tag2, self.tag1, self.tag3, self.tag2, self.tag1, self.tag3, self.tag2]
        users = [self.user3, self.user1, self.user2, self.user2, self.user3, self.user1, self.user1, self.user2, self.user1]
        id = 4
        for priority, tag, user in zip(priorities, tags, users):
            task = Task(id, "task"+str(id), "description4", randint(0, 1), "01/01/2022", priority, "red", tag, user, [])
            self.assertEqual(self.controller.add(task), True)
            id += 1 
    
    def test_create_task_incorrect_value(self):
        self.task2.set_id("fer")
        self.assertEqual(self.controller.add(self.task2), 1)
        self.task2.id = 2
        self.task3.get_user().set_id("fer")
        self.assertEqual(self.controller.add(self.task3), 1)

    def test_create_task_incorrect_db(self):
        self.assertEqual(self.controller.add(self.task1), 0)

    #-------------------------Share-------------------------------
    
    def test_share_task_correct(self):
        self.assertEqual(self.controller.share(self.task2, self.user1), True)

    def test_share_task_incorrect_value(self):
        self.task2.set_id("fer")
        self.assertEqual(self.controller.share(self.task2, self.user2), 1)
        self.task2.set_id(2)
        self.task2.get_user().set_id("fer")
        self.assertEqual(self.controller.share(self.task3, self.user2), 1)
        self.task3.get_user().set_id(3)
        self.assertEqual(self.controller.share(self.task3, self.user2), 1)

    def test_share_task_incorrect_db(self):
        self.assertEqual(self.controller.share(self.task1, self.user2), 0)

    #-------------------------Unshare-------------------------------
    
    def test_unshare_task_correct(self):
        self.assertEqual(self.controller.unshare(self.task1, self.user2), True)
        self.assertEqual(self.controller.unshare(self.task2, self.user1), 0)
    
    def test_unshare_task_incorrect_value(self):
        self.task1.set_id("fer")
        self.assertEqual(self.controller.unshare(self.task1, self.user2), 1)
        self.task1.set_id(1)
        self.user2.set_id("fer")
        self.assertEqual(self.controller.unshare(self.task1, self.user2), 1)

    def test_unshare_task_incorrect_db(self):
        self.assertEqual(self.controller.unshare(self.task2, self.user1), 0)
    
    #-------------------------Task_id-------------------------------
    
    def test_get_user_by_task_id_correct(self):
        self.assertEqual(self.controller.get_users_by_task(self.task1.id), [self.user2]) 
    
    def test_get_user_by_task_id_incorrect_value(self):
        self.assertEqual(self.controller.get_users_by_task("fer"), 1)
    
    def test_get_user_by_task_id_incorrect_db(self):
        self.assertEqual(self.controller.get_users_by_task(4), 0)
    
    #-------------------------User_id-------------------------------

    def test_get_tasks_by_user_id_correct(self):
        self.assertEqual(self.controller.get_tasks_by_user(self.user2.id), [self.task1])

    def test_get_tasks_by_user_id_incorrect_value(self):
        self.assertEqual(self.controller.get_tasks_by_user("fer"), 1)
    
    def test_get_tasks_by_user_id_incorrect_db(self):
        self.assertEqual(self.controller.get_tasks_by_user(4), 0)
    
def restore():
    conn = sqlite3.connect('./DB/to_do_calendar_test.db')
    c = conn.cursor()

    #remove tables
    c.execute('''DROP TABLE IF EXISTS user''')
    c.execute(
    '''
    CREATE TABLE `user` (
      `id` integer PRIMARY KEY AUTOINCREMENT,
      `username` varchar(50) NOT NULL,
      `email` varchar(50) NOT NULL,
      `password` varchar(50) NOT NULL
    ) 
    '''
    )

    c.execute('''DROP TABLE IF EXISTS tag''')

    c.execute(
    '''
    CREATE TABLE `tag` (
      `id` integer PRIMARY KEY AUTOINCREMENT,
      `name` varchar(250) NOT NULL,
      `color` varchar(250) NOT NULL DEFAULT 'white',
      `id_user` int(10) NOT NULL,
      FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
    ) 
    '''
    )

    c.execute('''DROP TABLE IF EXISTS task''')
    c.execute(
    '''
    CREATE TABLE `task` (
      `id` integer PRIMARY KEY AUTOINCREMENT,
      `name` varchar(250) NOT NULL,
      `description` text NOT NULL DEFAULT '',
      `state` int(2) NOT NULL DEFAULT 0,
      `date` varchar(150) NOT NULL,
      `priority` int(2) NOT NULL DEFAULT 0,
      `color` varchar(150) NOT NULL DEFAULT 'white',
      `id_tag` int(10) NOT NULL,
      `id_user` int(10) NOT NULL,
      FOREIGN KEY (`id_tag`) REFERENCES `tag` (`id`) ON DELETE CASCADE,
      FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE
    )
    '''
    )

    c.execute('''DROP TABLE IF EXISTS user_task''')
    c.execute(
    '''
    CREATE TABLE `user_task` (
      `id` integer PRIMARY KEY AUTOINCREMENT,
      `user_id` int(10) NOT NULL,
      `task_id` int(10) NOT NULL,
      `role` int(2) NOT NULL,
      FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
      FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE
    ) 
    '''
    )

    #insert data
    c.execute(
    '''
    INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
    (1, 'user1', 'user1@tdcalendar.com', 'password1'),
    (2, 'user2', 'user2@tdcalendar.com', 'password1'),
    (3, 'user3', 'user3@tdcalendar.com', 'password1')
    '''
    )

    c.execute(
    '''
    INSERT INTO `tag` (`id`, `name`, `color`, `id_user`) VALUES
    (1, 'tag1', 'red', 1),
    (2, 'tag2', 'blue', 1),
    (3, 'tag3', 'green', 2)
    '''
    )

    c.execute(
    '''
    INSERT INTO `task` (`id`, `name`, `description`, `state`, `date`, `priority`, `color`, `id_tag`, `id_user`) VALUES
    (1, 'task1', 'description1', 0, '01/01/2022', 0, 'red', 1, 1),
    (2, 'task2', 'description2', 1, '01/02/2022', 1, 'blue', 2, 1),
    (3, 'task3', 'description3', 1, '01/03/2022', 2, 'green', 3, 2)
    '''
    )

    c.execute(
    '''
    INSERT INTO `user_task` (`id`, `user_id`, `task_id`, `role`) VALUES
    (1, 1, 1, 0),
    (2, 1, 2, 0),
    (3, 2, 3, 0),
    (4, 2, 1, 1)
    '''
    )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    unittest.main()
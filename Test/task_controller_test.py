import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from task import Task
from tag import Tag
from user import User
sys.path.insert(1, 'Src/Controller/')
from task_controller import TaskController


class TestTaskController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = TaskController()
        self.user1 = User(1, "user1", "user1@tdcalendar.com", "password1")
        self.user2 = User(2, "user2", "user2@tdcalendar.com", "password1")
        self.tag1 = Tag(1, "tag1", "red", self.user1)
        self.tag2 = Tag(2, "tag2", "blue", self.user1)
        self.tag3 = Tag(3, "tag3", "green", self.user2)
        self.task1 = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.task2 = Task(2, "task2", "description2", 1, "01/01/2022", 1, "blue", self.tag2, self.user1)
        self.task3 = Task(3, "task3", "description3", 1, "01/01/2022", 2, "green", self.tag3, self.user2)


    def setUp(self):
        restore()
    
    def tearDown(self):
        restore()


    def test_add_task(self):
        task = Task(4, "task4", "description4", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.add(task), True)
        self.assertEqual(self.controller.add(task), 0)
        task.name = ""
        self.assertEqual(self.controller.add(task), 1)
        task.name = "task4"
        task.date = "dfko/ds/2022"
        self.assertEqual(self.controller.add(task), 1)
        task.date = "01/01/2022"
        task.priority = -1
        self.assertEqual(self.controller.add(task), 1)
        task.priority = 3
        self.assertEqual(self.controller.add(task), 1)
        task.priority = 0
        task.color = "sdff"
        self.assertEqual(self.controller.add(task), 1)
        task.color = "red"
        task.tag.id = 0
        self.assertEqual(self.controller.add(task), 0)
        task.tag.id = 1
        task.user.id = 0
        self.assertEqual(self.controller.add(task), 0)

    #-------------------------Id---------------------------------

    def test_get_by_id(self):
        task = self.controller.get_by_id(1)
        self.assertEqual(task, self.task1)
        self.assertEqual(self.controller.get_by_id(2), self.task2)
        self.assertEqual(self.controller.get_by_id(3), self.task3)
        self.assertEqual(self.controller.get_by_id(4), 0)
        self.assertEqual(self.controller.get_by_id(0), 1)
        self.assertEqual(self.controller.get_by_id("sdsd"), 1)

    def test_delete_by_id(self):
        self.assertEqual(self.controller.delete_by_id(1), True)
        self.assertEqual(self.controller.delete_by_id(1), 0)
        self.assertEqual(self.controller.delete_by_id(2), True)
        self.assertEqual(self.controller.delete_by_id(0), 1)
        self.assertEqual(self.controller.delete_by_id(4), 0)
        self.assertEqual(self.controller.delete_by_id("dfd"), 1)

    #-------------------------Name-------------------------------

    def test_get_by_name(self):
        self.assertEqual(self.controller.get_by_name("task1", self.task1.user.id), [self.task1])
        self.assertEqual(self.controller.get_by_name("task2", self.task2.user.id), [self.task2])
        self.assertEqual(self.controller.get_by_name("task3", self.task3.user.id), [self.task3])
        self.assertEqual(self.controller.get_by_name("task4", self.task1.user.id), [])
        self.assertEqual(self.controller.get_by_name('', self.task1.user.id), 1)
        self.assertEqual(self.controller.get_by_name("task1", 0), 1)

    def test_change_name(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_name(task, 'task4'), True)
        task.name = "task4"
        self.assertEqual(self.controller.change_name(task, 'task4'), 1)
        self.assertEqual(self.controller.change_name(task, ''), 1)
        task.user.id = 0
        self.assertEqual(self.controller.change_name(task, 'task4'), 1)

    def test_delete_by_name(self):
        self.assertEqual(self.controller.delete_by_name('task1', self.user1.id), True)
        self.assertEqual(self.controller.delete_by_name('task1', self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_name('task1xx', self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_name('', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_name('task1', 0), 1)

    #-------------------------Description--------------------------

    def test_change_despriction(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_description(task, 'description4'), True)
        task.description = "description4"
        self.assertEqual(self.controller.change_description(task, 'description4'), 1)
        self.assertEqual(self.controller.change_description(task, ''), True)
        task.user.id = 0
        self.assertEqual(self.controller.change_description(task, 'description4'), 1)

    #-------------------------State-------------------------------

    def test_get_by_state(self):
        self.assertEqual(self.controller.get_by_state(0, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_state(1, self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_state(2, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_state(-1, self.user1.id), 1)

    def test_change_state(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_state(task, 1), True)
        task.state = 1
        self.assertEqual(self.controller.change_state(task, 1), 1)
        self.assertEqual(self.controller.change_state(task, 2), 1)
        self.assertEqual(self.controller.change_state(task, -1), 1)
        self.assertEqual(self.controller.change_state(task_invented, 1), 0)

    def test_delete_by_status(self):
        self.assertEqual(self.controller.delete_by_state(0, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_state(0, self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_state(1, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_state(2, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_state(-1, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_state(-1, "f"), 1)

    #-------------------------Date-------------------------------

    def test_get_by_date(self):
        self.assertEqual(self.controller.get_by_date('01/01/2022', self.user1.id), [self.user1])
        self.assertEqual(self.controller.get_by_date('01/02/2022', self.user1.id), [self.user2])
        self.assertEqual(self.controller.get_by_date('01/03/2022', self.user1.id), [])
        self.assertEqual(self.controller.get_by_date('01/0sd4/sa2022', self.user1.id), 1)
        self.assertEqual(self.controller.get_by_date('01/01/2022', "ff"), 1)

    def test_change_date(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), True)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '35/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '45/-2/e3'), 1)
        self.assertEqual(self.controller.change_date(task_invented, '01/04/2022'), 0)
    
    def test_delete_by_date(self):
        self.assertEqual(self.controller.delete_by_date('01/01/2022', self.user1.id), True)
        self.assertEqual(self.controller.delete_by_date('01/01/2022', self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_date('111/32/2022', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_date('01/01/2022', "fsdas"), 1)

    #-------------------------Priority-------------------------------

    def test_get_by_priority(self):
        self.assertEqual(self.controller.get_by_priority(0, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_priority(1, self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_priority(2, self.user2.id), [self.task3])
        self.assertEqual(self.controller.get_by_priority(3, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_priority(-1, self.user1.id), 1)

    def test_change_priority(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_priority(task, 1), True)
        task.priority = 1
        self.assertEqual(self.controller.change_priority(task, 2), True)
        task.priority = 2
        self.assertEqual(self.controller.change_priority(task, 2), 1)
        self.assertEqual(self.controller.change_priority(task, -1), 1)
        self.assertEqual(self.controller.change_priority(task, 3), 1)
        self.assertEqual(self.controller.change_priority(task_invented, 2), 0)

    def test_delete_by_priority(self):
        self.assertEqual(self.controller.delete_by_priority(1, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_priority(1, self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_priority(2, self.user2.id), True)
        self.assertEqual(self.controller.delete_by_priority(2, self.user2.id), 0)
        self.assertEqual(self.controller.delete_by_priority(3, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_priority(-1, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_priority(1, "fsdas"), 1)

    #-------------------------Color-------------------------------

    def test_get_by_color(self):
        self.assertEqual(self.controller.get_by_color('red', self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_color('blue', self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_color('green', self.user1.id), [])
        self.assertEqual(self.controller.get_by_color('red1', self.user1.id), 1)
        self.assertEqual(self.controller.get_by_color('blue', "fd"), 1)
    
    def test_change_color(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_color(task, 'blue'), True)
        self.assertEqual(self.controller.change_color(task, 'blue'), 1)
        self.assertEqual(self.controller.change_color(task, 'left'), 1)
        self.assertEqual(self.controller.change_color(task_invented, 'blue'), 0)

    def test_delete_by_color(self):
        self.assertEqual(self.controller.delete_by_color('red', self.user1.id), True)
        self.assertEqual(self.controller.delete_by_color('red', self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_color('dfdfd', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_color('red', "fsdas"), 1)

    #-------------------------Tag-------------------------------

    def test_get_by_tag(self):
        self.assertEqual(self.controller.get_by_tag(1, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_tag(2, self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_tag(3, self.user2.id), [self.task3])
        self.assertEqual(self.controller.get_by_tag(0, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_tag(4, self.user1.id), 0)
        self.assertEqual(self.controller.get_by_tag("sdsd", self.user1.id), 1)
        self.assertEqual(self.controller.get_by_tag(1, "sdsd"), 1)
    
    def test_change_tag(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_tag(task, 2), True)
        self.assertEqual(self.controller.change_tag(task, 2), 1)
        self.assertEqual(self.controller.change_tag(task, 4), 0)
        self.assertEqual(self.controller.change_tag(task, 0), 1)
        self.assertEqual(self.controller.change_tag(task_invented, 2), 0)

    def test_delete_by_tag(self):
        self.assertEqual(self.controller.delete_by_tag(1, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_tag(0, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_tag(5, self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_tag("dfd", self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_tag(1, "fsdas"), 1)

    #-------------------------User-------------------------------

    def test_get_by_user(self):
        self.assertEqual(self.controller.get_by_user(self.user1.id), [self.task1, self.task2])
        self.assertEqual(self.controller.get_by_user(self.user2.id), [self.task3])
        self.assertEqual(self.controller.get_by_user("sdsd"), 1)
        self.assertEqual(self.controller.get_by_user(8520), 0)

    def test_delete_by_user(self):
        self.assertEqual(self.controller.delete_by_user(self.user1.id), True)
        self.assertEqual(self.controller.delete_by_user("dfd"), 1)
        self.assertEqual(self.controller.delete_by_user(8520), 0)


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

    #insert data
    c.execute(
    '''
    INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
    (1, 'user1', 'user1@tdcalendar.com', 'password1'),
    (2, 'user2', 'user2@tdcalendar.com', 'password1')
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

    conn.commit()
    conn.close()

if __name__ == '__main__':
    unittest.main()
        
    
import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from task import Task
from tag import Tag
from user import User
sys.path.insert(1, 'Src/Controller/')
from task_controller import TaskController
from random import randint


class TestTaskController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = TaskController()
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

    #-------------------------Add------------------------------

    def test_add_correct(self):
        priorities = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        tags = [self.tag1, self.tag3, self.tag2, self.tag1, self.tag3, self.tag2, self.tag1, self.tag3, self.tag2]
        users = [self.user3, self.user1, self.user2, self.user2, self.user3, self.user1, self.user1, self.user2, self.user1]
        id = 4
        for priority, tag, user in zip(priorities, tags, users):
            task = Task(id, "task"+str(id), "description4", randint(0, 1), "01/01/2022", priority, "red", tag, user)
            self.assertEqual(self.controller.add(task), True)
            id += 1 

        
    def test_add_incorrect_values(self):
        task = Task(4, "task4", "description4", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
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
    
    def test_add_incorrect_db(self):
        task = Task(4, "task4", "description4", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.controller.add(task), True
        self.assertEqual(self.controller.add(task), 0)
        task.tag.id = 0
        self.assertEqual(self.controller.add(task), 0)
        task.tag.id = 1
        task.user.id = 0
        self.assertEqual(self.controller.add(task), 0)
    

    #-------------------------Share------------------------------

    def test_share_correct(self):
        self.assertEqual(self.controller.share(self.task2, self.user1), True)
    
    def test_share_incorrect_values(self):
        self.task2.id = 0
        self.assertEqual(self.controller.share(self.task2, self.user2), 1)
        self.task2.id = 2
        self.user2.id = 0
        self.assertEqual(self.controller.share(self.task2, self.user2), 1)
    
    def test_share_incorrect_db(self):
        self.controller.share(self.task2, self.user1)
        self.assertEqual(self.controller.share(self.task2, self.user1), 0)

    
    #-------------------------Unshare------------------------------

    def test_unshare_correct(self):
        self.assertEqual(self.controller.unshare(self.task1, self.user2), True)
    
    def test_unshare_incorrect_values(self):
        self.task1.id = 0
        self.assertEqual(self.controller.unshare(self.task1, self.user2), 1)
        self.task1.id = 1
        self.user2.id = 0
        self.assertEqual(self.controller.unshare(self.task1, self.user2), 1)
    
    def test_unshare_incorrect_db(self):
        self.controller.unshare(self.task1, self.user2)
        self.assertEqual(self.controller.unshare(self.task1, self.user2), 0)

    


    #-------------------------Id:get---------------------------------

    def test_get_by_id_correct(self):
        self.assertEqual(self.controller.get_by_id(1), self.task1)
        self.assertEqual(self.controller.get_by_id(2), self.task2)
        self.assertEqual(self.controller.get_by_id(3), self.task3)
    
    def test_get_by_id_incorrect_values(self):
        self.assertEqual(self.controller.get_by_id(0), 1)
        self.assertEqual(self.controller.get_by_id("sdsd"), 1)
    
    def test_get_by_id_incorrect_db(self):
        self.assertEqual(self.controller.get_by_id(4), 0)
    
    #-------------------------id:delete---------------------------------

    def test_delete_by_id_correct(self):
        self.assertEqual(self.controller.delete_by_id(1), True)
        self.assertEqual(self.controller.delete_by_id(1), 0)
        self.assertEqual(self.controller.delete_by_id(2), True)
    def test_delete_by_id_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_id(0), 1)
        self.assertEqual(self.controller.delete_by_id("dfd"), 1)
    
    def test_delete_by_id_incorrect_db(self):
        self.controller.delete_by_id(1)
        self.assertEqual(self.controller.delete_by_id(1), 0)
        self.assertEqual(self.controller.delete_by_id(4), 0)



    #-------------------------Name:get-------------------------------

    def test_get_by_name_correct(self):
        self.assertEqual(self.controller.get_by_name("task1", self.task1.user.id), self.task1)
        self.assertEqual(self.controller.get_by_name("task2", self.task2.user.id), self.task2)
        self.assertEqual(self.controller.get_by_name("task3", self.task3.user.id), self.task3)
    
    def test_get_by_name_incorrect_values(self):
        self.assertEqual(self.controller.get_by_name('', self.task1.user.id), 1)
        self.assertEqual(self.controller.get_by_name("task1", 0), 1)
    
    def test_get_by_name_incorrect_db(self):
        self.assertEqual(self.controller.get_by_name("task4", self.task1.user.id), 0)
    
    #-------------------------Name:change-------------------------------

    def test_change_name_correct(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_name(task, 'task4'), True)
        task.name = "task4"
    
    def test_change_name_incorrect_values(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_name(task, 'task4'), 1)
        self.assertEqual(self.controller.change_name(task, ''), 1)
        task.user.id = 0
        self.assertEqual(self.controller.change_name(task, 'task4'), 1)
    
    def test_change_name_incorrect_db(self):
        task = Task(575, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_name(task, 'task4'), 0)

    #-------------------------Nmae:delete-------------------------------
    def test_delete_by_name_correct(self):
        self.assertEqual(self.controller.delete_by_name('task1', self.user1.id), True)

    def test_delete_by_name_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_name('', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_name('task1', 0), 1)
    
    def test_delete_by_name_incorrect_db(self):
        self.controller.delete_by_name('task1', self.user1.id)
        self.assertEqual(self.controller.delete_by_name('task1', self.user1.id), 0)
        self.assertEqual(self.controller.delete_by_name('task1xx', self.user1.id), 0)

    
    #-------------------------Description--------------------------

    def test_change_despriction_correct(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_description(task, 'description4'), True)
        self.assertEqual(self.controller.change_description(task, ''), True)
    
    def test_change_description_incorrect_values(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task.description = "description4"
        self.assertEqual(self.controller.change_description(task, 'description4'), 1)
        task.user.id = 0
        self.assertEqual(self.controller.change_description(task, 'description4'), 1)
    
    def test_change_description_incorrect_db(self):
        task = Task(575, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_description(task, 'description4'), 0)


    #-------------------------State:get-------------------------------

    def test_get_by_state_correct(self):
        self.assertEqual(self.controller.get_by_state(0, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_state(1, self.user1.id), [self.task2])
    
    def test_get_by_state_incorrect_values(self):
        self.assertEqual(self.controller.get_by_state(2, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_state(-1, self.user1.id), 1)
    
    def test_get_by_state_incorrect_db(self):
        self.assertEqual(self.controller.get_by_state(0, self.user2.id), 0)
    
    #-------------------------State:change-------------------------------

    def test_change_state_correct(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_state(task, 1), True)

    def test_change_state_incorrect_values(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        task.state = 1
        self.assertEqual(self.controller.change_state(task, 1), 1)
        self.assertEqual(self.controller.change_state(task, 2), 1)
        self.assertEqual(self.controller.change_state(task, -1), 1)
    
    def test_change_state_incorrect_db(self):
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_state(task_invented, 1), 0)
    
    #-------------------------State:delete-------------------------------

    def test_delete_by_state_correct(self):
        self.assertEqual(self.controller.delete_by_state(0, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_state(1, self.user1.id), True)
    
    def test_delete_by_state_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_state(2, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_state(-1, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_state(-1, "f"), 1)
    
    def test_delete_by_state_incorrect_db(self):
        self.controller.delete_by_state(0, self.user1.id)
        self.assertEqual(self.controller.delete_by_state(0, self.user1.id), 0)


    #-------------------------Date:get-------------------------------

    def test_get_by_date_correct(self):
        self.assertEqual(self.controller.get_by_date('01/01/2022', self.user1.id), [self.user1])
        self.assertEqual(self.controller.get_by_date('01/02/2022', self.user1.id), [self.user2])
    
    def test_get_by_date_incorrect_values(self):
        self.assertEqual(self.controller.get_by_date('01/0sd4/sa2022', self.user1.id), 1)
        self.assertEqual(self.controller.get_by_date('01/01/2022', "ff"), 1)
    
    def test_get_by_date_incorrect_db(self):
        self.assertEqual(self.controller.get_by_date('01/01/2022', self.user2.id), 0)
    
    #-------------------------Date:change-------------------------------

    def test_change_date_correct(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), True)
    
    def test_change_date_incorrect_values(self):
        task = Task(1, "task1", "description1", 0, "01/01/2022", 0, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '35/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '45/-2/e3'), 1)
    
    def test_change_date_incorrect_db(self):
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_date(task_invented, '01/04/2022'), 0)
    
    #-------------------------Date:delete-------------------------------
    
    def test_delete_by_date(self):
        self.assertEqual(self.controller.delete_by_date('01/01/2022', self.user1.id), True)
    
    def test_delete_by_date_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_date('111/32/2022', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_date('01/01/2022', "fsdas"), 1)
    
    def test_delete_by_date_incorrect_db(self):
        self.controller.delete_by_date('01/01/2022', self.user1.id)
        self.assertEqual(self.controller.delete_by_date('01/01/2022', self.user1.id), 0)

    #-------------------------Priority:get-------------------------------

    def test_get_by_priority_correct(self):
        self.assertEqual(self.controller.get_by_priority(0, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_priority(1, self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_priority(2, self.user2.id), [self.task3])

    def test_get_by_priority_incorrect(self):
        self.assertEqual(self.controller.get_by_priority(3, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_priority(-1, self.user1.id), 1)

    def test_get_by_priority_incorrect_bd(self):
        self.assertEqual(self.controller.get_by_priority(0, 100), 0)



    #-------------------------Priority:change-------------------------------

    def test_change_priority_correct(self):
        self.assertEqual(self.controller.change_priority(self.task1, 1), True)
        self.task1.priority = 1
        self.assertEqual(self.controller.change_priority(self.task1, 2), True)
        self.task1.priority = 2

    def test_change_priority_incorrect(self):
        self.assertEqual(self.controller.change_priority(self.task1, 2), 1)
        self.assertEqual(self.controller.change_priority(self.task1, -1), 1)
        self.assertEqual(self.controller.change_priority(self.task1, 3), 1)

    def test_change_priority_incorrect_bd(self):
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_priority(task_invented, 2), 0)


    #-------------------------Priority:delete-------------------------------

    def test_delete_by_priority_correct(self):
        self.assertEqual(self.controller.delete_by_priority(1, self.user1.id), True)
        self.assertEqual(self.controller.delete_by_priority(2, self.user2.id), True)

    def test_delete_by_priority_incorrect(self):
        self.assertEqual(self.controller.delete_by_priority(3, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_priority(-1, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_priority(1, "fsdas"), 1)

    def test_delete_by_priority_incorrect_bd(self):
        self.controller.delete_by_priority(1, self.user1.id)
        self.assertEqual(self.controller.delete_by_priority(1, self.user1.id), 0)
        self.controller.delete_by_priority(2, self.user2.id)
        self.assertEqual(self.controller.delete_by_priority(2, self.user2.id), 0)


    #-------------------------Color:get-------------------------------

    def test_get_by_color_correct(self):
        self.assertEqual(self.controller.get_by_color('red', self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_color('blue', self.user1.id), [self.task2])

    def test_get_by_color_incorrect(self):
        self.assertEqual(self.controller.get_by_color('red1', self.user1.id), 1)
        self.assertEqual(self.controller.get_by_color('blue', "fd"), 1)

    def test_get_by_color_incorrect_bd(self):
        self.assertEqual(self.controller.get_by_color('green', self.user1.id), 0)
    
    #-------------------------Color:change-------------------------------

    def test_change_color_correct(self):
        self.assertEqual(self.controller.change_color(self.task1, 'blue'), True)

    def test_change_color_incorrect(self):
        self.assertEqual(self.controller.change_color(self.task1, 'blue'), 1)
        self.assertEqual(self.controller.change_color(self.task1, 'left'), 1)

    def test_change_color_incorrect_bd(self):
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_color(task_invented, 'blue'), 0)

    #-------------------------Color:delete-------------------------------

    def test_delete_by_color_correct(self):
        self.assertEqual(self.controller.delete_by_color('red', self.user1.id), True)

    def test_delete_by_color_incorrect(self):
        self.assertEqual(self.controller.delete_by_color('dfdfd', self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_color('red', "fsdas"), 1)

    def test_delete_by_color_incorrect_bd(self):
         self.controller.delete_by_color('red', self.user1.id)
         self.assertEqual(self.controller.delete_by_color('red', self.user1.id), 0)


    #-------------------------Tag:get-------------------------------#
    def test_get_by_tag_correct(self):
        self.assertEqual(self.controller.get_by_tag(1, self.user1.id), [self.task1])
        self.assertEqual(self.controller.get_by_tag(2, self.user1.id), [self.task2])
        self.assertEqual(self.controller.get_by_tag(3, self.user2.id), [self.task3])

    def test_get_by_tag_incorrect(self):
        self.assertEqual(self.controller.get_by_tag(0, self.user1.id), 1)
        self.assertEqual(self.controller.get_by_tag("sdsd", self.user1.id), 1)
        self.assertEqual(self.controller.get_by_tag(1, "sdsd"), 1)

    def test_get_by_tag_incorrect_bd(self):
        self.assertEqual(self.controller.get_by_tag(4, self.user1.id), 0)
        
    #-------------------------Tag:change-------------------------------#

    def test_change_tag_correct(self):
        self.assertEqual(self.controller.change_tag(self.task1, 2), True)

    def test_change_tag_incorrect(self):
         self.assertEqual(self.controller.change_tag(self.task1, 2), 1)
         self.assertEqual(self.controller.change_tag(self.task1, 0), 1)

    def test_change_tag_incorrect_bd(self):
        task_invented = Task(167, "task1", "description1", 0, "01/01/2022", 1, "red", self.tag1, self.user1)
        self.assertEqual(self.controller.change_tag(self.task1, 4), 0)
        self.assertEqual(self.controller.change_tag(task_invented, 2), 0)

    #-------------------------Tag:delete-------------------------------#

    def test_delete_by_tag_correct(self):
        self.assertEqual(self.controller.delete_by_tag(1, self.user1.id), True)
   
    def test_delete_by_tag_incorrect(self):
        self.assertEqual(self.controller.delete_by_tag(0, self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_tag("dfd", self.user1.id), 1)
        self.assertEqual(self.controller.delete_by_tag(1, "fsdas"), 1)

    def test_delete_by_tag_incorrect_bd(self):
        self.assertEqual(self.controller.delete_by_tag(5, self.user1.id), 0)

        
    #-------------------------User:id-------------------------------#

    def test_get_by_user_id_correct(self):
        self.assertEqual(self.controller.get_by_user(self.user1.id), [self.task1, self.task2])
    

    def test_get_by_user_id_incorrect_value(self):
        self.assertEqual(self.controller.get_by_user("sdsd"), 1)

    def test_get_by_user_id_incorrect_db(self):
        self.assertEqual(self.controller.get_by_user(100), 0)

    #-------------------------User:delete-------------------------------#

    def test_delete_by_user_id_correct(self):
        self.assertEqual(self.controller.delete_by_user(self.user1.id), True)
   
    def test_delete_by_user_id_incorrect_value(self):
        self.assertEqual(self.controller.delete_by_user("sdsd"), 1)

    def test_delete_by_user_id_incorrect_db(self):
        self.assertEqual(self.controller.delete_by_user(100), 0)
    



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
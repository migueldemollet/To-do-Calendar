import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from user import User
from task import Task
sys.path.insert(1, 'Src/Controller/')
from user_controller import UserController

class TestUserController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = UserController()
        self.user1 = User(1, "user1", "user1@tdcalendar.com", "password1")
        self.user2 = User(2, "user2", "user2@tdcalendar.com", "password1")

    def setUp(self):
        restore()

    def tearDown(self):
        restore()


    #-------------------------Add-------------------------------
    
    def test_add_user_correct(self):
        user = User(3, 'user3', 'user3@tdcalendar.com', 'password3@')
        self.assertEqual(self.controller.add(user), True)
    
    def test_add_user_incorrect_values(self):
        user = User(3, 'user3', 'user3@tdcalendar.com', 'password3@')
        user.id = "dd"
        self.assertEqual(self.controller.add(user), 1)
        user.id = 3
        user.username = ""
        self.assertEqual(self.controller.add(user), 1)
        user.username = "user3"
        user.email = "oefjwfij"
        self.assertEqual(self.controller.add(user), 1)
        user.email = "user3@tdcalendar.com"
        user.password = "a2345678"
        self.assertEqual(self.controller.add(user), 1)

    def test_add_user_incorrect_db(self):
        user = User(3, 'user3', 'user3@tdcalendar.com', 'password3@')
        self.controller.add(user)
        self.assertEqual(self.controller.add(user), 0)
    

    #-------------------------Username:get-------------------------------
    
    def test_get_by_username_correct(self):
        self.assertEqual(self.controller.get_by_username('user1'), self.user1)

    def test_get_by_username_incorrect_value(self):
        self.assertEqual(self.controller.get_by_username(''), 1)
        self.assertEqual(self.controller.get_by_username('user1sdfdcalendar'), 1)

    def test_get_by_username_incorrect_db(self):
        self.assertEqual(self.controller.get_by_username('user2323'), 0)

    #-------------------------Username:change-------------------------------

    def test_change_username_correct(self):
        self.assertEqual(self.controller.change_username(self.user1, 'user4'), True)

    def test_change_username_incorrect_value(self):
        self.assertEqual(self.controller.change_username(self.user1, 'user4'), 1)
        self.user1.username = "usesdfsdfsfsfsfsdfr1"
        self.assertEqual(self.controller.change_username(self.user1, 'user7'), 1)
        self.user1.username = "user4"
        self.assertEqual(self.controller.change_username(self.user1, 'fghfghfhfhhtrthdfdfd'), 1)
        self.user1.username = ""
        self.assertEqual(self.controller.change_username(self.user1, ''), 1)

    def test_change_username_incorrect_db(self):
        self.controller.change_username(self.user1, 'user4')
        self.assertEqual(self.controller.change_username(self.user1, 'user7'), 0)

    #-------------------------Username:delete-------------------------------

    def test_delete_by_username_correct(self):
        self.assertEqual(self.controller.delete_by_username('user1'), True)
    
    def test_delete_by_username_incorrect_value(self):
        self.assertEqual(self.controller.delete_by_username('fghfghfhfhhtrthdfdfd'), 1)
        self.assertEqual(self.controller.delete_by_username(''), 1)

    def test_delete_by_username_incorrect_db(self):
        self.controller.delete_by_username('user1')
        self.assertEqual(self.controller.delete_by_username('user1'), 0)
        self.assertEqual(self.controller.delete_by_username('user1xx'), 0)


    #-------------------------Email:get-------------------------------

    def test_get_by_email_correct(self):
        self.assertEqual(self.controller.get_by_email('user1@tdcalendar.com'), self.user1)
    
    def test_get_by_email_incorrect_value(self):
        self.assertEqual(self.controller.get_by_email(''), 1)
        self.assertEqual(self.controller.get_by_email('usdad'), 1)
    
    def test_get_by_email_incorrect_db(self):
        self.assertEqual(self.controller.get_by_email('user1wer@tdcalendar.com'), 0)

    #-------------------------Email:change-------------------------------

    def test_change_email(self):
        self.assertEqual(self.controller.change_email(self.user1, 'user0@tdcalendar.com'), True)
    
    def test_change_email_incorrect_value(self):
        self.assertEqual(self.controller.change_email(self.user1, 'user0@tdcalendar.com'), 1)
        self.user1.username = "user1"
        self.assertEqual(self.controller.change_email(self.user1, 'usertdcalendar.com'), 1)
        self.user1.email = "user1@tdcalendar.com"

    def test_change_email_incorrect_db(self):
        self.user1.username = "sdsd"
        self.assertEqual(self.controller.change_email(self.user1, 'user34@tdcalendar.com'), 0)
        self.assertEqual(self.controller.change_email(self.user1, 'user2@tdcalendar.com'), 0)

    #-------------------------Email:delete-------------------------------

    def test_delete_by_email_correct(self):
        self.assertEqual(self.controller.delete_by_email('user1@tdcalendar.com'), True)

    def test_delete_by_email_incorrect_value(self):
        self.assertEqual(self.controller.delete_by_email(''), 1)
        self.assertEqual(self.controller.delete_by_email('user1sdfdcalendar'), 1)

    def test_delete_by_email_incorrect_db(self):
        self.controller.delete_by_email('user1@tdcalendar.com')
        self.assertEqual(self.controller.delete_by_email('user1@tdcalendar.com'), 0)

    #-------------------------Password-------------------------------

    def test_change_password_correct(self):
        self.assertEqual(self.controller.change_password(self.user1, 'password1@'), True)
        self.assertEqual(self.controller.change_password(self.user1, 'a2345678@'), True)
    
    def test_change_password_incorrect_value(self):
        self.assertEqual(self.controller.change_password(self.user1, '0'), 1)
        self.assertEqual(self.controller.change_password(self.user1, 'password1'), 1)
        self.assertEqual(self.controller.change_password(self.user1, '12345678.'), 1)
        self.assertEqual(self.controller.change_password(self.user1, 'a2345678'), 1)
        self.assertEqual(self.controller.change_password(self.user1, 'adsdadsdds.'), 1)
    
    def test_change_password_incorrect_db(self):
        self.user1.username = "sdsd"
        self.assertEqual(self.controller.change_password(self.user1, 'password1@'), 0)

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
    #insert data
    c.execute(
    '''
    INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
    (1, 'user1', 'user1@tdcalendar.com', 'password1'),
    (2, 'user2', 'user2@tdcalendar.com', 'password1')
    '''
    )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    unittest.main()
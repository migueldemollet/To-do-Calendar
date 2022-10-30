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

    def setUp(self):
        restore()

    def tearDown(self):
        restore()
    
    def test_add_user(self):
        user = User('user3', 'user3@tdcalendar.com', 'password3')
        self.assertEqual(self.controller.add(user), True)
        self.assertEqual(self.controller.add(user), 0)
    
    #-------------------------Username-------------------------------
    
    def test_get_by_username(self):
        self.assertEqual(self.controller.get_by_username('user1'), [{'username': 'user1', 'email': 'user1@tdcalendar.com', 'password': 'be3a7f14702be45fd3157db6144ca5bc'}])
        self.assertEqual(self.controller.get_by_username('user2323'), 0)
        self.assertEqual(self.controller.get_by_username(''), 1)

    def test_change_username(self):
        self.assertEqual(self.controller.change_username('user1', 'user4'), True)
        self.assertEqual(self.controller.change_username('user4', 'user4'), 1)
        self.assertEqual(self.controller.change_username('user1', 'user7'), 0)

    def test_delete_by_username(self):
        self.assertEqual(self.controller.delete_by_username('user1'), True)
        self.assertEqual(self.controller.delete_by_username('user1'), 0)
        self.assertEqual(self.controller.delete_by_username('user1xx'), 0)
        self.assertEqual(self.controller.delete_by_username(''), 1)

    #-------------------------Email-------------------------------

    def test_get_by_email(self):
        self.assertEqual(self.controller.get_by_email('user1@tdcalendar.com'), [{'username': 'user1', 'email': 'user1@tdcalendar.com', 'password': 'be3a7f14702be45fd3157db6144ca5bc'}])
        self.assertEqual(self.controller.get_by_email('user1wer@tdcalendar.com'), 0)
        self.assertEqual(self.controller.get_by_email(''), 1)
        self.assertEqual(self.controller.get_by_email('usdad'), 1)

    def test_change_email(self):
        self.assertEqual(self.controller.change_email('user1', 'user0@tdcalendar.com'), True)
        self.assertEqual(self.controller.change_email('user1', 'user0@tdcalendar.com'), 1)
        self.assertEqual(self.controller.change_email('user0', 'user0@tdcalendar.com'), 0)
        self.assertEqual(self.controller.change_email('user1', 'usertdcalendar.com'), 1)

    def test_delete_by_email(self):
        self.assertEqual(self.controller.delete_by_email('user1@tdcalendar.com'), True)
        self.assertEqual(self.controller.delete_by_email('user1@tdcalendar.com'), 0)
        self.assertEqual(self.controller.delete_by_email(''), 1)
        self.assertEqual(self.controller.delete_by_email('user1sdfdcalendar'), 1)

    #-------------------------Password-------------------------------

    def test_change_password(self):
        self.assertEqual(self.controller.change_password('user1', 'password1'), True)
        self.assertEqual(self.controller.change_password('user1', '0'), 1)
        self.assertEqual(self.controller.change_password('user0', 'password1'), 0)
        self.assertEqual(self.controller.change_password('user1', 'a2345678.'), True)
        self.assertEqual(self.controller.change_password('user1', '12345678.'), 1)
        self.assertEqual(self.controller.change_password('user1', 'a2345678'), 1)


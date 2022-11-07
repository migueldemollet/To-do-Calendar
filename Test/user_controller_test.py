import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from user import User
from friends import Friend
sys.path.insert(1, 'Src/Controller/')
from user_controller import UserController

class TestUserController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = UserController()
        self.user1 = User(1, "user1", "user1@tdcalendar.com", "5e06b84ac4f276aa03afc04fd1e82856", [])
        self.user2 = User(2, "user2", "user2@tdcalendar.com", "d6f85014ab40ab641c6b801818c4b681", [])
        self.user3 = User(3, "user3", "user3@tdcalendar.com", "cc0e14efb403fc5d6a07fbe1dc278e84", [])
        self.friend = Friend(1,self.user2,1)
        self.friend_2 = Friend(2,self.user3,0)
        self.user1.friends=[self.friend,self.friend_2]


    def setUp(self):
        restore()

    def tearDown(self):
        restore()


    #-------------------------Add-------------------------------
    
    def test_add_user_correct(self):
        user = User(4, 'user4', 'user4@tdcalendar.com', 'password4@')
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
        user = User(3, 'user3', 'user3@tdcalendar.com', 'password3@')
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

    #-------------------------login-------------------------------

    def test_login_correct(self):
        self.assertEqual(self.controller.login('user1', 'password1@'), True)
        self.assertEqual(self.controller.login('user2', 'password2@'), True)
    
    def test_login_incorrect_value(self):
        self.assertEqual(self.controller.login('', 'password1'), 1)
        self.assertEqual(self.controller.login('user1', ''), 1)
        self.assertEqual(self.controller.login('user1', 'password1'), 1)
        self.assertEqual(self.controller.login('user1', 'password1'), 1)
        self.assertEqual(self.controller.login('user1', 'password1'), 1)
    
    def test_login_incorrect_db(self):
        self.assertEqual(self.controller.login('user1sdsd', 'password1@'), 0)


    #-------------------------Friend:add-------------------------------

    def test_add_friend_correct(self):
        self.assertEqual(self.controller.add_friend(self.user2.id, self.user3.id), True)

    def test_add_friend_incorrect_value(self):
        self.assertEqual(self.controller.add_friend('', self.user3.id), 1)
        self.assertEqual(self.controller.add_friend(self.user2.id, ''), 1)
        self.assertEqual(self.controller.add_friend(self.user2.id, self.user2.id), 1)
        self.assertEqual(self.controller.add_friend(self.user2.id, self.user1.id), 1)
        self.assertEqual(self.controller.add_friend(self.user2.id, self.user3.id), 1)
    
    def test_add_friend_incorrect_db(self):
        self.assertEqual(self.controller.add_friend(100, 101), 0)
        self.assertEqual(self.controller.add_friend(1, 2), 0)
    
    #-------------------------Friend:confirm-------------------------------

    def test_confirm_friend_correct(self):
        self.assertEqual(self.controller.confirm_friend(self.user1.id, self.user3.id), True)

    def test_confirm_friend_incorrect_value(self):
        self.assertEqual(self.controller.confirm_friend('', self.user3.id), 1)
        self.assertEqual(self.controller.confirm_friend(self.user2.id, ''), 1)
        self.assertEqual(self.controller.confirm_friend(self.user2.id, self.user2.id), 1)

    def test_confirm_friend_incorrect_db(self):
        self.assertEqual(self.controller.confirm_friend(100, 101), 0)
        self.assertEqual(self.controller.confirm_friend(self.user2.id, self.user1.id), 0)
        self.assertEqual(self.controller.confirm_friend(self.user2.id, self.user3.id), 0)


    

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

    c.execute('''DROP TABLE IF EXISTS friends''')

    c.execute(
    '''
    CREATE TABLE `friends` (
    `id` integer PRIMARY KEY AUTOINCREMENT,
    `id_user_1` int(10) NOT NULL,
    `id_user_2` int(10) NOT NULL,
    `state` int(2) NOT NULL DEFAULT 0,
    FOREIGN KEY (`id_user_1`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`id_user_2`) REFERENCES `user` (`id`) ON DELETE CASCADE
    )
    '''
    )

    #insert data
    c.execute(
    '''
    INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
    (1, 'user1', 'user1@tdcalendar.com', '5e06b84ac4f276aa03afc04fd1e82856'),
    (2, 'user2', 'user2@tdcalendar.com', 'd6f85014ab40ab641c6b801818c4b681'),
    (3, 'user3', 'user3@tdcalendar.com', 'cc0e14efb403fc5d6a07fbe1dc278e84')
    '''
    )

    c.execute(
        '''
        INSERT INTO `friends` (`id`, `id_user_1`, `id_user_2`, `state`) VALUES
        (1, 1, 2, 1),
        (2, 1, 3, 0)
        '''
    )



    

    conn.commit()
    conn.close()

if __name__ == '__main__':
    unittest.main()
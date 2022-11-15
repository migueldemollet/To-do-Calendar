import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from user import User
from friends import Friend
sys.path.insert(1, 'Src/Controller/')
from friends_controller import FriendController

class TestFriendsController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = FriendController("./DB/to_do_calendar_test.db")
        self.user1 = User(1, "user1","user1@tdcalendar.com", "password1")
        self.user2 = User(2, "user2","user2@tdcalendar.com", "password1")
        self.user3 = User(3, "user3","user3@tdcalendar.com", "password1")
        self.friend = Friend(1,self.user2,1)
        self.friend_2 = Friend(2,self.user3,0)
        self.user1.friends=[self.friend,self.friend_2]


    def setUp(self):
        restore()

    def tearDown(self):
        restore()


    #-------------------------Add-------------------------------#
    def test_add_friend_correct(self):
        self.assertEqual(self.controller.add(self.user2.id,self.user3.id), True)

    def test_add_friend_incorrect_values(self):
        self.assertEqual(self.controller.add("string",self.user2.id), 1)
        self.assertEqual(self.controller.add(self.user1.id,"test"), 1)

    def test_add_friend_incorrect_db(self):
        self.assertEqual(self.controller.add(self.user1.id,self.user2.id), 0)

    
    #-------------------------find-------------------------------#

    def test_find_friend_correct(self):
        self.assertEqual(self.controller.find(1,2), self.friend)

    def test_find_friend_incorrect_values(self):
        self.assertEqual(self.controller.find("string",1), 1)
        self.assertEqual(self.controller.find(1,"string"), 1)
    
    def test_find_friend_incorrect_db(self):
        self.assertEqual(self.controller.find(2,3), 0)


    #-------------------------Delete-------------------------------#

    def test_delete_friend_correct(self):
        self.assertEqual(self.controller.delete(2), True)

    def test_delete_friend_incorrect_values(self):
        self.assertEqual(self.controller.delete("string"), 1)

    def test_delete_friend_incorrect_db(self):
        self.assertEqual(self.controller.delete(3), 0)


    #-------------------------Id:get-------------------------------#

    def test_get_by_id_friend_correct(self):
        self.assertEqual(self.controller.get_by_id(1), self.friend)

    def test_get_by_id_friend_incorrect_values(self):
        self.assertEqual(self.controller.get_by_id("string"), 1)

    def test_get_by_id_friend_incorrect_db(self):
        self.assertEqual(self.controller.get_by_id(3), 0)


    #-------------------------User:get-------------------------------#

    def test_get_by_user_friend_correct(self):
        self.assertEqual(self.controller.get_by_user(1), self.user1.friends)

    def test_get_by_user_friend_incorrect_values(self):
        self.assertEqual(self.controller.get_by_user("string"), 1)

    def test_get_by_user_friend_incorrect_db(self):
        self.assertEqual(self.controller.get_by_user(4), 0)


    #-------------------------User:delete-------------------------------#

    def test_delete_by_user_friend_correct(self):
        self.assertEqual(self.controller.delete_by_user(1), True)

    def test_delete_by_user_friend_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_user("string"), 1)

    def test_delete_by_user_friend_incorrect_db(self):
        self.assertEqual(self.controller.delete_by_user(4), 0)


    #-------------------------State:state-------------------------------# 

    def test_state_friend_correct(self):
        self.assertEqual(self.controller.get_by_state(1,1), [self.friend])

    def test_state_friend_incorrect_values(self):
        self.assertEqual(self.controller.get_by_state("string",1), 1)
        self.assertEqual(self.controller.get_by_state(1,"string"), 1)

    def test_state_friend_incorrect_db(self):
        self.assertEqual(self.controller.get_by_state(1,2), 0)


    #-------------------------State:change-------------------------------#

    def test_change_state_friend_correct(self):
        self.assertEqual(self.controller.change_state(1,0), True)

    def test_change_state_friend_incorrect_values(self):
        self.assertEqual(self.controller.change_state("string",1), 1)
        self.assertEqual(self.controller.change_state(1,"string"), 1)

    def test_change_state_friend_incorrect_db(self):
        self.assertEqual(self.controller.change_state(3,1), 0)


    #-------------------------State:delete-------------------------------#
    
    def test_delete_by_state_friend_correct(self):
        self.assertEqual(self.controller.delete_by_state(1,1), True)

    def test_delete_by_state_friend_incorrect_values(self):
        self.assertEqual(self.controller.delete_by_state("string",1), 1)
        self.assertEqual(self.controller.delete_by_state(1,"string"), 1)

    def test_delete_by_state_friend_incorrect_db(self):
        self.assertEqual(self.controller.delete_by_state(1,2), 0)
 

def restore():
    conn = sqlite3.connect('./DB/to_do_calendar_test.db')
    c = conn.cursor()
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

    c.execute('''DROP TABLE IF EXISTS user''')
    c.execute(
        ''' 
        CREATE TABLE `user` (
            `id` integer PRIMARY KEY AUTOINCREMENT,
            `username` varchar(50) NOT NULL,
            `email` varchar(50) NOT NULL,
            `password` varchar(50) NOT NULL
            )'''
    )

    c.execute(
        '''
        INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
        (1, 'user1','test@gmail.com', 'password1'),
        (2, 'user2', 'test2@gmail.com', 'password2'),
        (3, 'user3', 'test3@gmail.com', 'password3')
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



    




import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from tag import Tag
from user import User
sys.path.insert(1, 'Src/Controller/')
from tag_controller import TagController

class TestTagController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = TagController()
        self.user = User(1, "user1", "user1@tdcalendar.com", "password1")

    def setUp(self):
        restore()
    
    def tearDown(self):
        restore()
    
    def test_add_tag(self):
        new_tag = Tag(4, 'tag4', 'orange', self.user)
        self.assertEqual(self.controller.add(new_tag), True)
        self.assertEqual(self.controller.add(new_tag), 0)
        new_tag.name = ''
        self.assertEqual(self.controller.add(new_tag), 1)
        new_tag.name = 'tag4'
        new_tag.color = 'sd'
        self.assertEqual(self.controller.add(new_tag), 1)
        new_tag.user = User(67, "user1", "user1@tdcalendar.com", "password1")
        self.assertEqual(self.controller.add(new_tag), 1)

    def test_get_all(self):
        self.assertEqual(self.controller.get_all(self.user.id), [{'id':1, 'name': 'tag1', 'color': 'red', 'id_user': 1}, {'id':2, 'name': 'tag2', 'color': 'blue', 'id_user': 1}])
        self.assertEqual(self.controller.get_all("df"), 1)

    def test_delete_all(self):
        self.assertEqual(self.controller.delete_all(self.user.id), True)
        self.assertEqual(self.controller.delete_all("ty"), 1)
        

    #-------------------------Name-------------------------------

    def test_get_by_name(self):
        self.assertEqual(self.controller.get_by_name('tag1', self.user.id), [{'id':1, 'name': 'tag1', 'color': 'red', 'id_user': 1}])
        self.assertEqual(self.controller.get_by_name('tag2', self.user.id), [{'id':2, 'name': 'tag2', 'color': 'blue', 'id_user': 1}])
        self.assertEqual(self.controller.get_by_name('tag3', self.user.id), [])
        self.assertEqual(self.controller.get_by_name('', self.user.id), 1)
        self.assertEqual(self.controller.get_by_name('tag3', "fff"), 1)

    def test_change_name(self):
        self.assertEqual(self.controller.change_name('tag1', 'tag4', self.user.id), True)
        self.assertEqual(self.controller.change_name('tag4', 'tag4', self.user.id), 1)
        self.assertEqual(self.controller.change_name('tag1', 'tag7', self.user.id), 0)
        self.assertEqual(self.controller.change_name('tag1', '', self.user.id), 1)
        

    def test_delete_by_name(self):
        self.assertEqual(self.controller.delete_by_name('tag1', self.user.id), True)
        self.assertEqual(self.controller.delete_by_name('tag1', self.user.id), 0)
        self.assertEqual(self.controller.delete_by_name('tag1xx', self.user.id), 0)
        self.assertEqual(self.controller.delete_by_name('tag1xx', "sd"), 1)

    #-------------------------Color-------------------------------

    def test_get_by_color(self):
        self.assertEqual(self.controller.get_by_color('red', self.user.id), [{'id':1, 'name': 'tag1', 'color': 'red', 'id_user': 1}])
        self.assertEqual(self.controller.get_by_color('blue', self.user.id), [{'id':2, 'name': 'tag2', 'color': 'blue', 'id_user': 1}])
        self.assertEqual(self.controller.get_by_color('green', self.user.id), [])
        self.assertEqual(self.controller.get_by_color('', self.user.id), 1)
        self.assertEqual(self.controller.get_by_color('blue', "self.user.id"), 1)

    def test_change_color(self):
        tag = Tag(1, 'tag1', 'red', self.user)
        tag_invented = Tag(56, 'fdfdf', 'red', self.user)
        self.assertEqual(self.controller.change_color(tag, 'blue'), True)
        tag.color = 'blue'
        self.assertEqual(self.controller.change_color(tag, 'blue'), 1)
        tag.color = 'green'
        self.assertEqual(self.controller.change_color(tag, 'yellow'), 1)
        self.assertEqual(self.controller.change_color(tag, ''), 1)
        self.assertEqual(self.controller.change_color(tag_invented, 'green'), 0)
        tag.user.id = "fdf"
        self.assertEqual(self.controller.change_color(tag, 'blue'), 1)
    
    def test_delete_by_color(self):
        self.assertEqual(self.controller.delete_by_color('red', self.user.id), True)
        self.assertEqual(self.controller.delete_by_color('red', self.user.id), 0)
        self.assertEqual(self.controller.delete_by_color('redxx', self.user.id), 1)
        self.assertEqual(self.controller.delete_by_color('red', "self.user.id"), 1)

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

    conn.commit()
    conn.close()

if __name__ == '__main__':
    unittest.main()
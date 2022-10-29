import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from tag import Tag
sys.path.insert(1, 'Src/Controller/')
from tag_controller import TagController

class TestTagController(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = TagController()

    def setUp(self):
        restore()
    
    def tearDown(self):
        restore()
    
    def test_add_tag(self):
        tag = Tag('tag3', 'orange')
        self.assertEqual(self.controller.add(tag), True)
        self.assertEqual(self.controller.add(tag), 0)

    #-------------------------Name-------------------------------

    def change_name(self):
        self.assertEqual(self.controller.change_name('tag1', 'tag4'), True)
        self.assertEqual(self.controller.change_name('tag4', 'tag4'), 1)
        self.assertEqual(self.controller.change_name('tag1', 'tag7'), 0)

    def test_delete_by_name(self):
        self.assertEqual(self.controller.delete_by_name('tag1'), True)
        self.assertEqual(self.controller.delete_by_name('tag1'), 0)
        self.assertEqual(self.controller.delete_by_name('tag1xx'), 0)

    #-------------------------Color-------------------------------

    def test_get_by_color(self):
        self.assertEqual(self.controller.get_by_color('red'), [{'name': 'tag1', 'color': 'red'}])
        self.assertEqual(self.controller.get_by_color('blue'), [{'name': 'tag2', 'color': 'blue'}])
        self.assertEqual(self.controller.get_by_color('green'), [])
        self.assertEqual(self.controller.get_by_color(''), 1)

    def test_change_color(self):
        tag = Tag('tag1', 'red')
        tag_invented = Tag('fdfdf', 'red')
        self.assertEqual(self.controller.change_color(tag, 'blue'), True)
        tag.color = 'blue'
        self.assertEqual(self.controller.change_color(tag, 'green'), True)
        tag.color = 'green'
        self.assertEqual(self.controller.change_color(tag, 'yellow'), 1)
        self.assertEqual(self.controller.change_color(tag, ''), 1)
        self.assertEqual(self.controller.change_color(tag_invented, 'green'), 0)
    
    def test_delete_by_color(self):
        self.assertEqual(self.controller.delete_by_color('red'), True)
        self.assertEqual(self.controller.delete_by_color('red'), 0)
        self.assertEqual(self.controller.delete_by_color('redxx'), 1)


def restore():
    conn = sqlite3.connect('./DB/to_do_calendar_test.db')
    c = conn.cursor()

    #remove tables
    c.execute("DROP TABLE IF EXISTS task")
    c.execute("DROP TABLE IF EXISTS tag")

    c.execute('''CREATE TABLE task (id integer primary key, name text unique, status integer, tag integer, date text, color text, priority integer)''')


    #create table tag with columns id, name unique, color
    c.execute('''CREATE TABLE tag (id integer primary key, name text unique, color text)''')

    #insert data into table tag
    c.execute("INSERT INTO tag VALUES (1, 'tag1', 'red')")
    c.execute("INSERT INTO tag VALUES (2, 'tag2', 'blue')")
    #insert data into table task
    c.execute("INSERT INTO task VALUES (1, 'task1', 0, 1, '01/01/2022', 'red', 1)")
    c.execute("INSERT INTO task VALUES (2, 'task2', 1, 2, '01/02/2022', 'blue', 2)")

    conn.commit()
    conn.close()  

if __name__ == '__main__':
    unittest.main()
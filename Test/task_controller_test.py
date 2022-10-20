import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from task import Task
sys.path.insert(1, 'Src/Controller/')
from task_controller import TaskController


class TestTaskController(unittest.TestCase):

    def test_add_task(self):
        controller = TaskController()
        task = Task('task3', 1, '01/01/2022', 'red', 1)
        self.assertEqual(controller.add_task(task), True)
        self.assertEqual(controller.add_task(task), 0)
        restore()

    def test_change_name(self):
        self.assertEqual(self.controller.change_name('task1', 'task4'), True)
        self.assertEqual(self.controller.change_name('task4', 'task4'), 1)
        self.assertEqual(self.controller.change_name('task4', 'task7'), 0)
        restore()                

    def test_change_status(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_status(task), True)
        self.task.status = 0
        self.assertEqual(self.controller.change_status(task), True)
        self.task.status = 2
        self.assertEqual(self.controller.change_status(task), 1)
        self.task.status = -1
        self.assertEqual(self.controller.change_status(task), 1)
        self.task.status = 1
        restore()
    
    def test_change_tag(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_tag(task, '2'), True)
        self.assertEqual(self.controller.change_tag(task, '3'), 0)
        restore()

    def test_change_date(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), True)
        self.assertEqual(self.controller.change_date(task, '45/-2/e3'), 1)
        restore()
    
    def test_change_color(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_color(task, 'blue'), True)
        self.assertEqual(self.controller.change_color(task, 'blue'), 0)
        restore()

    def test_change_priority(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_priority(task, 2), True)
        self.assertEqual(self.controller.change_priority(task, 2), 0)
        self.assertEqual(self.controller.change_priority(task, 3), 1)
        self.assertEqual(self.controller.change_priority(task, 0), True)
        self.assertEqual(self.controller.change_priority(task, -1), 1)
        restore()

    def test_delete_by_name(self):
        controller = TaskController()
        self.assertEqual(controller.delete_by_name('task1'), True)
        self.assertEqual(controller.delete_by_name('task1'), 0)
        self.assertEqual(controller.delete_by_name('task1xx'), 0)
        restore()

    def test_delete_by_status(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.delete_by_status(task, 0), True)
        self.assertEqual(self.controller.delete_by_status(task, 0), 0)
        restore()

    def test_delete_by_date(self):
        self.assertEqual(self.controller.delete_by_date('01/01/2022'), True)
        self.assertEqual(self.controller.delete_by_date('01/01/2022'), 0)
        self.assertEqual(self.controller.delete_by_date('111/32/2022'), 0)
        restore()

    def test_delete_task(self):
        task = Task('task1', 0, 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.delete_task(task), True)


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
    c.execute("INSERT INTO task VALUES (2, 'task2', 0, 2, '01/02/2022', 'blue', 2)")

    conn.commit()
    conn.close()  

if __name__ == '__main__':
    unittest.main()
        
    
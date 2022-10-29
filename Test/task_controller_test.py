import sqlite3
import unittest
import sys
sys.path.insert(0, 'Src/')
from task import Task
sys.path.insert(1, 'Src/Controller/')
from task_controller import TaskController


class TestTaskController(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.controller = TaskController()

    def setUp(self):
        restore()
    
    def tearDown(self):
        restore()

    def test_add_task(self):
        task = Task('task3', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.add_task(task), True)
        self.assertEqual(self.controller.add_task(task), 0)

    #-------------------------Name-------------------------------

    def test_change_name(self):
        self.assertEqual(self.controller.change_name('task1', 'task4'), True)
        self.assertEqual(self.controller.change_name('task4', 'task4'), 1)
        self.assertEqual(self.controller.change_name('task1', 'task7'), 0)

    def test_delete_by_name(self):
        self.assertEqual(self.controller.delete_by_name('task1'), True)
        self.assertEqual(self.controller.delete_by_name('task1'), 0)
        self.assertEqual(self.controller.delete_by_name('task1xx'), 0)

    #-------------------------Status-------------------------------

    def test_get_by_status(self):
        self.assertEqual(self.controller.get_by_status(0), [{'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}])
        self.assertEqual(self.controller.get_by_status(1), [{'name': 'task2', 'status': 1, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}])
        self.assertEqual(self.controller.get_by_status(2), 1)
        self.assertEqual(self.controller.get_by_status(-1), 1)

    def test_change_status(self):
        task = Task('task1', 1, '01/01/2022', 'red', 1)
        task_invented = Task('fdfdf', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_status(task, 0), True)
        task.status = 0
        self.assertEqual(self.controller.change_status(task, 1), True)
        task.status = 1
        self.assertEqual(self.controller.change_status(task, 2), 1)
        self.assertEqual(self.controller.change_status(task, -1), 1)
        self.assertEqual(self.controller.change_status(task_invented, 1), 0)

    def test_delete_by_status(self):
        self.assertEqual(self.controller.delete_by_status(0), True)
        self.assertEqual(self.controller.delete_by_status(0), 0)
        self.assertEqual(self.controller.delete_by_status(1), True)
        self.assertEqual(self.controller.delete_by_status(2), 1)
        self.assertEqual(self.controller.delete_by_status(-1), 1)

    #-------------------------Tag-------------------------------

    def test_get_by_tag(self):
        self.assertEqual(self.controller.get_by_tag(1), [{'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}])
        self.assertEqual(self.controller.get_by_tag(2), [{'name': 'task2', 'status': 1, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}])
        self.assertEqual(self.controller.get_by_tag(3), 0)
        self.assertEqual(self.controller.get_by_tag(-1), 0)
        self.assertEqual(self.controller.get_by_tag("sdsd"), 1)
    
    def test_change_tag(self):
        task = Task('task1', 1, '01/01/2022', 'red', 1)
        task_invented = Task('fdfdf', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_tag(task, '2'), True)
        self.assertEqual(self.controller.change_tag(task, '2'), 1)
        self.assertEqual(self.controller.change_tag(task, '3'), 0)
        self.assertEqual(self.controller.change_tag(task_invented, '2'), 0)

    def test_delete_by_tag(self):
        self.assertEqual(self.controller.delete_by_tag(1), True)
        self.assertEqual(self.controller.delete_by_tag(0), 1)
        self.assertEqual(self.controller.delete_by_tag(5), 0)
        self.assertEqual(self.controller.delete_by_tag("dfd"), 1)

    #-------------------------Date-------------------------------

    def test_get_by_date(self):
        self.assertEqual(self.controller.get_by_date('01/01/2022'), [{'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}])
        self.assertEqual(self.controller.get_by_date('01/02/2022'), [{'name': 'task2', 'status': 1, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}])
        self.assertEqual(self.controller.get_by_date('01/03/2022'), [])
        self.assertEqual(self.controller.get_by_date('01/0sd4/sa2022'), 1)
        self.assertEqual(self.controller.get_by_date('51/04/022'), 1)

    def test_change_date(self):
        task = Task('task1', 1, '01/01/2022', 'red', 1)
        task_invented = Task('fdfdf', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), True)
        self.assertEqual(self.controller.change_date(task, '01/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '35/04/2022'), 1)
        self.assertEqual(self.controller.change_date(task, '45/-2/e3'), 1)
        self.assertEqual(self.controller.change_date(task_invented, '01/04/2022'), 0)
    
    def test_delete_by_date(self):
        self.assertEqual(self.controller.delete_by_date('01/01/2022'), True)
        self.assertEqual(self.controller.delete_by_date('01/01/2022'), 0)
        self.assertEqual(self.controller.delete_by_date('111/32/2022'), 1)

    #-------------------------Color-------------------------------

    def test_get_by_color(self):
        self.assertEqual(self.controller.get_by_color('red'), [{'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}])
        self.assertEqual(self.controller.get_by_color('blue'), [{'name': 'task2', 'status': 1, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}])
        self.assertEqual(self.controller.get_by_color('green'), [])
        self.assertEqual(self.controller.get_by_color('red1'), 1)
        self.assertEqual(self.controller.get_by_color('dfdfd'), 1)
    
    def test_change_color(self):
        task = Task('task1', 1, '01/01/2022', 'red', 1)
        task_invented = Task('fdfdf', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_color(task, 'blue'), True)
        self.assertEqual(self.controller.change_color(task, 'blue'), 1)
        self.assertEqual(self.controller.change_color(task, 'left'), 1)
        self.assertEqual(self.controller.change_color(task_invented, 'blue'), 0)

    def test_delete_by_color(self):
        self.assertEqual(self.controller.delete_by_color('red'), True)
        self.assertEqual(self.controller.delete_by_color('red'), 0)
        self.assertEqual(self.controller.delete_by_color('blue'), True)
        self.assertEqual(self.controller.delete_by_color('blue'), 0)
        self.assertEqual(self.controller.delete_by_color('green'), 1)

    #-------------------------Priority-------------------------------

    def test_get_by_priority(self):
        self.assertEqual(self.controller.get_by_priority(1), [{'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}])
        self.assertEqual(self.controller.get_by_priority(2), [{'name': 'task2', 'status': 1, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}])
        self.assertEqual(self.controller.get_by_priority(3), 1)
        self.assertEqual(self.controller.get_by_priority(0), [])
        self.assertEqual(self.controller.get_by_priority(4), 1)

    def test_change_priority(self):
        task = Task('task1', 1, '01/01/2022', 'red', 1)
        task_invented = Task('fdfdf', 1, '01/01/2022', 'red', 1)
        self.assertEqual(self.controller.change_priority(task, 2), True)
        task.priority = 2
        self.assertEqual(self.controller.change_priority(task, 2), 1)
        self.assertEqual(self.controller.change_priority(task, 3), 1)
        self.assertEqual(self.controller.change_priority(task, 0), True)
        self.assertEqual(self.controller.change_priority(task, -1), 1)
        self.assertEqual(self.controller.change_priority(task_invented, 2), 0)

    def test_delete_by_priority(self):
        self.assertEqual(self.controller.delete_by_priority(1), True)
        self.assertEqual(self.controller.delete_by_priority(1), 0)
        self.assertEqual(self.controller.delete_by_priority(2), True)
        self.assertEqual(self.controller.delete_by_priority(2), 0)
        self.assertEqual(self.controller.delete_by_priority(3), 1)


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
        
    
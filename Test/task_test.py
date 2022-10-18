import unittest
import sys
sys.path.insert(1, 'Src/')
from task import Task

class TestTask(unittest.TestCase):

    def test_init(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        self.assertEqual(task.name, 'testing tasks')
        self.assertEqual(task.status, 0)
        self.assertEqual(task.tag, 'TQS')
        self.assertEqual(task.date, '15/11/2022')
        self.assertEqual(task.priority, 0)

    def test_status(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        task.status = 1
        self.assertEqual(task.status, 1)
    
    def test_tag(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        task.tag = 'TQS2'
        self.assertEqual(task.tag, 'TQS2')

    def test_date(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        task.date = '16/11/2022'
        self.assertEqual(task.date, '16/11/2022')

    def test_color(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        task.color = '#FF0000'
        self.assertEqual(task.color, '#FF0000')

    def test_priority(self):
        task = Task('testing tasks', tag='TQS', date='15/11/2022', color=None, priority=0)
        task.priority = 1
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.change_priority(2), 2)
        task.remove_priority()
        self.assertEqual(task.priority, 0)

if __name__ == '__main__':
    unittest.main()
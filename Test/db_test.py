import unittest
import sys
sys.path.insert(0, "Src/Model")
from TaskModel import TaskModel

class TestTaskModel(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.model = TaskModel('./DB/to_do_calendar_test.db')
        
    def test_get_all(self):
        self.assertEqual(self.model.get_all(), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}, 
            {'name': 'task2', 'status': 0, 'tag': 2, 'date': '01/02/2022', 'color': 'blue', 'priority': 2}
            ])
    
    def test_get_by_name(self):
        self.assertEqual(self.model.get_by_name('task1'), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}
        ])

        self.assertEqual(self.model.get_by_name('s9d8we'), [])

    
    def test_get_by_tag(self):
        self.assertEqual(self.model.get_by_tag(1), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}
        ])

        self.assertEqual(self.model.get_by_tag(-34), [])
    
    def test_get_by_date(self):
        self.assertEqual(self.model.get_by_date('01/01/2022'), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}
        ])

        self.assertEqual(self.model.get_by_date('01/01/0004'), [])

    def test_get_by_color(self):
        self.assertEqual(self.model.get_by_color('red'), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}
        ])

        self.assertEqual(self.model.get_by_color('left'), [])


    def test_get_by_priority(self):
        self.assertEqual(self.model.get_by_priority(1), [
            {'name': 'task1', 'status': 0, 'tag': 1, 'date': '01/01/2022', 'color': 'red', 'priority': 1}
        ])

        self.assertEqual(self.model.get_by_priority(90), [])

    
if __name__ == '__main__':
    unittest.main()
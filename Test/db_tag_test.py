import unittest
import sys
sys.path.insert(0, "Src/Model")
from tag_model import TagModel

class TestTagDb(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.model = TagModel('./DB/to_do_calendar_test.db')

    def test_get_all(self):
        self.assertEqual(self.model.get_all(), [
            {'name': 'tag1', 'color': 'red'}, 
            {'name': 'tag2', 'color': 'blue'}
        ])

    def test_get_by_name(self):
        self.assertEqual(self.model.get_by_name('tag1'), [
            {'name': 'tag1', 'color': 'red'}
        ])

        self.assertEqual(self.model.get_by_name('s9d8we'), [])

    def test_get_by_color(self):
        self.assertEqual(self.model.get_by_color('red'), [
            {'name': 'tag1', 'color': 'red'}
        ])

        self.assertEqual(self.model.get_by_color('left'), [])

    def test_get_custom(self):
        self.assertEqual(self.model.get_custom('tag1', 'red'), [
            {'name': 'tag1', 'color': 'red'}
        ])

        self.assertEqual(self.model.get_custom('name', 's9d8we'), [])

    
if __name__ == '__main__':
    unittest.main()
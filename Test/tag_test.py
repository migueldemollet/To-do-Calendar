import unittest
import sys
sys.path.insert(1, 'Src/')
from Tag import Tag

class TestTag(unittest.TestCase):
    
    def test_init(self):
        tag = Tag('TQS', color='#FF0000')
        self.assertEqual(tag.name, 'TQS')
        self.assertEqual(tag.color, '#FF0000')

    def test_color(self):
        tag = Tag('TQS', color='#FF0000')
        tag.color = '#00FF00'
        self.assertEqual(tag.color, '#00FF00')

    def test_eq(self):
        tag1 = Tag('TQS', color='#FF0000')
        tag2 = Tag('TQS', color='#FF0000')
        self.assertEqual(tag1, tag2)
        tag2.name = 'TQS2'
        self.assertNotEqual(tag1, tag2)

        

if __name__ == '__main__':
    unittest.main()


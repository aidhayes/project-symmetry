import unittest

# Import the function to be tested
from dev.ui import gen_colors

class TestColorGeneration(unittest.TestCase):

    def test_gen_colors(self):
        # Call the function to generate colors
        result = gen_colors()
        # Add assertions based on expected results
        self.assertIsNotNone(result)
        # Check if the length of the generated list is 100,000
        self.assertEqual(len(result), 100000)
        # Check if each color in the list starts with '#' and is a valid hexadecimal code
        for color in result:
            self.assertTrue(color.startswith('#'))
            self.assertTrue(all(c in '0123456789ABCDEFabcdef' for c in color[1:]))
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()

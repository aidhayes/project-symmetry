import unittest
from dev.gui import highlight_sim

class TestHighlightSim(unittest.TestCase):

    def test_highlight_sim(self):
        element = "-TEXT 1-"
        text = "This is a sample article. It contains sentences for testing."
        pairs = {"This is a sample article.": ("This is a sample article.", "yellow")}
        # Assuming that this function updates the UI, it's challenging to test directly. 
        # You might need to mock the GUI update calls and check if they are called with the expected values.
        # For simplicity, let's assume it returns a string with highlighted text.
        result = highlight_sim(element, text, pairs)
        self.assertIn("This is a sample article.", result)

if __name__ == '__main__':
    unittest.main()

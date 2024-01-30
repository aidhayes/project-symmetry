import unittest
from dev.gui import count_words

class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        article = "This is a sample article. It contains sentences for testing."
        result = count_words(article)
        self.assertEqual(result, 10)  # Replace with the expected word count

if __name__ == '__main__':
    unittest.main()

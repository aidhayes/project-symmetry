import unittest

# Import the functions to be tested
#from dev.gui import languageGetter, textGetter
from dev.gui import languageGetter, textGetter

class TestWikipediaFunctions(unittest.TestCase):

    def test_languageGetter(self):
        # Replace with a valid Wikipedia link
        wiki_link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        result = languageGetter(wiki_link)
        # Add assertions based on expected results
        self.assertIsNotNone(result)
        # Add more assertions as needed

    def test_textGetter(self):
        # Replace with a valid Wikipedia link
        wiki_link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        result = textGetter(wiki_link)
        # Add assertions based on expected results
        self.assertIsNotNone(result)
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()

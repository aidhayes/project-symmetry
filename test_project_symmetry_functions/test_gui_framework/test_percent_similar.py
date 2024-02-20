import unittest
from dev.gui import percent_similar

class TestPercentSimilar(unittest.TestCase):

    def test_percent_similar(self):
        article = "This is a sample article. It contains sentences for testing."
        sim_dict = {"This is a sample article.": ("This is a sample article.", "yellow")}
        result = percent_similar(article, sim_dict)
        self.assertEqual(result, 14.29)  # Replace with the expected similarity percentage

if __name__ == '__main__':
    unittest.main()

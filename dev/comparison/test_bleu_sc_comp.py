import unittest

# Import the function to be tested
from bleu_score import compare

#This line defines a test case class named TestSentenceComparison, 
#which inherits from unittest.TestCase. This class will contain 
#individual test methods.
class TestCompareFunction(unittest.TestCase):

    #Defines a test method named test_compare within the TestCompareFunction class.
    def test_compare(self):
        source_text = "This is a sample source sentence."
        target_text = "This is a sample target sentence."
        colors = ["#FF0000", "#00FF00"]
        similarity_threshold = 0.1  #default similarity

        source_pairs, target_pairs = compare(source_text, target_text, colors, similarity_threshold)

        # Add assertions based on expected results
        self.assertEqual(len(source_pairs), 1)
        self.assertEqual(len(target_pairs), 1)
        # Add more assertions as needed based on your understanding of the expected behavior.

if __name__ == '__main__':
    unittest.main()

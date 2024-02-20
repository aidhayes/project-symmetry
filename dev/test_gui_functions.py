
import unittest
from translation import translate
from dev.gui import percent_similar, highlight_sim, count_words
#from dev.test_gui_functions import percent_similar, highlight_sim, count_words
#from gui import percent_similar, highlight_sim, count_words
from .comparison.bleu_score import compare as bleu   
from .comparison.bert import compare as bert
from nltk.tokenize import sent_tokenize
from .ui.colors import gen_colors
from nltk.tokenize import sent_tokenize
import nltk
import requests
import dev.scraper as scraper
import csv
import sys
import os
from deepl.exceptions import QuotaExceededException
from deepl.exceptions import AuthorizationException
import textwrap


class TestPercentSimilar(unittest.TestCase):

    def test_percent_similar(self):
        article = "This is a sample article. It contains sentences for testing."
        sim_dict = {"This is a sample article.": ("This is a sample article.", "yellow")}
        result = percent_similar(article, sim_dict)
        self.assertEqual(result, 14.29)  # Replace with the expected similarity percentage

    def test_highlight_sim(self):
        element = "-TEXT 1-"
        text = "This is a sample article. It contains sentences for testing."
        pairs = {"This is a sample article.": ("This is a sample article.", "yellow")}
        # Assuming that this function updates the UI, it's challenging to test directly. 
        # You might need to mock the GUI update calls and check if they are called with the expected values.
        # For simplicity, let's assume it returns a string with highlighted text.
        result = highlight_sim(element, text, pairs)
        self.assertIn("This is a sample article.", result)

    def test_count_words(self):
        article = "This is a sample article. It contains sentences for testing." # (In this text, the count_words = 10)"
        result = count_words(article) #call the def count_words() from gui module. 
        self.assertEqual(result, 10)  # Replace with the expected word count

if __name__ == '__main__':
    unittest.main()
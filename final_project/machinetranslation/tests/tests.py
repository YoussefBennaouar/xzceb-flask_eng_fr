import unittest
from translator import english_to_french, french_to_english

class testTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('bonjour'),'hello')

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('hello'),'bonjour')

    def test_for_null_englishToFrench(self):
        self.assertIsNone(english_to_french('hello'),'input is null')

    def test_for_null_frenchToEnglish(self):
        self.assertIsNone(french_to_english('bonjour'),'input is null')

if __name__ == '__main__':
    unittest.main()
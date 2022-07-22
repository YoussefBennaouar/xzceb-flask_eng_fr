import unittest
from translator import englishToFrench, frenchToEnglish

class testTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('bonjour'),'hello')

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('hello'),'bonjour')

    def test_for_null_englishToFrench(self):
        self.assertIsNone(englishToFrench('hello'),'input is null')

    def test_for_null_frenchToEnglish(self):
        self.assertIsNone(frenchToEnglish('bonjour'),'input is null')

if __name__ == '__main__':
    unittest.main()
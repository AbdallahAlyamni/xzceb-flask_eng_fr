import unittest
from machinetranslation.translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello, how are you today?"), "Bonjour, comment vous êtes aujourd'hui?") 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench(" "), None)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"), "Hello, how are you today?") 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertNotEqual(frenchToEnglish(" "), None) 

unittest.main()

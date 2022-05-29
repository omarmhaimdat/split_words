import unittest
import split_words

class TestSplitWords(unittest.TestCase):
    
    def test_split(self):
        x = "hello world"
        y = "helloworld"
        splitted = split_words.split(y)
        self.assertEqual(x, splitted)

if __name__ == '__main__':
    unittest.main()

import unittest
from sentiment import sentiment_analyzer

class TestSentiment(unittest.TestCase):

    def test_add(self) : 
        result = sentiment_analyzer('i feel good').analyze()
        result1 = sentiment_analyzer('i feel bad').analyze()
        result2 = sentiment_analyzer('i feel hungry').analyze()
        
        for word in ['positive', 'great']:
            self.assertIn(word,result)
        self.assertIn('negative',result1)
        self.assertIn('negative',result2)
     


if __name__ == '__main__':
    unittest.main()    
    
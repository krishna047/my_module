import unittest
import cap

class Testcap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_test(text)
        self.assertEqual(result,'Python')

    def test_two_word(self):
        text = 'krishna python'
        result = cap.cap_test(text)
        self.assertEqual(result,'Krishna Python')

if __name__=='__main__':

    unittest.main()
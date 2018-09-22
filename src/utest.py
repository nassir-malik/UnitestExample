import unittest
import Testclass # import class under test

class TestStringMethods(unittest.TestCase):
    #intilize utills class - Accessable to all tests
    utilsClass = Testclass.Utills()

    #Data for test validation - It can be parametrize
    validValues = ('6', 'jumped')

    def test_simpleText(self):
        #Simple text string can be parametrized
        text = "The cow jumped over the möön!."
        retVal = self.utilsClass.processSimpleText(text)
        print(retVal)
        self.assertEqual(retVal, self.validValues)

    def test1_UFT8Text(self):
        #UFT8 string can be parametrized
        text = b'The cow jumped over the m\xc3\xb6\xc3\xb6n!.'
        retVal = self.utilsClass.processUFT8Sentence(text)
        print(retVal)
        self.assertEqual(retVal, self.validValues)

    def test1_Base64Text(self):
        #Base64 string can be parametrized
        text = b'VGhlIGNvdyBqdW1wZWQgb3ZlciB0aGUgbcO2w7ZuIS4='
        retVal = self.utilsClass.processBase64Sentence(text)
        print(retVal)
        self.assertEqual(retVal, self.validValues)

if __name__ == '__main__':
    unittest.main()

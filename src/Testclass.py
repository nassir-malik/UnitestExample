import base64


#Test strings
text = "The cow jumped over the möön!."
text1 = text.encode('utf-8')
text2 = base64.b64encode(bytes(text1))

class Utills:

    #Process Base64 text
    def processBase64Sentence(self, sentence):
        return self.processSimpleText(base64.b64decode(sentence).decode("utf-8"))

    # Process UFT8 text
    def processUFT8Sentence(self, sentence):
        return self.processSimpleText(sentence.decode("utf-8"))

    #Process simple text
    def processSimpleText(self, sentence):
        words = sentence.split()
        largestWord = max(words, key=len)
        wordCount = str(len(words))
        return wordCount, largestWord

##Test to make sure code works
# utilsClass = Utils()
# print(text)
# print(utilsClass.processSimpleText(text))
#
# print(text1)
# print(utilsClass.processUFT8Sentence(text1))
#
# print(text2)
# print(utilsClass.processBase64Sentence(text2))
inputSentence = "I am Python"
pigLatinKey = 'ay'
for word in inputSentence.split():
    firstChar = word[0]  # take the first character of the word
    if len(word) > 1:  # check if the word has more than one character
        word = word[1:] + firstChar + pigLatinKey
    print(word, end=' ')
output:
  I maay ythonPay 

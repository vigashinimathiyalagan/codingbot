sentence = "This is a cat and it has a tail and two eyes"
countOfWords = {}

# Split the sentence into words
words = sentence.split()

# Iterate over each word in the sentence
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in countOfWords:
        countOfWords[word] += 1
    # Otherwise, add the word to the dictionary with a count of 1
    else:
        countOfWords[word] = 1

# Print the unique words and their counts
for word, count in countOfWords.items():
    print(word, ":", count)
    
    output:
      This : 1
is : 1
a : 2
cat : 1
and : 2
it : 1
has : 1
tail : 1
two : 1
eyes : 1

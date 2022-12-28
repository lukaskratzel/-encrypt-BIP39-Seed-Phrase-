import random

# get input
key = input("Input your keys in the following format: \"word, word, word\":\n")
wordList = key.split(", ")
words = []

# get right format
for word in wordList:
    strippedWord = word.strip().lower()
    reducedWord = strippedWord[:4]
    words.append(reducedWord)

lettersToNumbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                    'x': 24, 'y': 25, 'z': 26}

# get unique bit representation of each word
wordsInBits = []
for word in words:
    bitString = ""

    for char in word:
        charInBit = bin(lettersToNumbers[char])[2:]
        while len(charInBit) < 5:
            charInBit = "0" + charInBit
        bitString += charInBit

    if len(word) == 3:
        num = random.randint(27, 31)
        bitString += bin(num)[2:]

    wordsInBits.append(bitString)

# fill up each bitString to 24 length
for bitString in wordsInBits:
    while len(bitString) < 24:
        num = random.randint(0, 1)
        bitString += str(num)

print(wordsInBits)
import enchant
d = enchant.Dict("en_US")
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = input('Enter Text: ')
transAlphabet = {}

def createDict(shift):
    for i in range(0, 26):
        letter = alphabet[i]
        transAlphabet[letter] = alphabet[(i-shift+26) % 26]

def decodeText(text, key):
    real = False
    total = 0
    cipherText = ''
    for letter in text:
        if letter in transAlphabet:
            cipherText = cipherText+transAlphabet[letter]
        else:
            cipherText = cipherText+letter
    t = cipherText.split()
    for word in t:
        if d.check(word) == True:
            real = True
            total = total+1
    if total == len(t):
        print("Key:", key)
        print("Cipher Text:", cipherText)

for i in range(0, 26):
    createDict(i)
    decodeText(text, i)

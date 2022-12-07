import enchant
d = enchant.Dict("en_US")
message = input('Enter Cipher text : ') 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
actualText=''
actualKey=0
no_of_words=len(message.split())
words=[]
for key in range(len(LETTERS)):
   translated = ''
   word=''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num <0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
         word=word+LETTERS[num]
      else:
        if d.check(word):
            words.append(word)
        else:
            words.clear()
        word=''
   if d.check(word):
        words.append(word)
   if len(words)==no_of_words:
        actualText=translated
        actualKey=key
        words.clear()
   print('Plain text with %s: %s' % (key, translated))
print('Actual plain text is %s with key:%s' % (actualKey,actualText))

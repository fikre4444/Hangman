import random_words
word = random_words.get_random_word(3, 7).lower()
wordModifiable = word
wordDashes = len(word) * '-'
images = ['none', 'head', 'body', 'left leg', 'right leg', 'left arm', 'right arm', 'noose', 'beggin not to mess up', 'die']
j = 0
#print(word)
while j < len(images)-1:
    if len(wordModifiable) == 0:
        print("congrats you have won. And the word is '"+word+"'")
        break
    print('word = ', wordDashes, images[j])
    guess = input("guess a letter: ")
    if len(guess) > 0 and guess in wordModifiable:  # the first part of the condition is to check if the person pressed enter (if they pressed enter len(g) would be 0
        print('good')
        index = 0
        while True:   # this part of the loop is to find the index to change a '-' to the letter (used for double occuring letters)
            index = word.index(guess, index)
            if wordDashes[index] == '-':
                break
            index = index + 1
        wordDashes = wordDashes[:index]+guess+wordDashes[index+1:]
        wordModifiable = wordModifiable.replace(guess, '', 1)
    else:
        print('incorrect')
        j += 1
if j == len(images)-1:
    print('die')
    print('game over')
    print("btw the word was '"+word+"'")
        
        
        
    
    

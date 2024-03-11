import random
def get_random_word(s = 1, e = 15):
    words = open('words.txt').read().splitlines()
    while True:
        i = random.randint(0, len(words)-1)
        word = words[i]
        if len(word) >= s and len(word) <= e:
            return word
    


import random
from collections import Counter

someWords = '''monkey square beach highway forest autumn banana sword mountain'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if _name_ =='_main_':
    print('Guess the word!')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterguessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter '))
            except: 
                print('Enter only a letter.  This is Hangman. What are you doing?')
                continue    
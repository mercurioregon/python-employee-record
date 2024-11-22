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
import random

words = ['easy', 'aa' 'beautiful', 'javascript', 'python', 'joy', 'great', 'awesome', 'read', 'reactapp', 'pomegranite', 'element', 'create']
# answer = random.choice(words)
answer = 'apple'
health = 7
print('Hangman. You know how to play, so let\'s get started!')

dashes = ('_' * len(answer)) ##display = ['_'] * len(answer) ## gives you a list of underscores
##print(' '.join(display)) ## joins list items (underscores) into a string
print(dashes) ## a check

answerletters = list(answer)
print(answerletters)## a check

##while health > 0:
guess = input('Okay, we have ' + str(len(answer)) + ' characters, start guessing!')
if guess in answer:
    for char in answer: ##for index, char in enumerate(answer): ## if char == guess: dashes[index] = guess ##
        if char == guess:
            print(char) ##iterate to find correct letter, find() to get index of letter in answer,
            ##then replace it at same index of dashes string using
        else:
            print('_')
else:
    health -= 1
    if healt == 0

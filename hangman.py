import random

words = ['easy', 'aa' 'beautiful', 'javascript', 'python', 'joy', 'great', 'awesome', 'read', 'reactapp', 'pomegranite', 'element', 'create']
answer = random.choice(words)
health = 7
print('Hangman. You know how to play!')
dashes = ('_' * len(answer))
dashes = list(dashes)
answerletters = list(answer)

while health > 0 and '_' in dashes:
    guess = input('Okay, we have ' + str(len(answer)) + ' characters, start guessing!')
    if guess in answer:
        for index, char in enumerate(answer):
            if char == guess:
                dashes[index] = guess
                print(dashes)
                if '_' not in dashes:
                    print('Nice! You won!')
    else:
        health -= 1
        if health == 0:
            print('sorry! but you lost.')
            

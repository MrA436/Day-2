import random
a=random.randint(1,10)
b=int(input('Guess a number between 1 and 10: '))
if a==b:
    print('You win')
else:
    print(f'You lose the number was {a}')
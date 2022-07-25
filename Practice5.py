import random

# Try to find a randomly chosen number between 1 and 100 by guiding it up or down according to the predictions.
random = random.randint(1, 100)
right = int(input('How many guesses do you want?'))
counter = 0
score = 100 / right
while right > 0:
    right -= 1
    counter += 1
    guess = int(input('Please enter your guess: '))
    if guess == random:
        print(
            f'Congratulations, you found the random number on your {counter}th guess. Your score is {(right + 1) * score}')
    elif guess < random:
        print('Up')
    elif guess > random:
        print('Down')
    if right == 0:
        print(f'Unfortunately, you\'ve run out of guesses! The number you were trying to guess was {random}')

# Design a function that prints a user-typed word to the screen the specified time.
def printer():
    word = str(input('Please enter the word you want to print: '))
    time = int(input('How many times do you want to print your word?: '))
    print(word * time)


printer()

# Design a function that converts an unlimited number of parameters sent to it into a list
list = []


def convertList(*args):
    print('You can enter your values to add to list, enter \'q\' for quit. ')
    user_input = 0
    while user_input != 'q':
        user_input = str(input('Enter the value add to list: '))
        if user_input == 'q':
            continue
        list.append(user_input)


convertList()
print(list)

# Find all prime numbers between two numbers entered by the user
primeList = []


def isPrime(num1, num2):
    for num in range(num1, num2 + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeList.append(num)
    print(primeList)


num1 = int(input('Please enter the start value: '))
num2 = int(input('Please enter the end value: '))
isPrime(num1, num2)


# Design the function that finds the exact divisors of the number entered by the user.
def division():
    numbers = []
    number = int(input('Please enter a number: '))
    for i in range(1, number + 1):
        if number % i == 0:
            numbers.append(i)
    print(numbers)


division()

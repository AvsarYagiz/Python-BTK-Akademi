# Check whether a number entered by the user is prime and print it on the screen.
number = int(input('Please enter a number: '))
isPrime = True

if number == 1:
    isPrime = False
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break
if isPrime:
    print(f'The number {number} is a prime number.')
else:
    print(f'The number {number} is not a prime number.')

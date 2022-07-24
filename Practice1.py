# Which of the two numbers entered is the greater?
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
if num1 < num2:
    print(f"The second number {num2} is greater.")
else:
    print(f"The first number {num1} is greater.")

# Get a midterm exam grade (40%) and a final exam grade (60%) from the user and calculate the average.
# If GPA is 50 and above, print 'Passed', otherwise 'Failed'.
midterm = int(input('Please enter your midterm exam result'))
final = int(input('Please enter your final exam result'))
gpa = midterm * 0.40 + final * 0.60
print(f'Your average result is {gpa}')
if gpa >= 50:
    print('Passed')
else:
    print('Failed')

# Print whether the number entered by the user is odd or even
num = int(input('Please enter a number'))
if num % 2 == 0:
    print(f'The number {num} is even.')
else:
    print(f'The number {num} is odd.')

# Print whether an entered number is negative or positive
num = int(input('Please enter a number'))
if num < 0:
    print(f'The number {num} is negative.')
elif num > 0:
    print(f'The number {num} is positive.')
else:
    print(f'The number {num} is zero.')

# Ask the user for the password and email information and check that it is correct.
login = {
    'username': 'samplepassword'
}
username = str(input('Please enter your email or username: '))

if username in login.keys():
    password = str(input('Please enter your password: '))
    if password == login[username]:
        print('You logged in successfully!')
    else:
        print('The password is wrong!')
else:
    print('The username does not exist!')

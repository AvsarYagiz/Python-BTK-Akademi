import datetime

# Check the status of obtaining a driver's license by getting name, age and education information from the user.
# The condition for obtaining a license is to be over the age of 18 and to be at least a high school graduate.


user_info = {}
name = str(input('Please enter your name: '))
age = int(input('Please enter your age: '))
edu = str(input('Please enter your education level (high school, university): '))
user_info[name] = age, edu

if user_info[name][0] >= 18:
    if user_info[name][1].lower() != 'high school' and 'university':
        print(f'Dear {name}, your education level must be at least high school in order to get a driver\'s license.')
    else:
        print(f'Dear {name}, you are eligible to get a driver\'s license')
else:
    print(f'Dear {name}, you must be over the age of 18 to get a driver\'s license.')

# Take a student's midterm and final grade and print a grade in 5 grade system based on their success score
midterm = int(input('Please enter your midterm exam result'))
final = int(input('Please enter your final exam result'))
gpa = midterm * 0.40 + final * 0.60
print(f'Your average result is {gpa}')
if 0 <= gpa <= 24:
    print('0')
elif 25 <= gpa <= 44:
    print('1')
elif 45 <= gpa <= 54:
    print('2')
elif 55 <= gpa <= 69:
    print('3')
elif 70 <= gpa <= 84:
    print('4')
elif 85 <= gpa <= 100:
    print('5')

# Calculate the maintenance period of the vehicle whose first traffic date is taken as an input from the user.
car_date = str(input('Please enter your car\'s first date on traffic (30/06/1998): '))
car_date = car_date.split('/')
car_date = datetime.datetime(int(car_date[2]), int(car_date[1]), int(car_date[0]))
days = (datetime.datetime.now() - car_date).days
if days <= 365:
    print('1. Maintenance period')
elif 365 < days <= 365 * 2:
    print('2. Maintenance period')
elif 365 * 2 < days <= 365 * 3:
    print('3. Maintenance period')
else:
    print('There are 3 maintenance period and you already had them. Congratulations!')
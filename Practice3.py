# Which numbers in the number list are multiples of 3?
numbers = [1, 3, 5, 7, 9, 12, 19, 21]
sum = 0
sum_even = []
i = 0
for number in numbers:
    sum += number
    if number % 2 != 0:
        sum_even.append(number ** 2)
        if number % 3 == 0:
            print(number)
print('*' * 50)

# What is the sum of the numbers in the list?
print(sum)
print('*' * 50)

# Print the square of the odd numbers in the list.
print(sum_even)

# Which of the names of the cities have a maximum of 6 characters?
cities = ['Istanbul', 'Virginia', 'Berlin', 'Paris']
for city in cities:
    if len(city) <= 6:
        print(city)

# What is the sum of the prices of the products?
# Show the products with a maximum price of 5000 units.
products = [
    {'name': 'Samsung S6', 'price': '3000'},
    {'name': 'Samsung S7', 'price': '4000'},
    {'name': 'Samsung S8', 'price': '5000'},
    {'name': 'Samsung S9', 'price': '6000'},
    {'name': 'Samsung S10', 'price': '7000'}
]
sum = 0
for product in products:
    price = int(product['price'])
    sum += price
    if price >= 5000:
        print(product)

print(sum)
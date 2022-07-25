# Print the list of numbers to the screen using the while loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Print all odd numbers in the range of numbers you get the start and end value from the user
start = int(input('Please enter the start value: '))
end = int(input('Please enter the end value: '))
while start <= end:
    if start % 2 != 0:
        print(start)
    start += 1

# Print numbers from 1 to 100 in descending order
i = 100
while i >= 0:
    print(i)
    i -= 1

# Print the 5 numbers you receive from the user in a sequential order
i = 1
tosort = []
while i <= 5:
    num = int(input(f'Please enter the {i}. number: '))
    tosort.append(num)
    i += 1
tosort.sort()
print(tosort)

# Store the information of the products received from the user in a dictionary and print them as names and prices.
quantity = int(input('How many products do you want to add?: '))
products = {}
i = 0
while i < quantity:
    name = str(input('Please enter name of the product: '))
    price = str(input('Please enter price of the product: '))
    products[name] = price
    i += 1

product_list = list(products.items())
i = 0
while i < quantity:
    print(f'Product name: {product_list[i][0]}, Product price: {product_list[i][1]}')
    i += 1

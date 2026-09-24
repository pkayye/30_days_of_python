# Day 2: 30 Days of python programming

#level 1
first_name = 'pkayye'
last_name = 'dorofeev'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Allahabad'
age = 18
year = 2022
is_married = True
is_true = True
is_light_on = False

# Multiple variables on one line
a, b, c = 'Python', 3.9, True

#level 2
# 1. Check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Length of first name
print(len(first_name))

# 3. Compare length of first and last name
print(len(first_name) > len(last_name))
print(len(first_name) == len(last_name))

# 4-11. Arithmetic
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('Total:', total)
print('Diff:', diff)
print('Product:', product)
print('Division:', division)
print('Remainder:', remainder)
print('Exp:', exp)
print('Floor division:', floor_division)

# 12. Circle with radius 30 meters
PI = 3.14
radius = 30
area_of_circle = PI * radius ** 2
circum_of_circle = 2 * PI * radius
print('Area of circle:', area_of_circle)
print('Circumference of circle:', circum_of_circle)

# 12.3 Radius from user input
radius = float(input('Enter radius: '))
area = PI * radius ** 2
print('Area of circle:', area)

# 13. Get user details with input()
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')
print(first_name, last_name, country, age)

# 14. Python reserved words
help('keywords')
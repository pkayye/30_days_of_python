# 1. Different data types
num_int = 10
num_float = 3.14
num_complex = 4 - 4j
name = "pkayye"
is_python_fun = True
fruits = ["apple", "banana", "mango"]
coordinates = (10, 20)
unique_numbers = {1, 2, 3, 4}
person = {"name": "pkayye", "country": "India"}

print(type(num_int))
print(type(num_float))
print(type(num_complex))
print(type(name))
print(type(is_python_fun))
print(type(fruits))
print(type(coordinates))
print(type(unique_numbers))
print(type(person))

# 2. Euclidean distance between (2,3) and (10,8)
x1, y1 = 2, 3
x2, y2 = 10, 8

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)
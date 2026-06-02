# Sort List of Tuples

students = [
    ("Ajit", 75),
    ("Rohit", 90),
    ("Aman", 82)
]

students.sort(key=lambda x: x[1])

print(students)


# Lambda with map()

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x**2, numbers))

print(result)



# Lambda with Filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)



# Lambda with sorted

data = {
    "Ajit": 85,
    "Rohit": 70,
    "Aman": 95
}

result = sorted(data.items(), key=lambda x: x[1])

print(result)
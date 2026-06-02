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
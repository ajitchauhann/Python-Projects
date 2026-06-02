# Sort List of Tuples

students = [
    ("Ajit", 75),
    ("Rohit", 90),
    ("Aman", 82)
]

students.sort(key=lambda x: x[1])

print(students)
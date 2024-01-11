student_info = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Physics', 'English']
}

# Accessing values using keys
print("Student Name:", student_info['name'])    # Output: Student Name: Alice
print("Student Age:", student_info['age'])      # Output: Student Age: 20
print("Student Grade:", student_info['grade'])  # Output: Student Grade: A

# Modifying a value
student_info['age'] = 21

# Adding a new key-value pair
student_info['gender'] = 'Female'

# Iterating through keys and values
print("\nStudent Information:")
for key, value in student_info.items():
    print(f"{key}: {value}")
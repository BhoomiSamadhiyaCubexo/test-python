#Write a Python script that takes input from the user and prints out a message based on the input type.

# Get input from the user

user_input = input("Enter something: ")

if user_input.isdigit():
    print("You entered an integer.")
elif user_input.replace(".", "").isdigit():
    print("You entered a floating-point number.")
else:
    print("You entered a string or something else.")


'''def check_input_type(user_input):
    try:
        # Try converting the input to an integer
        int_value = int(user_input)
        return "You entered an integer: {}".format(int_value)
    except ValueError:
        try:
            # Try converting the input to a floating-point number
            float_value = float(user_input)
            return "You entered a floating-point number: {}".format(float_value)
        except ValueError:
            # If both attempts fail, it's likely a string or something else
            return "You entered a string or something else: {}".format(user_input)

# Get input from the user
user_input = input("Enter something: ")

# Check the type of input and print a corresponding message
result_message = check_input_type(user_input)
print(result_message)'''
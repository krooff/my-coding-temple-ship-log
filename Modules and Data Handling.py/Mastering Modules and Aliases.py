# text_utils.py
def reverse_string(s):
    """Function to reverse a string."""
    return s[::-1]

def capitalize_string(s):
    """Function to capitalize a string."""
    return s.capitalize()

# Import the text_utils module using an alias
import text_utils as tu

# Take user input
input_string = input("Enter a string: ")

# Use the functions from the text_utils module
reversed_string = tu.reverse_string(input_string)
capitalized_string = tu.capitalize_string(input_string)


print(f"Reversed String: {reversed_string}")
print(f"Capitalized String: {capitalized_string}")

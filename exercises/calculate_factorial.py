import sys
import logging

def get_user_input():
    input_string = input("Enter a non-negative integer: ")
    return input_string

        

def process_input(input_string):
    error_msg = ""
    value = None
    try:
        value = int(input_string)
        if value < 0:
            return None, "Number cannot be negative"
        return value, error_msg
    except ValueError as e:
        error_msg = "Number must be an integer"
        return None, error_msg

# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 | number == 1:
        return 1
    else:
        return number * (factorial_recursive(number - 1))

def main():
    print("Factorial Computation Using Recursion")
    input = get_user_input()
    value, error_msg = process_input(input)
    # Call factorial_recursive method
    while value is None:
        print("Invalid value.")
        input = get_user_input()
        value, error_msg = process_input(input)

    factorial = factorial_recursive(value)
    print("The factorial of", value, "is:", factorial)

if __name__ == "__main__":
    main()

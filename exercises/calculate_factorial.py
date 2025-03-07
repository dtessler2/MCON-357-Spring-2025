import sys

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
def factorial_recursive(number, level = 0):
    '''
    Set dummy recursion limit to 900 to allow extra stack frames for python processing, although the real recursion limit is 1000
    '''
    if level >= 900:
        print("Hit recursion limit, ending calculation.")
        return 0, level, "Factorial not calculated because recursion limit hit"
    elif number == 0 or number == 1:
        return 1, level, None
    else:
        factorial, next_level, error_msg = factorial_recursive(number - 1, level + 1)
        return (number * factorial), next_level, error_msg
    
def main():
    print("Factorial Computation Using Recursion")
    print(f"Recursion limit: {sys.getrecursionlimit()}")
    input = get_user_input()
    value, error_msg = process_input(input)
    # Call factorial_recursive method
    while value is None:
        print("Invalid value.")
        input = get_user_input()
        value, error_msg = process_input(input)

    factorial, level, error_msg_2 = factorial_recursive(value, 0)
    if error_msg_2:
        print(error_msg_2)
    else:
        print("The factorial of", value, "is:", factorial)

if __name__ == "__main__":
    main()

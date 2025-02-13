import logging

# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 | number == 1:
        return 1
    else:
        return number * (factorial_recursive(number - 1))


def main():
    print("Factorial Computation Using Recursion")
    try:
        number = int(input("Enter a non-negative integer: "))

        # handle negative input
        while number < 0:
            logging("Invalid input. The number can not be less than 0.")
            number = int(input("Enter a non-negative integer: "))
    except ValueError as e:
        print("Error: ", e)
        exit()
        
    # Call factorial_recursive method
    factorial = factorial_recursive(number)
    print("The factorial of", number, "is:", factorial)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Simple program to add 2 numbers
"""

def add_numbers(num1, num2):
    """Add two numbers and return the result"""
    return num1 + num2


def main():
    """Main function to get user input and display result"""
    print("Simple Number Addition Program")
    print("-" * 30)

    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Calculate sum
        result = add_numbers(num1, num2)

        # Display result
        print(f"\n{num1} + {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()


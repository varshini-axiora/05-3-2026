from typing import List, Union


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> Union[float, str]:
    """
    Divide two numbers.

    Handles division by zero.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float | str: Division result or error message
    """
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def is_even(num: int) -> bool:
    """
    Check whether a number is even.

    Args:
        num (int): Input number

    Returns:
        bool: True if even, False otherwise
    """
    return num % 2 == 0


def factorial(n: int) -> Union[int, str]:
    """
    Calculate factorial of a number.

    Edge Case:
        Factorial is not defined for negative numbers.

    Args:
        n (int): Input number

    Returns:
        int | str: Factorial value or error message
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def square_list(numbers: List[int]) -> List[int]:
    """
    Return list of squares of numbers.

    Args:
        numbers (List[int]): List of integers

    Returns:
        List[int]: List containing squared values
    """
    if not numbers:
        return []

    squares = []
    for num in numbers:
        squares.append(num * num)

    return squares


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.

    Ignores case sensitivity.

    Args:
        text (str): Input string

    Returns:
        bool: True if palindrome, otherwise False
    """
    if not text:
        return False

    text = text.lower()
    return text == text[::-1]


# Main program to test the functions
if __name__ == "__main__":

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))

    print("Is 8 Even?", is_even(8))

    print("Factorial of 5:", factorial(5))

    numbers = [1, 2, 3, 4]
    print("Square List:", square_list(numbers))

    print("Is 'madam' a palindrome?", is_palindrome("madam"))
def factorial(n):
    """
    Compute the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer.

    Raises:
    ValueError: If the input is negative or not an integer.
    RecursionError: If the recursion depth is exceeded.
    """
    # Check if the input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    
    # Check if the input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    try:
        return n * factorial(n - 1)
    except RecursionError:
        raise RecursionError("Recursion depth exceeded. Input is too large.")

# Example usage:
if __name__ == "__main__":
    try:
        print(factorial(0))  # Output: 1
        print(factorial(5))  # Output: 120
        print(factorial(10)) # Output: 3628800
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RecursionError as re:
        print(f"RecursionError: {re}")

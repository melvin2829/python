def generate_fibonacci(n):
    """
    Generate the first n Fibonacci numbers using an iterative approach.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    if n < 0:
        raise ValueError("n should be a non-negative integer")
    
    fibonacci_sequence = []
    
    if n == 0:
        return fibonacci_sequence
    elif n == 1:
        return [0]
    
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate the remaining Fibonacci numbers iteratively
    for i in range(2, n):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    return fibonacci_sequence

# Example usage:
if __name__ == "__main__":
    n_values = [0, 1, 5, 10]
    for n in n_values:
        print(f"The first {n} Fibonacci numbers are: {generate_fibonacci(n)}")
def simple_calculator(a, b, operator):
    """
    Function to perform basic arithmetic operations.
    Args:
        a (float): First number.
        b (float): Second number.
        operator (str): The operator indicating the operation ('+', '-', '*', '/').
    Returns:
        float: The result of the arithmetic operation.
    Raises:
        ZeroDivisionError: If division by zero is attempted.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return a / b
    else:
        raise ValueError('Invalid operator')

# Sample runs to demonstrate the functionality
sample_runs = [
    {'input': 'simple_calculator(10, 5, "+")', 'output': simple_calculator(10, 5, "+")},
    {'input': 'simple_calculator(10, 5, "-")', 'output': simple_calculator(10, 5, "-")},
    {'input': 'simple_calculator(10, 5, "*")', 'output': simple_calculator(10, 5, "*")},
    {'input': 'simple_calculator(10, 5, "/")', 'output': simple_calculator(10, 5, "/")},
    {'input': 'simple_calculator(10, 0, "/")', 'output': 'ZeroDivisionError: Cannot divide by zero'}
]

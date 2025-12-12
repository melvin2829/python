def find_smallest_of_three(a, b, c):
    """
    Function to find the smallest of three numbers.
    Args:
        a (float): First number.
        b (float): Second number.
        c (float): Third number.
    Returns:
        float: The smallest of the three numbers.
    """
    if a <= b and a <= c:
        return a
    elif b <= c:
        return b
    else:
        return c

# Read inputs from the user
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    
    # Find the smallest number
    smallest = find_smallest_of_three(a, b, c)
    
    # Display the result
    print(f"The smallest number is: {smallest}")
except ValueError:
    print("Please enter valid numbers.")

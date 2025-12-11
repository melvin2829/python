def find_largest(a, b, c):
    """
    Function to find the largest of three integers.
    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.
    Returns:
        int: The largest of the three integers.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def test_find_largest():
    """
    Function to test the find_largest function with sample inputs.
    """
    sample_inputs = [
        (1, 2, 3, 3),
        (-1, -2, -3, -1),
        (5, 5, 3, 5),
        (0, 0, 0, 0)
    ]

    for a, b, c, expected in sample_inputs:
        result = find_largest(a, b, c)
        assert result == expected, f"Test failed for input ({a}, {b}, {c}). Expected {expected}, got {result}"
        print(f"Test passed for input ({a}, {b}, {c}). Expected and got {result}")

# Run the tests
test_find_largest()
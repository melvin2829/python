def filter_even_numbers(numbers):
    """
    Filters even numbers from a list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    # Using list comprehension to filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Sample runs
if __name__ == "__main__":
    print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
    print(filter_even_numbers([1, 3, 5]))           # Output: []
    print(filter_even_numbers([]))                  # Output: []

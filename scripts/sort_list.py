def validate_input(input_list):
    """
    Validate the input to ensure it is a list of integers.
    Args:
        input_list (list): The input list to validate.
    Raises:
        ValueError: If the input is not a list of integers.
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    for item in input_list:
        if not isinstance(item, int):
            raise ValueError("All elements in the list must be integers.")


def sort_list(input_list):
    """
    Sort the input list in ascending and descending order.
    Args:
        input_list (list): The list of integers to sort.
    Returns:
        tuple: A tuple containing two lists - one sorted in ascending order and the other in descending order.
    """
    # Handle edge case: empty list
    if not input_list:
        return [], []
    ascending_order = sorted(input_list)
    descending_order = sorted(input_list, reverse=True)
    return ascending_order, descending_order


def main():
    """
    Main function to demonstrate the usage of validate_input and sort_list functions.
    """
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    validate_input(input_list)
    ascending, descending = sort_list(input_list)
    print("Ascending order:", ascending)
    print("Descending order:", descending)


if __name__ == "__main__":
    main()
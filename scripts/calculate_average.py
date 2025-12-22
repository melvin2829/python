def calculate_average(num1, num2, num3):
    """
    Calculate the average of three numbers.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        num3 (float): The third number.
    
    Returns:
        float: The average of the three numbers.
    """
    # Calculate the sum of the three numbers
    total_sum = num1 + num2 + num3
    
    # Calculate the average
    average = total_sum / 3
    
    return average

# Sample runs to demonstrate the code's functionality
if __name__ == "__main__":
    sample_runs = [
        {
            "input": "calculate_average(1, 2, 3)",
            "output": calculate_average(1, 2, 3)
        },
        {
            "input": "calculate_average(-1, -2, -3)",
            "output": calculate_average(-1, -2, -3)
        },
        {
            "input": "calculate_average(0, 0, 0)",
            "output": calculate_average(0, 0, 0)
        },
        {
            "input": "calculate_average(1.5, 2.5, 3.5)",
            "output": calculate_average(1.5, 2.5, 3.5)
        }
    ]
    
    # Print sample runs
    for run in sample_runs:
        print(f"Input: {run['input']}, Output: {run['output']}")
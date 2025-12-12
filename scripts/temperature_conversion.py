def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Args:
        celsius (float): Temperature in Celsius.
    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

# Sample runs
if __name__ == "__main__":
    temp_celsius = 25
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius} Celsius is {temp_fahrenheit} Fahrenheit")

    temp_fahrenheit = 77
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit} Fahrenheit is {temp_celsius} Celsius")

    temp_celsius = -40
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius} Celsius is {temp_fahrenheit} Fahrenheit")

import pytest
from your_module import add_numbers  # Replace 'your_module' with the actual module name

def test_add_numbers():
    # Test cases based on the examples and edge cases
    assert add_numbers(3, 5) == 8
    assert add_numbers(-3, -5) == -8
    assert add_numbers(3, -5) == -2
    assert add_numbers(0, 0) == 0
    assert add_numbers(3, 0) == 3
    assert add_numbers(-3, 0) == -3
    assert add_numbers(0, 5) == 5
    assert add_numbers(0, -5) == -5
    assert add_numbers(5, -3) == 2
    assert add_numbers(-5, 3) == -2

if __name__ == "__main__":
    pytest.main()
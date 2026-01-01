import pytest

# Assuming the is_prime function is defined in a module named prime_module
from prime_module import is_prime

@pytest.mark.parametrize("number, expected", [
    (-1, False),  # Negative number, should return false
    (0, False),   # Zero, should return false
    (1, False),   # One, should return false
    (2, True),    # Smallest prime number, should return true
    (3, True),    # Small prime number, should return true
    (4, False),   # Small non-prime number, should return false
    (17, True),   # Prime number, should return true
    (18, False),  # Non-prime number, should return false
    (19, True),   # Prime number, should return true
    (20, False),  # Non-prime number, should return false
    (104729, True),  # Large prime number, should return true
    (104730, False)  # Large non-prime number, should return false
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected

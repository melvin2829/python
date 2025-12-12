import math

def get_primes_up_to_n(n):
    """
    Function to return all prime numbers up to a given number n.
    Args:
        n (int): The upper limit to find prime numbers.
    Returns:
        list: A list of prime numbers up to n.
    """
    if n < 2:
        return []
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# Sample runs
if __name__ == "__main__":
    print(get_primes_up_to_n(10))  # Expected output: [2, 3, 5, 7]
    print(get_primes_up_to_n(2))   # Expected output: [2]
    print(get_primes_up_to_n(20))  # Expected output: [2, 3, 5, 7, 11, 13, 17, 19]
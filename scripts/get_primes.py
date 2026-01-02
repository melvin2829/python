def get_primes(n):
    """Return a list of all prime numbers up to a given number n."""
    if n < 2:
        return []
    
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes

# Example usage:
# print(get_primes(10))  # Output: [2, 3, 5, 7]
# print(get_primes(0))   # Output: []
# print(get_primes(1))   # Output: []
# print(get_primes(2))   # Output: [2]
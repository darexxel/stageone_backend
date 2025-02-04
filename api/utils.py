# utils.py

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n: int) -> bool:
    """
    Return True if n is a perfect number, i.e., if the sum of its proper divisors equals n.
    """
    if n < 2:
        return False
    total = 1  # 1 is always a divisor (for n > 1)
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total == n

def is_armstrong(n: int) -> bool:
    """
    Return True if n is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    For negative numbers, the check is performed on their absolute value.
    """
    abs_n = abs(n)
    digits = str(abs_n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == abs_n

def digit_sum(n: int) -> int:
    """Return the sum of the digits of n. Works correctly even if n is negative."""
    return sum(int(d) for d in str(abs(n)))

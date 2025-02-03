def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(d) ** power for d in num_str)

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_digit_sum(n):
    return sum(int(d) for d in str(n))

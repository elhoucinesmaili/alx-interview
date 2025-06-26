#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Return a list where index i is True if i is prime."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
    return sieve

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each n
    primes_count = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if is_prime[i]:
            count += 1
        primes_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

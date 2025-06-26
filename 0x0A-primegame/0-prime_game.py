#!/usr/bin/python3
"""Prime Game module"""


def isWinner(x, nums):
    """Determines the winner of the prime game.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = count_primes_up_to(n, primes)
        if prime_count % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Generates a list indicating prime status up to n
    using Sieve of Eratosthenes"""
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def count_primes_up_to(n, primes):
    """Counts how many prime numbers are ≤ n using precomputed sieve"""
    return sum(primes[0:n + 1])

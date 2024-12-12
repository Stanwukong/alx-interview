#!/usr/bin/python3
"""Prime game."""


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def play_round(n):
    """
    Play a single round of the Prime Game.
    """
    numbers = set(range(1, n + 1))

    is_maria_turn = True

    while True:
        curr_primes = [p for p in numbers if is_prime(p)]

        if not curr_primes:
            return 'Ben' if is_maria_turn else 'Maria'

        prime = min(curr_primes)
        numbers = {num for num in numbers if num % prime != 0}

        is_maria_turn = not is_maria_turn


def isWinner(x, nums):
    """
    Calculates the winner of a prime game session
    with x rounds
    """
    if not nums or x == 0:
        return None

    nums = nums[:x]

    maria_wins = sum(play_round(n) == 'Maria' for n in nums)
    ben_wins = sum(play_round(n) == 'Ben' for n in nums)

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

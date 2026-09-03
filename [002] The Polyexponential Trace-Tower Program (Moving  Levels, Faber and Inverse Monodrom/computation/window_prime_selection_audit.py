#!/usr/bin/env python3
"""Exact audit of the q=1 window-prime selection criterion.

For every odd m in [7, bound], including prime degree endpoints, test the
largest prime p<m.  If the
residual trace derivative P'_{1,m-p} is not square-free modulo p, test the
second-largest prime.  The calculation is entirely in finite fields.

The default bound 1,000,000 is the range used in
WINDOW_PRIME_SELECTION_AUDIT.md.
"""

from __future__ import annotations

import argparse

from sympy import nextprime, primerange


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply_truncated(
    left: list[int], right: list[int], degree: int, prime: int
) -> list[int]:
    result = [0] * (min(degree, len(left) + len(right) - 2) + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > degree:
                break
            if b:
                result[i + j] = (result[i + j] + a * b) % prime
    return result


def remainder(left: list[int], right: list[int], prime: int) -> list[int]:
    left = trim(left[:])
    right = trim(right[:])
    inverse_lead = pow(right[-1], -1, prime)
    while len(left) >= len(right) and any(left):
        factor = left[-1] * inverse_lead % prime
        shift = len(left) - len(right)
        for j, value in enumerate(right):
            left[shift + j] = (left[shift + j] - factor * value) % prime
        trim(left)
    return left


def polynomial_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left = trim(left)
    right = trim(right)
    while any(right):
        left, right = right, remainder(left, right, prime)
    return trim(left)


def derivative(poly: list[int], prime: int) -> list[int]:
    return [(j * poly[j]) % prime for j in range(1, len(poly))]


def trace_derivative(degree: int, prime: int) -> list[int]:
    """Ascending coefficients of P'_{1,degree} modulo prime; prime>degree."""
    ein = [0] * (degree + 1)
    factorial = 1
    for n in range(1, degree + 1):
        factorial = factorial * n % prime
        sign = 1 if n % 2 else -1
        ein[n] = sign * pow(factorial * n % prime, -1, prime) % prime

    power = [1]
    answer: list[int] = []
    for _k in range(1, degree + 1):
        power = multiply_truncated(power, ein, degree, prime)
        answer.append(degree * power[degree] % prime)
    return answer


def square_free(degree: int, prime: int) -> bool:
    poly = trace_derivative(degree, prime)
    return len(polynomial_gcd(poly, derivative(poly, prime), prime)) == 1


def audit(bound: int) -> None:
    # Include the first prime above the bound without relying on a fixed
    # numerical cushion.
    prime_ceiling = int(nextprime(bound))
    primes = list(primerange(2, prime_ceiling + 1))
    first_failures: list[tuple[int, int, int]] = []
    second_failures: list[tuple[int, int, int, int, int]] = []
    largest_residual = 0

    for index, prime in enumerate(primes[:-1]):
        if prime < 5 or prime > bound:
            continue
        next_prime = primes[index + 1]
        # Include next_prime itself: at a prime degree it is the right-hand
        # endpoint of the current gap, and `prime` is still the largest
        # prime strictly below the degree.
        for degree in range(prime + 2, min(next_prime + 1, bound + 1), 2):
            if not (degree + 1 < 2 * prime < 2 * degree):
                raise AssertionError("nearest prime is outside the strict window")
            residual = degree - prime
            largest_residual = max(largest_residual, residual)
            if square_free(residual, prime):
                continue

            first_failures.append((degree, prime, residual))
            previous_prime = primes[index - 1]
            if not (degree + 1 < 2 * previous_prime < 2 * degree):
                raise AssertionError("fallback prime is outside the strict window")
            previous_residual = degree - previous_prime
            if not square_free(previous_residual, previous_prime):
                second_failures.append(
                    (degree, prime, residual, previous_prime, previous_residual)
                )

    print(f"BOUND={bound}")
    print(f"LARGEST_NEAREST_RESIDUAL={largest_residual}")
    print(f"NEAREST_PRIME_FAILURES={first_failures}")
    print(f"TWO_PRIME_FAILURES={second_failures}")
    print("SELECTION_AUDIT=" + ("PASS" if not second_failures else "FAIL"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=1_000_000)
    arguments = parser.parse_args()
    if arguments.bound < 7:
        raise ValueError("--bound must be at least 7")
    audit(arguments.bound)


if __name__ == "__main__":
    main()

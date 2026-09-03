#!/usr/bin/env python3
"""Exact finite-field certificates for the Bertrand-prime trace criterion.

For each odd m in the requested range, this finds a prime

    (m+1)/2 < p < m,       r = m-p,

for which P'_{q,r} is square-free over GF(p).  The accompanying research
note proves that such a witness forces a unique p-adically isolated simple
critical value of P_{q,m}, and hence geometric monodromy S_m.

Only exact modular arithmetic is used.  The default q=1 certifies the
original Ein trace tower.
"""

from __future__ import annotations

import argparse
import bisect

from sympy import primerange, symbols
from sympy.polys import Poly
from sympy.polys.polytools import gcd


X = symbols("X")


def convolve_truncated(
    left: list[int], right: list[int], degree: int, prime: int
) -> list[int]:
    result = [0] * (degree + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j in range(min(len(right), degree + 1 - i)):
            b = right[j]
            if b:
                result[i + j] = (result[i + j] + a * b) % prime
    return result


def trace_derivative_coefficients(
    degree: int, prime: int, order: int
) -> list[int]:
    """Ascending coefficients of P'_{q,degree} in GF(prime)[X]."""
    ein = [0] * (degree + 1)
    factorial = 1
    for n in range(1, degree + 1):
        factorial = factorial * n % prime
        denominator = factorial * pow(n, order, prime) % prime
        sign = 1 if n % 2 else -1
        ein[n] = sign * pow(denominator, -1, prime) % prime

    power = [1] + [0] * degree
    coefficients: list[int] = []
    for k in range(1, degree + 1):
        power = convolve_truncated(power, ein, degree, prime)
        coefficients.append(degree * power[degree] % prime)
    return coefficients


def residual_is_square_free(degree: int, prime: int, order: int) -> bool:
    coefficients = trace_derivative_coefficients(degree, prime, order)
    residual = Poly.from_list(
        list(reversed(coefficients)), gens=X, modulus=prime
    )
    return gcd(residual, residual.diff()).degree() == 0


def certify(maximum: int, order: int, prime_trials: int) -> None:
    primes = list(primerange(2, maximum + 1))
    certified = 0
    largest_residual_degree = 0
    largest_trials_used = 0

    # Degrees <=5 have independent exact certificates in the main trace note.
    for m in range(7, maximum + 1, 2):
        upper = bisect.bisect_left(primes, m)
        lower = bisect.bisect_right(primes, (m + 1) // 2)
        candidates = list(reversed(primes[lower:upper]))
        witness = None
        for trial, prime in enumerate(candidates[:prime_trials], start=1):
            residual_degree = m - prime
            if residual_is_square_free(residual_degree, prime, order):
                witness = (prime, residual_degree, trial)
                break
        if witness is None:
            raise RuntimeError(
                f"no witness for m={m} among the first "
                f"{min(prime_trials, len(candidates))} Bertrand primes"
            )
        certified += 1
        largest_residual_degree = max(largest_residual_degree, witness[1])
        largest_trials_used = max(largest_trials_used, witness[2])

    print(f"order q={order}")
    print(f"certified odd degrees: 7 <= m <= {maximum}")
    print(f"number of certified degrees: {certified}")
    print(f"largest residual degree r: {largest_residual_degree}")
    print(f"largest number of prime trials used: {largest_trials_used}")
    print("status: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=20_000)
    parser.add_argument("--order", type=int, default=1)
    parser.add_argument("--prime-trials", type=int, default=12)
    args = parser.parse_args()
    if args.max_m < 7:
        raise ValueError("--max-m must be at least 7")
    if args.order < 1:
        raise ValueError("--order must be positive")
    certify(args.max_m, args.order, args.prime_trials)


if __name__ == "__main__":
    main()

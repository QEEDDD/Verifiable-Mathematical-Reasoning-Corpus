#!/usr/bin/env python3
"""Verify mod-409 arithmetic and geometric monodromy certificates.

The calculation is entirely in GF(409).  Because 409>401, the rational
coefficients of every P_m used below have good reduction.  The convolution
arrays stay below int64 overflow before each modular reduction.
"""

from __future__ import annotations

import argparse
import numpy as np
from sympy.polys.domains import GF
from sympy.polys.euclidtools import dup_resultant


PRIME = 409
MAX_M = 401
WITNESSES = {81: 0, 121: 4, 169: 0, 225: 3, 289: 0, 361: 3}


def ein_power_table() -> np.ndarray:
    ein = np.zeros(MAX_M + 1, dtype=np.int64)
    factorial = 1
    for n in range(1, MAX_M + 1):
        factorial = factorial * n % PRIME
        sign = -1 if n % 2 == 0 else 1
        ein[n] = sign * pow(n * factorial % PRIME, -1, PRIME) % PRIME

    powers = np.zeros((MAX_M + 1, MAX_M + 1), dtype=np.int64)
    powers[0, 0] = 1
    for k in range(1, MAX_M + 1):
        powers[k, :] = (
            np.convolve(powers[k - 1, :], ein)[: MAX_M + 1] % PRIME
        )
    return powers


def trace_coefficients(m: int, powers: np.ndarray) -> list[int]:
    coefficients = [0] * (m + 1)  # ascending order
    for k in range(1, m + 1):
        coefficients[k] = (
            m * pow(k, -1, PRIME) * int(powers[k, m]) % PRIME
        )
    return coefficients


def discriminant_at(m: int, value: int, powers: np.ndarray) -> int:
    coefficients = trace_coefficients(m, powers)
    derivative_descending = [
        i * coefficients[i] % PRIME for i in range(m, 0, -1)
    ]
    specialized = coefficients.copy()
    specialized[0] = -value % PRIME
    resultant = int(
        dup_resultant(
            list(reversed(specialized)), derivative_descending, GF(PRIME)
        )
    ) % PRIME
    sign = -1 if (m * (m - 1) // 2) % 2 else 1
    return sign * resultant % PRIME


def opposite_character_witnesses(
    m: int, powers: np.ndarray
) -> tuple[int, int]:
    """Return regular t_plus,t_minus with Legendre characters +1,-1."""
    found: dict[int, int | None] = {1: None, PRIME - 1: None}
    for value in range(PRIME):
        discriminant = discriminant_at(m, value, powers)
        if discriminant == 0:
            continue
        character = pow(discriminant, (PRIME - 1) // 2, PRIME)
        if character in found and found[character] is None:
            found[character] = value
        if found[1] is not None and found[PRIME - 1] is not None:
            return int(found[1]), int(found[PRIME - 1])
    raise RuntimeError(f"no opposite-character pair found for m={m}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--all-odd",
        action="store_true",
        help="verify opposite-character pairs for every odd 57<=m<=401",
    )
    args = parser.parse_args()
    powers = ein_power_table()
    for m, value in WITNESSES.items():
        discriminant = discriminant_at(m, value, powers)
        legendre = pow(discriminant, (PRIME - 1) // 2, PRIME)
        assert discriminant != 0 and legendre == PRIME - 1
        print(f"m={m}, t={value}, disc={discriminant}, Legendre=-1")
    if args.all_odd:
        for m in range(57, MAX_M + 1, 2):
            plus, minus = opposite_character_witnesses(m, powers)
            print(f"m={m}, t_plus={plus}, t_minus={minus}")


if __name__ == "__main__":
    main()

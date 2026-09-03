#!/usr/bin/env python3
"""Exact finite-field checks used in ODD_TRACE_MODP_ROUTE.md.

The main certificate closes the exceptional row m=27 in the window-prime
audit.  The progression q == 1075 (mod 1584) occupies seven classes modulo
28; each class has opposite nonzero discriminant/resultant characters at
two regular specializations modulo 29.
"""

from __future__ import annotations

import math

import sympy as sp


X, T = sp.symbols("X T")


def trace_polynomial_mod(q: int, m: int, p: int) -> sp.Poly:
    """Return P_{q,m}(X) modulo p, assuming p > m."""
    if p <= m or not sp.isprime(p):
        raise ValueError("this routine requires a prime p > m")

    e = [0]
    for n in range(1, m + 1):
        coefficient = (
            (-1) ** (n - 1)
            * pow(int(sp.factorial(n)) % p, -1, p)
            * pow(n % p, -q, p)
        ) % p
        e.append(coefficient)

    power = [1]
    coefficients = [0] * (m + 1)
    for k in range(1, m + 1):
        new_power = [0] * (m + 1)
        for i, a in enumerate(power):
            for j, b in enumerate(e):
                if i + j <= m:
                    new_power[i + j] = (new_power[i + j] + a * b) % p
        power = new_power
        coefficients[k] = (m * pow(k, -1, p) * power[m]) % p

    expression = sum(coefficients[k] * X**k for k in range(m + 1))
    return sp.Poly(expression, X, modulus=p)


def critical_value_resultant(poly: sp.Poly, p: int) -> sp.Poly:
    expression = sp.resultant(poly.diff().as_expr(), poly.as_expr() - T, X)
    return sp.Poly(expression, T, modulus=p)


def quadratic_character(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def certificate_m27() -> None:
    p, m = 29, 27
    progression, period = 1075, 1584
    residues = sorted(
        {
            (progression + k * period) % (p - 1)
            for k in range((p - 1) // math.gcd(period, p - 1))
        }
    )
    assert residues == [3, 7, 11, 15, 19, 23, 27]

    expected = {
        3: ((3, 22), (0, 12)),
        7: ((0, 13), (4, 18)),
        11: ((0, 7), (5, 2)),
        15: ((2, 13), (1, 17)),
        19: ((1, 13), (0, 11)),
        23: ((0, 7), (1, 14)),
        27: ((0, 7), (1, 26)),
    }

    certificates: dict[int, tuple[tuple[int, int], tuple[int, int]]] = {}
    gcd_degrees: dict[int, int] = {}
    for q_residue in residues:
        poly = trace_polynomial_mod(q_residue, m, p)
        resultant = critical_value_resultant(poly, p)
        assert poly.degree() == 27
        assert resultant.degree() == 26
        gcd_degrees[q_residue] = sp.gcd(resultant, resultant.diff()).degree()

        positive: tuple[int, int] | None = None
        negative: tuple[int, int] | None = None
        for t in range(p):
            value = int(resultant.eval(t)) % p
            character = quadratic_character(value, p)
            if character == 1 and positive is None:
                positive = (t, value)
            elif character == -1 and negative is None:
                negative = (t, value)
        assert positive is not None and negative is not None
        certificates[q_residue] = (positive, negative)

    assert certificates == expected
    print(f"m=27, q mod 28 in {residues}, p=29")
    print(f"gcd degrees={gcd_degrees}")
    print(f"opposite-character witnesses={certificates}")


if __name__ == "__main__":
    certificate_m27()

#!/usr/bin/env python3
"""Exact finite-field certificates for the trace-Morse conjecture.

For
    P_m(X) = -m [z^m] log(1-X Ein(z)),
this script searches for a prime p at which

  (i)  the reduction of P_m'(X) is irreducible, and
  (ii) Res_X(P_m'(X), P_m(X)-T) is square-free in F_p[T].

Such a prime is an exact certificate that P_m is Morse in characteristic
zero.  Hence Gal(P_m(X)-T / Q(T)) = S_m.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial

import sympy as sp


X, T = sp.symbols("X T")


def trace_polynomials(max_m: int) -> list[sp.Poly | None]:
    """Return P_0,...,P_max_m, with unused slots set to None."""
    ein = [Fraction(0)] + [
        Fraction((-1) ** (n - 1), n * factorial(n))
        for n in range(1, max_m + 1)
    ]
    powers = [[Fraction(0)] * (max_m + 1) for _ in range(max_m + 1)]
    powers[0][0] = Fraction(1)
    for k in range(1, max_m + 1):
        for n in range(1, max_m + 1):
            powers[k][n] = sum(
                powers[k - 1][n - j] * ein[j] for j in range(1, n + 1)
            )

    result: list[sp.Poly | None] = [None] * (max_m + 1)
    for m in range(1, max_m + 1):
        expression = sum(
            sp.Rational(m * powers[k][m].numerator, k * powers[k][m].denominator)
            * X**k
            for k in range(1, m + 1)
        )
        result[m] = sp.Poly(expression, X, domain=sp.QQ)
    return result


def integral_model(poly: sp.Poly) -> tuple[int, sp.Poly]:
    """Return D and F=D*poly with F integral and D>0."""
    denominator = sp.ilcm(*[int(c.q) for c in poly.all_coeffs()])
    return denominator, sp.Poly(sp.expand(denominator * poly.as_expr()), X, domain=sp.ZZ)


def witness_prime(poly: sp.Poly, lower: int, upper: int) -> int | None:
    denominator, integral = integral_model(poly)
    for p in sp.primerange(lower, upper):
        if denominator % p == 0 or int(integral.LC()) % p == 0:
            continue
        derivative = sp.Poly(integral.diff().as_expr(), X, modulus=p)
        if not derivative.is_irreducible:
            continue
        critical_values = sp.Poly(
            sp.resultant(
                derivative.as_expr(),
                sp.Poly(integral.as_expr() - T, X, T, modulus=p).as_expr(),
                X,
            ),
            T,
            modulus=p,
        )
        if sp.gcd(critical_values, critical_values.diff()).degree() == 0:
            return int(p)
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=20)
    parser.add_argument("--prime-bound", type=int, default=100_000)
    args = parser.parse_args()
    polynomials = trace_polynomials(args.max_m)
    for m in range(4, args.max_m + 1):
        p = witness_prime(polynomials[m], m + 1, args.prime_bound)  # type: ignore[arg-type]
        print(f"{m}\t{p}")


if __name__ == "__main__":
    main()

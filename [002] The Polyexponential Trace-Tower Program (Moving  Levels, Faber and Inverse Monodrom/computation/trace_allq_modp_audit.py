#!/usr/bin/env python3
"""Exact finite-field audit for the all-q trace-monodromy criterion.

For E_q(z)=sum_{n>=1}(-1)^(n-1) z^n/(n! n^q), put

    P_{q,m}(X) = -m [z^m] log(1-X E_q(z)).

If (m+1)/2 < p < m is prime, r=m-p, and P'_{q,r} is squarefree modulo p,
the p-adic isolation lemma in ODD_TRACE_MODP_ROUTE.md produces a simple
isolated critical value of P_{q,m}; hence its geometric monodromy is S_m.
For r<p the reduction depends only on q modulo p-1.  This script searches
for one p that works for every q-residue.

The only composite exceptions through 1001 are m=27 and m=989.  The script
also checks exact patches: for m=27 three strict-window primes leave only
q=1075 mod 1584.  This progression occupies seven order classes modulo 28,
and every one is separated modulo 29 by opposite discriminant characters.
For m=989 the bad residue classes for p=919 and p=929 have empty
simultaneous CRT intersection.

Prime degrees are marked separately; they are covered theoretically by the
prime-degree Newton-polygon theorem, not by this finite search.
"""

from __future__ import annotations

import argparse
import math
from typing import Iterable

import sympy as sp
from sympy.ntheory.modular import solve_congruence


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul_trunc(a: list[int], b: list[int], degree: int, p: int) -> list[int]:
    c = [0] * (min(degree, len(a) + len(b) - 2) + 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            if i + j > degree:
                break
            c[i + j] = (c[i + j] + x * y) % p
    return c


def remainder(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a[:])
    b = trim(b[:])
    inv_lead = pow(b[-1], -1, p)
    while len(a) >= len(b) and any(a):
        factor = a[-1] * inv_lead % p
        shift = len(a) - len(b)
        for j, value in enumerate(b):
            a[shift + j] = (a[shift + j] - factor * value) % p
        trim(a)
    return a


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a)
    b = trim(b)
    while any(b):
        a, b = b, remainder(a, b, p)
    return trim(a)


def derivative(a: list[int], p: int) -> list[int]:
    return [(j * a[j]) % p for j in range(1, len(a))]


def trace_polynomial(q: int, m: int, p: int) -> list[int]:
    """Ascending coefficients of P_{q,m} modulo p; requires p>m."""
    e = [0] * (m + 1)
    factorial = 1
    for n in range(1, m + 1):
        factorial = factorial * n % p
        sign = 1 if n % 2 else -1
        e[n] = sign * pow(factorial, -1, p) * pow(n, -q, p) % p

    power = [1]
    ans = [0] * (m + 1)
    for k in range(1, m + 1):
        power = mul_trunc(power, e, m, p)
        ans[k] = m * pow(k, -1, p) * power[m] % p
    return ans


def trace_derivative(q: int, m: int, p: int) -> list[int]:
    """Ascending coefficients of P'_{q,m} modulo p; requires p>m."""
    return derivative(trace_polynomial(q, m, p), p)


def squarefree_trace_derivative(q: int, r: int, p: int) -> bool:
    if r == 1:
        return True
    f = trace_derivative(q, r, p)
    return len(gcd_poly(f, derivative(f, p), p)) == 1


def uniform_witness(m: int, candidate_count: int = 10) -> tuple[int, int] | None:
    # We use p>(m+1)/2, equivalently r=m-p<=p-2.  The strict endpoint is
    # part of the Newton-polygon isolation lemma.
    primes = list(sp.primerange((m + 3) // 2, m))
    for p in reversed(primes[-candidate_count:]):
        r = m - p
        if all(squarefree_trace_derivative(q, r, p) for q in range(1, p)):
            return p, r
    return None


def bad_residues(m: int, p: int) -> set[int]:
    r = m - p
    return {
        q % (p - 1)
        for q in range(1, p)
        if not squarefree_trace_derivative(q, r, p)
    }


def simultaneous_bad_classes(m: int, primes: Iterable[int]) -> list[tuple[int, int]]:
    """CRT classes that are bad for every prime in ``primes``."""
    solutions = [(0, 1)]
    for p in primes:
        modulus = p - 1
        residues = bad_residues(m, p)
        next_solutions: set[tuple[int, int]] = set()
        for old_residue, old_modulus in solutions:
            for residue in residues:
                answer = solve_congruence(
                    (old_residue, old_modulus), (residue, modulus), check=True
                )
                if answer is not None:
                    next_solutions.add((int(answer[0]), int(answer[1])))
        solutions = sorted(next_solutions)
        if not solutions:
            break
    return solutions


def discriminant_value(q: int, m: int, p: int, t: int) -> int:
    x = sp.symbols("X")
    coeffs = trace_polynomial(q, m, p)
    f = sp.Poly(sum(c * x**j for j, c in enumerate(coeffs)) - t, x, modulus=p)
    return int(sp.discriminant(f)) % p


def legendre(a: int, p: int) -> int:
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def patch_m27() -> dict[str, object]:
    primes = (17, 19, 23)
    bad = [(p - 1, bad_residues(27, p)) for p in primes]
    period = math.lcm(*(modulus for modulus, _ in bad))
    uncovered = [
        q
        for q in range(1, period + 1)
        if all(q % modulus in residues for modulus, residues in bad)
    ]
    progression_residues_mod_28 = sorted(
        {
            (uncovered[0] + k * period) % 28
            for k in range(28 // math.gcd(period, 28))
        }
    )
    character_witnesses: dict[int, tuple[tuple[int, int], tuple[int, int]]] = {}
    for q in progression_residues_mod_28:
        positive: tuple[int, int] | None = None
        negative: tuple[int, int] | None = None
        for t in range(29):
            value = discriminant_value(q, 27, 29, t)
            character = legendre(value, 29)
            if character == 1 and positive is None:
                positive = (t, value)
            elif character == -1 and negative is None:
                negative = (t, value)
        if positive is None or negative is None:
            raise SystemExit(f"m=27 mod-29 character patch failed at q={q}")
        character_witnesses[q] = (positive, negative)
    return {
        "bad_sets": bad,
        "period": period,
        "uncovered": uncovered,
        "mod29_order_residues": progression_residues_mod_28,
        "mod29_character_witnesses": character_witnesses,
    }


def patch_m989() -> dict[str, object]:
    # Bad residues for p=919 are odd, while those for p=929 are even.
    # Since both periods are even, the simultaneous bad CRT locus is empty.
    primes = (919, 929)
    bad = [(p - 1, bad_residues(989, p)) for p in primes]
    return {
        "bad_sets": bad,
        "simultaneous_bad_classes": simultaneous_bad_classes(989, primes),
    }


def audit(bound: int, candidate_count: int) -> None:
    witnesses: dict[int, tuple[int, int]] = {}
    prime_degrees: list[int] = []
    composite_exceptions: list[int] = []

    for m in range(3, bound + 1, 2):
        witness = uniform_witness(m, candidate_count)
        if witness is not None:
            witnesses[m] = witness
        elif sp.isprime(m):
            prime_degrees.append(m)
        else:
            composite_exceptions.append(m)

    print(f"BOUND={bound}")
    print(f"UNIFORM_BERTRAND_WITNESSES={len(witnesses)}")
    print(f"PRIME_DEGREE_FALLBACK={prime_degrees}")
    print(f"COMPOSITE_EXCEPTIONS={composite_exceptions}")
    print(f"M27_PATCH={patch_m27()}")
    print(f"M989_PATCH={patch_m989() if bound >= 989 else 'NOT_NEEDED'}")

    expected_exceptions = [m for m in (27, 989) if m <= bound]
    if composite_exceptions != expected_exceptions:
        raise SystemExit("Unexpected composite exception list")
    patch = patch_m27()
    if patch["uncovered"] != [1075]:
        raise SystemExit("Unexpected m=27 uncovered residue")
    if patch["mod29_order_residues"] != [3, 7, 11, 15, 19, 23, 27]:
        raise SystemExit("Unexpected m=27 order residues modulo 28")
    if bound >= 989 and patch_m989()["simultaneous_bad_classes"]:
        raise SystemExit("m=989 CRT patch failed")
    print("AUDIT=PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=1001)
    parser.add_argument("--candidate-count", type=int, default=10)
    args = parser.parse_args()
    audit(args.bound, args.candidate_count)


if __name__ == "__main__":
    main()

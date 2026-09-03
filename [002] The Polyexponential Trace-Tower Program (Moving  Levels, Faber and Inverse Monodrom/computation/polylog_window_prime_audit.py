#!/usr/bin/env python3
"""Exact strict-window audit for the polylogarithmic Faber transfer.

For

    Li_tau(z) = z A_tau(z),
    A_tau(z) = sum_{n >= 0} (n + 1)^(-tau) z^n,

the single-spike transfer criterion at a strict-window prime

    (m + 1) / 2 < p < m,    r = m - p,

uses the polynomial

    R_r(X) = r sum_{j=1}^r [z^(r-j)] A_tau(z)^j X^(j-1)

over F_p.  This script searches the strict-window primes in descending
order and records the first one for which gcd(R_r, R_r') = 1.  Every
operation is exact finite-field arithmetic; no floating-point or symbolic
black-box calculation is used.

The frozen audit range is tau in {1, 2, 3, 4} and odd 7 <= m <= 1001.
There are no window exceptions for tau = 1, 2, 3, and the sole exception
for tau = 4 is m = 17.  Any deviation makes the program exit nonzero.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


MINIMUM_DEGREE = 7
FROZEN_BOUND = 1001
TAUS = (1, 2, 3, 4)
EXPECTED_EXCEPTIONS = {1: [], 2: [], 3: [], 4: [17]}


def trim(polynomial: list[int]) -> list[int]:
    """Remove high zero coefficients, retaining one coefficient for zero."""
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def multiply_truncated(
    left: list[int], right: list[int], degree: int, prime: int
) -> list[int]:
    """Multiply ascending coefficient lists in F_prime[z], truncated."""
    result = [0] * (min(degree, len(left) + len(right) - 2) + 1)
    for i, left_coefficient in enumerate(left):
        if left_coefficient == 0:
            continue
        largest_j = min(len(right) - 1, degree - i)
        for j in range(largest_j + 1):
            right_coefficient = right[j]
            if right_coefficient:
                result[i + j] = (
                    result[i + j] + left_coefficient * right_coefficient
                ) % prime
    return result


def derivative(polynomial: list[int], prime: int) -> list[int]:
    """Formal derivative of an ascending coefficient list over F_prime."""
    if len(polynomial) <= 1:
        return [0]
    return trim(
        [(degree * polynomial[degree]) % prime for degree in range(1, len(polynomial))]
    )


def remainder(left: list[int], right: list[int], prime: int) -> list[int]:
    """Polynomial remainder in F_prime[X]."""
    left = trim(left[:])
    right = trim(right[:])
    if right == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    inverse_lead = pow(right[-1], -1, prime)
    while left != [0] and len(left) >= len(right):
        factor = left[-1] * inverse_lead % prime
        shift = len(left) - len(right)
        for index, coefficient in enumerate(right):
            left[shift + index] = (
                left[shift + index] - factor * coefficient
            ) % prime
        trim(left)
    return left


def polynomial_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    """Monic gcd of two polynomials in F_prime[X]."""
    left = trim(left[:])
    right = trim(right[:])
    while right != [0]:
        left, right = right, remainder(left, right, prime)
    inverse_lead = pow(left[-1], -1, prime)
    return [(coefficient * inverse_lead) % prime for coefficient in left]


def polylog_residual_polynomial(tau: int, residual: int, prime: int) -> list[int]:
    """Return ascending coefficients of R_residual over F_prime."""
    if not 2 <= residual <= prime - 2:
        raise ValueError("the residual must satisfy 2 <= r <= p - 2")

    # Only coefficients through z^(r-1) can enter the defining formula.
    a_tau = [
        pow(pow(index + 1, tau, prime), -1, prime)
        for index in range(residual)
    ]
    power = [1]
    result = [0] * residual
    for exponent in range(1, residual + 1):
        power = multiply_truncated(power, a_tau, residual - 1, prime)
        result[exponent - 1] = (
            residual * power[residual - exponent]
        ) % prime

    # The leading coefficient is r, hence nonzero because r < p.
    if len(trim(result[:])) != residual:
        raise AssertionError("R_r unexpectedly lost degree modulo p")
    return result


def gcd_degree(tau: int, residual: int, prime: int) -> int:
    """Degree of gcd(R_r, R_r') over F_prime."""
    polynomial = polylog_residual_polynomial(tau, residual, prime)
    gcd = polynomial_gcd(polynomial, derivative(polynomial, prime), prime)
    return len(gcd) - 1


def primes_through(bound: int) -> list[int]:
    """Return all primes <= bound by an exact Eratosthenes sieve."""
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for candidate in range(2, isqrt(bound) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : bound + 1 : candidate] = b"\x00" * (
                (bound - start) // candidate + 1
            )
    return [number for number in range(2, bound + 1) if sieve[number]]


def strict_window_primes(degree: int, primes: list[int]) -> list[int]:
    """Strict-window primes in descending order."""
    return [
        prime
        for prime in reversed(primes)
        if prime < degree and 2 * prime > degree + 1
    ]


@dataclass(frozen=True)
class Candidate:
    prime: int
    residual: int
    gcd_degree: int


@dataclass(frozen=True)
class TauAudit:
    tau: int
    witnesses: int
    candidate_tests: int
    largest_prime_witnesses: int
    fallbacks: tuple[tuple[int, int, int, int], ...]
    exceptions: tuple[int, ...]
    exception_candidates: tuple[tuple[int, tuple[Candidate, ...]], ...]


def audit_tau(tau: int, bound: int, primes: list[int]) -> TauAudit:
    """Search for the first strict-window witness at every odd degree."""
    witness_count = 0
    candidate_tests = 0
    largest_prime_witnesses = 0
    fallbacks: list[tuple[int, int, int, int]] = []
    exceptions: list[int] = []
    exception_candidates: list[tuple[int, tuple[Candidate, ...]]] = []

    for degree in range(MINIMUM_DEGREE, bound + 1, 2):
        candidates = strict_window_primes(degree, primes)
        if not candidates:
            raise AssertionError(f"no strict-window prime at m={degree}")

        tested: list[Candidate] = []
        witness: Candidate | None = None
        witness_rank = 0
        for rank, prime in enumerate(candidates, start=1):
            residual = degree - prime
            if not 2 <= residual <= prime - 2:
                raise AssertionError(
                    f"strict-window residual check failed at m={degree}, p={prime}"
                )
            degree_of_gcd = gcd_degree(tau, residual, prime)
            candidate = Candidate(prime, residual, degree_of_gcd)
            tested.append(candidate)
            candidate_tests += 1
            if degree_of_gcd == 0:
                witness = candidate
                witness_rank = rank
                break

        if witness is None:
            # In an exceptional row every strict-window prime was tested.
            if len(tested) != len(candidates):
                raise AssertionError("exception search did not exhaust its prime window")
            exceptions.append(degree)
            exception_candidates.append((degree, tuple(tested)))
            continue

        witness_count += 1
        if witness_rank == 1:
            largest_prime_witnesses += 1
        else:
            fallbacks.append(
                (degree, witness.prime, witness.residual, witness_rank)
            )

    return TauAudit(
        tau=tau,
        witnesses=witness_count,
        candidate_tests=candidate_tests,
        largest_prime_witnesses=largest_prime_witnesses,
        fallbacks=tuple(fallbacks),
        exceptions=tuple(exceptions),
        exception_candidates=tuple(exception_candidates),
    )


def format_exception_candidates(
    details: tuple[tuple[int, tuple[Candidate, ...]], ...]
) -> str:
    rows = []
    for degree, candidates in details:
        candidate_text = ", ".join(
            f"(p={item.prime}, r={item.residual}, gcd_degree={item.gcd_degree})"
            for item in candidates
        )
        rows.append(f"{degree}: [{candidate_text}]")
    return "{" + ", ".join(rows) + "}"


def run_audit(bound: int) -> bool:
    primes = primes_through(bound)
    degrees_tested = (bound - MINIMUM_DEGREE) // 2 + 1
    results = [audit_tau(tau, bound, primes) for tau in TAUS]

    print(f"BOUND={bound}")
    print(f"ODD_DEGREES_TESTED_PER_TAU={degrees_tested}")
    print(f"TAUS={list(TAUS)}")
    print("STRICT_WINDOW=(m+1)/2 < p < m")

    matches_expectation = True
    for result in results:
        expected = [
            degree
            for degree in EXPECTED_EXCEPTIONS[result.tau]
            if degree <= bound
        ]
        actual = list(result.exceptions)
        print(f"TAU={result.tau}")
        print(f"  WITNESSES={result.witnesses}")
        print(f"  CANDIDATE_TESTS={result.candidate_tests}")
        print(f"  LARGEST_PRIME_WITNESSES={result.largest_prime_witnesses}")
        print(f"  FALLBACK_WITNESSES={list(result.fallbacks)}")
        print(f"  WINDOW_EXCEPTIONS={actual}")
        print(
            "  EXCEPTION_CANDIDATES="
            + format_exception_candidates(result.exception_candidates)
        )
        if actual != expected:
            matches_expectation = False
            print(f"  EXPECTED_WINDOW_EXCEPTIONS={expected}")

    print("POLYLOG_WINDOW_AUDIT=" + ("PASS" if matches_expectation else "FAIL"))
    return matches_expectation


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Exact strict-window audit for Li_tau Faber residuals."
    )
    parser.add_argument("--bound", type=int, default=FROZEN_BOUND)
    arguments = parser.parse_args()
    if not MINIMUM_DEGREE <= arguments.bound <= FROZEN_BOUND:
        parser.error(
            f"--bound must satisfy {MINIMUM_DEGREE} <= bound <= {FROZEN_BOUND}"
        )
    if arguments.bound % 2 == 0:
        parser.error("--bound must be odd")
    raise SystemExit(0 if run_audit(arguments.bound) else 1)


if __name__ == "__main__":
    main()

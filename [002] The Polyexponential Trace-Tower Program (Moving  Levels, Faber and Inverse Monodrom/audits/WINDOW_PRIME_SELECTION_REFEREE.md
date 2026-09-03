# Hostile referee audit: window-prime selection

## Executive verdict

The mathematical core of `WINDOW_PRIME_SELECTION_AUDIT.md` is sound.  The
integral model, exact discriminant criterion, discriminant-height estimate,
fixed-offset families, and the **DS-conditional** density-one argument all
pass.  The exponents \(15/16\) and \(369/400\) are correctly balanced from
the cited mean-square prime-gap bounds.  None of this proves selection in
every sufficiently large odd degree: the correlated shifted-divisor problem
identified in the note remains open.

The exact \(10^6\) calculation required one audit-time repair.  The original
loop stopped before the upper prime of each prime gap and therefore checked
only odd composite degrees.  The revised loop includes those prime endpoints.
This was an explicit coverage correction, not a change to the finite-field
criterion.  The final verdict below is conditional on the revised full-range
run recorded in Section 7.

| Item | Verdict | Qualification |
|---|---|---|
| \((r!)^2P'_r\in\mathbf Z[X]\) | **PASS** | Composition-by-composition divisibility is valid. |
| \(p\) bad iff \(p\mid\Delta_r\), for \(p>r\) | **PASS** | Degree and scaling are units modulo \(p\). |
| \(\log|\Delta_r|=O(r^2\log r)\) | **PASS if \(\Delta_r\ne0\)** | The displayed formula has one harmless TeX comma typo. |
| Fixed separable residual row gives all but finitely many shifted primes | **PASS** | Strict window is \(p>r+1\). |
| DS-conditional density-one theorem | **PASS** | It remains conditional on all even residual derivatives being separable over \(\mathbf Q\). |
| Exceptional exponent \(15/16\) | **PASS** | Uses the Peck--Maynard \(5/4\) mean-square exponent. |
| Improved exponent \(369/400\) | **PASS** | Uses Stadlmann's \(1.23=123/100\) preprint theorem. |
| Exact window selection for every odd \(7\le m\le10^6\) | **PASS after endpoint repair and full rerun** | The archived source/output hashes must be the revised ones in Section 7. |
| \(q=1\), \(G^{\rm geom}_{1,m}=G^{\rm arith}_{1,m}=S_m\) for \(2\le m\le10^6\) | **PASS when combined with prior theorems** | Even degrees use the prior even-degree theorem; the moving-prime theorem supplies odd degrees. Prime-degree Morse is also an independent fallback. |
| Selection for every sufficiently large odd \(m\) | **OPEN** | Neither the height bound nor prime-gap estimates control the correlated divisibilities. |

## 1. Integral model and exact bad-prime criterion

Differentiation gives

\[
 P'_r(X)=r\sum_{k=1}^r[z^r]E(z)^kX^{k-1}.
\]

For an ordered composition \(n_1+\cdots+n_k=r\), its denominator is

\[
 \prod_i n_i!n_i.
\]

The two divisibilities used in the note are independent and correct:

\[
 \prod_i n_i!\mid r!,\qquad \prod_i n_i\mid r!.
\]

The first is the multinomial integrality statement.  For the second, at
each prime \(\ell\),

\[
 \sum_i v_\ell(n_i)
 =\sum_{a\ge1}\#\{i:\ell^a\mid n_i\}
 \le\sum_{a\ge1}\left\lfloor\frac r{\ell^a}\right\rfloor
 =v_\ell(r!).
\]

Thus every summand becomes integral after multiplication by \((r!)^2\),
and \(F_r=(r!)^2P'_r\in\mathbf Z[X]\).  Since the \(k=r\) term is \(rX^{r-1}\),

\[
 \deg F_r=r-1,\qquad \operatorname{lc}(F_r)=r(r!)^2.
\]

For \(p>r\), both \(r\) and \(r!\) are units modulo \(p\).  Hence reduction
preserves the degree, and scaling \(P'_r\) by \((r!)^2\) does not affect
square-freeness.  The standard discriminant criterion therefore gives

\[
 P'_r\bmod p\text{ non-square-free}
 \Longleftrightarrow p\mid\operatorname{Disc}(F_r).
\]

No hidden denominator prime remains.  The same argument for fixed \(q\)
uses

\[
 \prod_i n_i^q\mid(r!)^q
\]

and correctly yields \((r!)^{q+1}P'_{q,r}\in\mathbf Z[X]\).

## 2. Discriminant height

Coefficientwise absolute domination by \(e^z-1\) gives

\[
 |[z^r]E(z)^k|
 \le \frac{k!S(r,k)}{r!}
 \le \frac{k^r}{r!}.
\]

Consequently each coefficient of \(F_r\) is bounded by

\[
 H_r=r\,r!\,r^r.
\]

Writing \(d=r-1\), the standard inequalities

\[
 |\operatorname{Disc}F_r|\le d^dM(F_r)^{2d-2},
 \qquad M(F_r)\le\|F_r\|_2\le\sqrt r\,H_r
\]

give exactly

\[
 |\Delta_r|\le(r-1)^{r-1}(\sqrt r\,H_r)^{2r-4}.
\]

Since \(\log H_r=O(r\log r)\), this proves
\(\log|\Delta_r|=O(r^2\log r)\).  Also
\(\omega(\Delta_r)\le\log_2|\Delta_r|\).  Both conclusions require
\(\Delta_r\ne0\), as the note states.  In formula (2.3), the source has
`^{,2r-4}`; the comma should simply be deleted.

For fixed \(q\), the claimed height

\[
 H_{q,r}=r(r!)^q r^r
\]

is also correct.  Any density estimate deduced from it should use an
implied constant \(\ll_{q,\varepsilon}\), not one uniform in unbounded \(q\).

## 3. Fixed-offset checks

Direct rational reconstruction gives

\[
 P'_2=2X-\frac12,
\]

and

\[
 P'_4=4X^3-3X^2+\frac{25}{36}X-\frac1{24},\qquad
 \operatorname{Disc}(P'_4)=-\frac{211}{11664}.
\]

For \(r=6\), the numerator factors as

\[
 -4720511048743=-7\cdot41\cdot197\cdot83491237.
\]

These displayed examples are exact.  If \(m=p+r\), the strict window
condition is equivalent to \(p>r+1\).  Thus a fixed even \(r\) with
\(\Delta_r\ne0\) indeed works for all but finitely many eligible primes.

## 4. Conditional density-one argument

Assume DS: \(\Delta_r\ne0\) for every even \(r\ge2\).  In a dyadic block
\([X,2X]\), let \(p<m\) be the largest prime below \(m\), let \(r=m-p\),
and put \(H=X^{5/16}\).  For sufficiently large \(X\), \(r\le H\) makes
\(p\) a strict-window prime.  If \(m\) is exceptional, then
\(p\mid\Delta_r\).  For a fixed \(r\), each prime divisor determines at
most one \(m=p+r\), so

\[
 \#\{m:r\le H,\ p\mid\Delta_r\}
 \ll\sum_{r\le H}r^2\log r
 \ll H^3\log H.
\]

For \(r>H\), summing the number of positions more than \(H\) into each
prime gap gives

\[
 \sum_{p_n\le2X}(g_n-H)_+
 \le H^{-1}\sum_{p_n\le2X}g_n^2.
\]

Using \(\sum_{p_n\le x}g_n^2\ll_\varepsilon x^{5/4+\varepsilon}\), the two
exponents are \(3a\) and \(5/4-a\) for \(H=X^a\).  Their equality gives
\(a=5/16\) and \(3a=15/16\).  The logarithm is absorbed into
\(X^\varepsilon\), and dyadic summation is valid because the resulting
exponent is below one.

With Stadlmann's \(123/100\) in place of \(5/4\), balancing gives

\[
 a=\frac1{4}\frac{123}{100}=\frac{123}{400},\qquad
 3a=\frac{369}{400}.
\]

Thus both displayed exceptional exponents are correct.  The conclusion is
conditional only in the explicitly stated sense: the analytic prime-gap
input is unconditional, while DS is not proved.

## 5. Primary-source check for prime-gap inputs

The cited Maynard manuscript states as Theorem 3.1

\[
 \sum_{p_n\le x}(p_{n+1}-p_n)^2\ll x^{5/4+\varepsilon}.
\]

Its abstract and update explicitly say this reproduces an earlier theorem
of Peck.  Bibliographically, “the Peck--Maynard bound” is therefore better
than presenting it as a new Maynard theorem.  The mathematical citation is
nevertheless valid:

- J. Maynard, [*On the difference between consecutive primes*](https://arxiv.org/abs/1201.1787), Theorem 3.1.

Stadlmann's Theorem 1 states

\[
 \sum_{p_n\le x}(p_{n+1}-p_n)^2\ll_\varepsilon x^{1.23+\varepsilon},
\]

so the note's use of \(123/100\) is exact:

- J. Stadlmann, [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867), Theorem 1.

## 6. Exact finite-field implementation

The arithmetic kernel is correct:

1. `trace_derivative(r,p)` constructs
   \(E(z)\bmod(z^{r+1},p)\); \(p>r\) makes every factorial and \(n\)
   denominator invertible.
2. Repeated truncated convolution returns the ascending coefficients
   \(r[z^r]E(z)^k\) of \(P'_r\).
3. The Euclidean algorithm computes \(\gcd(P'_r,P''_r)\) over
   \(\mathbf F_p\).  A constant gcd is equivalent to square-freeness because
   the leading coefficient \(r\) is nonzero modulo \(p\).

I cross-checked the coefficient arrays and gcd decisions against the
independent SymPy-based implementation in `odd_trace_padic_certify.py`:

| \(p\) | \(r\) | expected | both implementations |
|---:|---:|---|---|
| 211 | 4 | bad, gcd degree 1 | agree |
| 199 | 16 | good | agree |
| 69623 | 26 | bad, gcd degree 1 | agree |
| 69593 | 56 | good | agree |

The monic gcds in the two bad cases are respectively \(X-40\) and
\(X-8582\), agreeing with the note.

### Coverage and strict-window logic

The revised stop value `min(next_prime + 1, bound + 1)` includes the upper
prime endpoint of every gap.  The loop then covers exactly 499,997 odd
degrees from 7 through 999,999, with neither omissions nor duplicates.
For the nearest candidate, an independent enumeration found

\[
 \min(2p-m-1)=2,
\]

so every tested nearest prime satisfies \(p>(m+1)/2\).  In the only two
nearest-prime failures, the fallback primes \(199\) for \(m=215\) and
\(69593\) for \(m=69649\) are also strictly eligible.

**Post-audit hardening.**  Both robustness caveats found here were then
resolved: the production script now asserts strict eligibility for nearest
and fallback primes, and obtains the first prime above the requested bound
dynamically with `nextprime(bound)` rather than a fixed numerical cushion.
These changes do not alter the audited output.

## 7. Full-range rerun and hashes

The initial, pre-repair run reproduced the published failure list but had
`LARGEST_NEAREST_RESIDUAL=112`, revealing the omitted prime endpoints.  A
separate endpoint enumeration checked all 78,495 prime degrees
\(7\le m\le10^6\): their maximum nearest residual was 114 and none had a
nearest-prime failure.

I independently reran the revised source at the full bound; it completed
successfully and matched the archived log byte for byte.  The output is

```text
BOUND=1000000
LARGEST_NEAREST_RESIDUAL=114
NEAREST_PRIME_FAILURES=[(215, 211, 4), (69649, 69623, 26)]
TWO_PRIME_FAILURES=[]
SELECTION_AUDIT=PASS
```

Final archived hashes:

```text
SCRIPT_SHA256=e2eb3b8a14f758d84c0d80a4ed3c0ed11a3cf7eb38e3935960be3122d8fdcbf0
OUTPUT_SHA256=51d3a027e9f0ce42f4918b39058288cdfdf808e25ded994ed009a701bc7c44f5
```

## 8. What follows for \(q=1\) through one million

Once the revised full-range output is archived, the window-prime theorem
applies to every odd \(7\le m\le10^6\).  Together with the already audited
indecomposability input, it gives

\[
 G^{\rm geom}_{1,m}=G^{\rm arith}_{1,m}=S_m
\]

for those odd degrees.  The prior even-degree theorem handles every even
\(m\), while the prime-degree Morse theorem independently handles the odd
prime degrees (and degrees 3 and 5).  Consequently the combined statement

\[
 \boxed{G^{\rm geom}_{1,m}=G^{\rm arith}_{1,m}=S_m
 \quad(2\le m\le10^6)}
\]

really does follow.

This is a group-theoretic conclusion.  The modular window certificate
produces an isolated transposition; it does **not** assert that every
polynomial in this finite rectangle is Morse.

## 9. Exact remaining caveats

1. DS is an infinite characteristic-zero separability hypothesis.  Finite
   residual checks do not prove it.
2. The height estimate bounds how many primes divide one fixed
   \(\Delta_r\); it gives no independence across the correlated values
   \(\Delta_{m-p}\) attached to several primes in one moving window.
3. Even Cramér-scale nearest-prime gaps do not make the crude comparison
   \(p>|\Delta_r|\) effective, because \(r^2\log r\) remains much larger
   than \(\log p\) at \(r\asymp(\log p)^2\).
4. For fixed \(q\), the density-one proof extends with constants depending
   on \(q\).  It is not uniform over all orders.
5. Reduction depends on \(q\bmod(p-1)\), but periodicity alone supplies no
   bound on the set of bad order residues.

### Final referee assessment

After the explicit endpoint repair and matching full rerun, the note is a
valid theorem package: an unconditional exact divisor reduction, a useful
height lemma, a DS-conditional density-one selection theorem, and an exact
\(q=1\) selection theorem through \(10^6\).  It does not close the universal
all-odd selection problem, and the manuscript is correct to leave that gate
open.

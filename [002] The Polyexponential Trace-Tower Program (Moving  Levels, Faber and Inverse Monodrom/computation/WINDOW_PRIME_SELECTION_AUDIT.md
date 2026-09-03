# Window-prime selection for the original trace tower

## Exact divisor reduction, a density-one theorem conditional on derivative separability, and the remaining obstruction

### Verdict

For

\[
 E(z)=\operatorname {Ein}(z)
 =\sum_{n\ge1}\frac{(-1)^{n-1}}{n!n}z^n,
 \qquad
 P_m(X)=-m[z^m]\log(1-XE(z)),
\]

the desired selection statement is

\[
 \tag{W}
 \text{for every sufficiently large odd }m\text{ there is a prime }
 \frac{m+1}{2}<p<m
\]

such that, with (r=m-p), the reduction of (P'_r) is square-free over
\(\mathbf F_p\).

This audit does **not** prove (W).  It does obtain four rigorous advances.

1. The finite-field condition is exactly a shifted prime-divisor avoidance
   problem for one integer discriminant \(\Delta_r\).
2. The integers \(\Delta_r\) satisfy the useful height bound
   \(\log|\Delta_r|=O(r^2\log r)\), whenever they are nonzero.
3. Conditional only on characteristic-zero square-freeness of every even
   residual derivative, (W) holds for a density-one set of odd degrees; the
   exceptional count is \(O_\varepsilon(X^{15/16+\varepsilon})\) up to
   \(X\).
4. Exact computation proves (W) for every odd \(7\le m\le10^6\), using one
   of the two largest eligible primes.  The largest-prime-only strengthening
   is false already at \(m=215\).

The exact all-\(m\) blocker is now clear: one needs uniform control of the
correlated divisibilities

\[
 m-r\mid\Delta_r,
 \qquad m-r\text{ prime},
\]

for several even offsets \(r\) in the same prime window.  Standard
prime-gap estimates alone do not control these shifted discriminant
divisors.

---

## 1. An integral derivative model

Coefficient extraction gives

\[
 P'_r(X)=r\sum_{k=1}^r [z^r]E(z)^kX^{k-1}.             \tag{1.1}
\]

Consider a composition \(n_1+\cdots+n_k=r\).  Its contribution to the
coefficient in (1.1) has denominator

\[
 \prod_{i=1}^k n_i!n_i.
\]

Both factors divide a factorial:

\[
 \prod_i n_i!\mid r!
\]

by integrality of the multinomial coefficient, and

\[
 \prod_i n_i\mid r!.                                  \tag{1.2}
\]

For (1.2), at each prime \(\ell\),

\[
 \sum_i v_\ell(n_i)
 =\sum_{a\ge1}\#\{i:\ell^a\mid n_i\}
 \le\sum_{a\ge1}\left\lfloor\frac r{\ell^a}\right\rfloor
 =v_\ell(r!).
\]

Therefore

\[
 \boxed{F_r(X):=(r!)^2P'_r(X)\in\mathbf Z[X].}         \tag{1.3}
\]

Its degree is \(d=r-1\) and its leading coefficient is \(r(r!)^2\).  Put

\[
 \Delta_r:=\operatorname {Disc}(F_r)\in\mathbf Z.     \tag{1.4}
\]

### Proposition 1.1 -- exact bad-prime criterion

For every prime \(p>r\),

\[
 \boxed{
 P'_r\bmod p\text{ is not square-free}
 \quad\Longleftrightarrow\quad p\mid\Delta_r.}        \tag{1.5}
\]

Indeed, \(p\nmid r(r!)^2\), so degree is preserved and multiplication by
\((r!)^2\) is a unit scaling modulo \(p\).  The usual discriminant
criterion then proves (1.5).

Thus the window-prime problem is not a vague finite-field randomness
question.  It is the precise selection problem

\[
 \exists r\text{ even},\quad 2\le r<\frac{m-1}{2},
 \quad p=m-r\text{ prime},
 \quad p\nmid\Delta_r.                                \tag{1.6}
\]

If \(\Delta_r=0\), that residual degree fails at every good prime.  This is
why characteristic-zero derivative separability is a genuine prerequisite
for any argument that counts the prime divisors of \(\Delta_r\).

---

## 2. A sharp-enough discriminant height bound

Since

\[
 |E(z)|\preceq e^z-1
\]

coefficientwise in absolute value,

\[
 \left|[z^r]E(z)^k\right|
 \le [z^r](e^z-1)^k
 =\frac{k!S(r,k)}{r!}
 \le\frac{k^r}{r!}.                                   \tag{2.1}
\]

Consequently every coefficient of \(F_r\) is at most

\[
 H_r:=r\,r!\,r^r                                      \tag{2.2}
\]

in absolute value.  Mahler's discriminant inequality and
\(M(F_r)\le\|F_r\|_2\le\sqrt r H_r\) give, when
\(\Delta_r\ne0\),

\[
 \boxed{
 |\Delta_r|
 \le (r-1)^{r-1}(\sqrt r\,H_r)^{2r-4}.}              \tag{2.3}
\]

In particular,

\[
 \boxed{\log|\Delta_r|=O(r^2\log r),
 \qquad
 \omega(\Delta_r)=O(r^2\log r).}                     \tag{2.4}
\]

The implied constants are absolute.  Formula (2.4) is the correct useful
scale: a fixed residual row has few bad primes compared with its
discriminant size, even though those primes need not be small.

The same proof works for every fixed polyexponential order \(q\).  Namely,

\[
 (r!)^{q+1}P'_{q,r}\in\mathbf Z[X],
\]

and one may take

\[
 H_{q,r}=r(r!)^q r^r,
 \qquad
 \log|\Delta_{q,r}|=O_q(r^2\log r).                  \tag{2.5}
\]

This is uniform in \(r\), but not in an unbounded order \(q\).

---

## 3. Unconditional shifted-prime families

Fix an even \(r\) for which \(\Delta_r\ne0\).  Proposition 1.1 shows that
only finitely many primes \(p>r+1\) fail.  Therefore

\[
 \boxed{
 m=p+r\text{ satisfies the window criterion for all but finitely many
 primes }p.}                                          \tag{3.1}
\]

This recovers the structural shifted-prime families without any
probabilistic heuristic.  In the first rows,

\[
 P'_2(X)=2X-\frac12,
 \qquad \Delta_2=1,
\]

so every \(m=p+2\) works.  Also

\[
 P'_4(X)=4X^3-3X^2+\frac{25}{36}X-\frac1{24},
\]

\[
 \operatorname {Disc}(P'_4)=-\frac{211}{11664}.       \tag{3.2}
\]

Thus the row \(r=4\) works at every eligible prime except \(p=211\).

There cannot be a bound saying that every bad prime is \(O(r^C)\) for a
small fixed \(C\) on the evidence of the first rows: already

\[
 \operatorname {num}\operatorname {Disc}(P'_6)
 =-7\cdot41\cdot197\cdot83491237.                     \tag{3.3}
\]

Large exceptional primes are genuinely present.

---

## 4. A density-one theorem, conditional on derivative separability

### Hypothesis DS

\[
 \boxed{\Delta_r\ne0\quad\text{for every even }r\ge2.} \tag{DS}
\]

This says only that every even-row derivative \(P'_r\) is square-free in
characteristic zero.  It is much weaker than the Trace--Morse conjecture,
which also requires distinct critical values.

### Theorem 4.1

Assume **DS**.  Let \(\mathcal E(X)\) be the set of odd \(m\le X\) for
which no window prime satisfies (1.5).  Then, for every
\(\varepsilon>0\),

\[
 \boxed{
 \#\mathcal E(X)\ll_\varepsilon X^{15/16+\varepsilon}.} \tag{4.1}
\]

In particular, the window-prime criterion, and hence symmetric geometric
trace monodromy, holds for a density-one set of odd degrees.

### Proof

It is enough to count in a dyadic interval \([X,2X]\).  Let \(p<m\) be
the largest prime below \(m\), and put \(r=m-p\).  Choose

\[
 H=X^{5/16}.                                          \tag{4.2}
\]

If \(r\le H\) and \(m\) is exceptional, then the largest prime is bad,
so Proposition 1.1 gives \(p\mid\Delta_r\).  For a fixed \(r\), every
such prime divisor determines at most one integer \(m=p+r\).  Hence (2.4)
gives

\[
 \#\{m:r\le H,\ p\mid\Delta_r\}
 \ll\sum_{r\le H}r^2\log r
 \ll H^3\log H
 \ll X^{15/16}\log X.                                \tag{4.3}
\]

For the complementary integers, \(m\) lies more than \(H\) places into a
prime gap.  If \(g_n=p_{n+1}-p_n\), their number is at most

\[
 \sum_{p_n\le2X}(g_n-H)_+
 \le\frac1H\sum_{p_n\le2X}g_n^2.                    \tag{4.4}
\]

Maynard's mean-square prime-gap theorem states

\[
 \sum_{p_n\le x}g_n^2\ll_\varepsilon x^{5/4+\varepsilon};
\]

see J. Maynard, [*On the difference between consecutive primes*](https://arxiv.org/abs/1201.1787).
Substitution into (4.4) and (4.2) gives

\[
 X^{5/4+\varepsilon-5/16}=X^{15/16+\varepsilon}.      \tag{4.5}
\]

Equations (4.3)--(4.5), followed by dyadic summation, prove (4.1).
\(\square\)

### Sharper exponent from the current preprint record

Stadlmann proves

\[
 \sum_{p_n\le x}g_n^2\ll_\varepsilon x^{1.23+\varepsilon}
\]

in [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867).
If that preprint theorem is used, balancing the two terms at
\(H=X^{123/400}\) sharpens (4.1) to

\[
 \#\mathcal E(X)\ll_\varepsilon X^{369/400+\varepsilon}. \tag{4.6}
\]

The proof is identical.  The conservative exponent (4.1) uses the older
Maynard--Peck bound.

Theorem 4.1 and (4.6) extend verbatim to each fixed order \(q\), under the
fixed-\(q\) analogue \(\Delta_{q,r}\ne0\) for every even \(r\).

---

## 5. Why this does not prove every degree

The height bound gives the elementary sufficient condition

\[
 p>|\Delta_r|\quad\Longrightarrow\quad p\nmid\Delta_r. \tag{5.1}
\]

By (2.3), (5.1) is guaranteed only when roughly

\[
 r^2\log r\ll\log p.                                  \tag{5.2}
\]

Known pointwise prime-gap bounds are far too weak for (5.2).  More
importantly, even Cramer's conjectural bound \(r=O((\log p)^2)\) for the
nearest-prime gap would not make the crude size comparison (5.1) work:
the allowed discriminant bound would still be exponentially larger than
\(p\).

One therefore needs arithmetic information, not merely a smaller prime
gap.  A counterexample to (W) would be an odd \(m\) for which every prime
\(p\in((m+1)/2,m)\) satisfies

\[
 p\mid\Delta_{m-p}.                                   \tag{5.3}
\]

These are different discriminants at different offsets.  Neither a product
bound for one \(\Delta_r\) nor Bertrand's theorem prevents the correlated
covering (5.3).  Conversely, no such \(m\) is known from the exact search
below.

The largest-prime-only simplification is definitely false.  At

\[
 m=215,
 \qquad p=211,
 \qquad r=4,
\]

(3.2) makes the nearest prime bad; exactly,

\[
 \deg\gcd(P'_4,P''_4)_{\mathbf F_{211}}=1,
 \qquad \gcd\sim X-40.
\]

The next prime \(199\) has residual degree \(16\) and is good.  A second
nearest-prime failure occurs at

\[
 (m,p,r)=(69649,69623,26),
\]

where the modular gcd is proportional to \(X-8582\); the next prime
\(69593\), with residual degree \(56\), is good.

Thus a successful proof must genuinely allow prime selection; it cannot
canonically take the largest prime.

---

## 6. Exact computation through one million

The companion program

* `output/research/window_prime_selection_audit.py`

uses exact convolution and Euclidean gcd arithmetic in finite fields.  It
tests the largest eligible prime and, only when necessary, the second
largest.  The command

```text
python output/research/window_prime_selection_audit.py --bound 1000000
```

returns

```text
BOUND=1000000
LARGEST_NEAREST_RESIDUAL=114
NEAREST_PRIME_FAILURES=[(215, 211, 4), (69649, 69623, 26)]
TWO_PRIME_FAILURES=[]
SELECTION_AUDIT=PASS
```

The audited artifacts have SHA-256 hashes

- `window_prime_selection_audit.py`:
  `e2eb3b8a14f758d84c0d80a4ed3c0ed11a3cf7eb38e3935960be3122d8fdcbf0`;
- `window_prime_selection_audit_1000000.txt`:
  `51d3a027e9f0ce42f4918b39058288cdfdf808e25ded994ed009a701bc7c44f5`.

Therefore

\[
 \boxed{
 \text{the window-prime criterion holds exactly for every odd }
 7\le m\le10^6.}                                     \tag{6.1}
\]

This extends the earlier \(10^5\) audit by one order of magnitude.  It is
a finite theorem, not evidence silently promoted to an asymptotic theorem.

---

## 7. The all-order-\(q\) version

For a fixed \(q\), Sections 1--4 remain valid with \(\Delta_r\) replaced
by \(\Delta_{q,r}\).  For a single prime \(p>r\), reduction depends only
on \(q\bmod(p-1)\), so an all-\(q\) computation is finite at that prime.

However, this periodicity does not supply an asymptotic theorem uniform in
\(q\).  The characteristic-zero height in (2.5) grows with \(q\), and a
prime that is good for one order residue can be bad for another.  Proving
one window prime good for every order residue would require a uniform bound
on the bad-residue sets of

\[
 \operatorname {Disc}(P'_{q,r})\bmod p,
 \qquad q\in\mathbf Z/(p-1)\mathbf Z,                 \tag{7.1}
\]

and no such bound is presently proved.  The family \(r=2\) remains the
clean unconditional exception: its derivative is linear for every \(q\),
so every \(m=p+2\) works simultaneously for all orders.

---

## 8. Referee-status table

| Claim | Status | Reason |
|---|---|---|
| Exact equivalence \(p\) bad \(\Longleftrightarrow p\mid\Delta_r\) | **PROVED** | Integral model (1.3), good reduction |
| \(\log|\Delta_r|=O(r^2\log r)\) | **PROVED when \(\Delta_r\ne0\)** | Coefficient and Mahler bounds |
| All but finitely many primes in each fixed separable residual row work | **PROVED** | A nonzero integer has finitely many prime divisors |
| Selection for all odd \(m\le10^6\), \(q=1\) | **EXACT COMPUTATION** | Finite-field gcd audit |
| Density-one selection for fixed \(q\) | **CONDITIONAL THEOREM** | Requires all even \(P'_{q,r}\) square-free in characteristic zero |
| Selection for every sufficiently large odd \(m\) | **OPEN** | Correlated shifted-discriminant divisor avoidance |
| One prime uniform for every \(q\) and every odd \(m\) | **OPEN, STRONGER** | No uniform control of bad order residues |

### Strongest honest conclusion

The window-prime route is not blocked by the transcendence barriers.  It
has become a concrete arithmetic problem with a strong finite theorem and a
conditional density-one theorem.  What is still missing for an all-degree
closure is not a better generic prime-gap estimate; it is either

1. an all-even derivative-separability theorem plus a pointwise
   shifted-divisor avoidance argument, or
2. a second local Newton polygon that bypasses the bad residual rows.

That is the exact next gate.

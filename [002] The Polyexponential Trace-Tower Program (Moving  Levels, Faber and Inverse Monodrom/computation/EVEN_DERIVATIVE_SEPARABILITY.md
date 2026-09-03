# Even-row derivative separability in the original trace tower

## A dyadic half-separation theorem, prime-shift families, and an exact audit through 5000

### Verdict

Put

\[
 E(z)=\operatorname {Ein}(z)
 =\sum_{n\geq1}\frac{(-1)^{n-1}}{n!n}z^n,
 \qquad
 P_m(X)=-m[z^m]\log(1-XE(z)).
\]

When an all-order statement is made, the notation is

\[
 E_q(z)=\sum_{n\geq1}\frac{(-1)^{n-1}}{n!n^q}z^n,
 \qquad
 P_{q,m}(X)=-m[z^m]\log(1-XE_q(z)),
\]

so that \(E=E_1\) and \(P_m=P_{1,m}\).

The hypothesis under attack is

\[
 \tag{DS}
 P'_r(X)\text{ is square-free over }\mathbf Q
 \quad\text{for every even }r\geq2.
\]

This note does **not** prove DS and finds no counterexample.  It proves
three unconditional substitutes.

1. For every order \(q\geq1\) and every even \(r=2s\), at least \(s\) of
   the \(2s-1\) roots of \(P'_{q,r}\) are simple.  More precisely, an exact
   dyadic reduction isolates all \(s\) unit roots, and any repeated root
   must lie in the strict positive-valuation disk.
2. For every odd prime \(p\), and in fact for every polyexponential order
   \(q\geq1\), the derivative \(P'_{q,p+1}\) is square-free.  Thus DS holds
   on the infinite family \(r=p+1\), containing \(\sim X/\log X\) rows up
   to \(X\).  Two further explicit prime-shift families are obtained below.
3. One exact finite-field computation proves DS for every even
   \(2\leq r\leq5000\), and also proves the polar polynomial \(B_s\)
   square-free for every odd \(1\leq s\leq4999\).  Thus Proposition 4.1
   supplies 2500 rigorously certified fixed-offset prime families.

The obstruction is now sharply local.  Modulo two, the outer half of the
roots is separable, but the inner factor has multiplicity \(s-1\).  Its
later Newton faces can genuinely be inseparable; for example a face for
\(r=10\) has residual polynomial \(1+Y^2\).  A recursive Hensel argument
therefore needs new higher-order information.

---

## 1. Positive-sign normalization and a universal derivative identity

It is convenient to remove alternating signs.  Set

\[
 g(z):=-E(-z)=\sum_{n\geq1}\frac{z^n}{n!n}
\]

and

\[
 H_r(X):=\sum_{k=1}^r [z^r]g(z)^kX^{k-1}.
 \tag{1.1}
\]

Then

\[
 \boxed{
 \frac1rP'_r(X)=(-1)^{r+1}H_r(-X).}
 \tag{1.2}
\]

Consequently \(P'_r\) is square-free if and only if \(H_r\) is.  The
resolvent identity is

\[
 \frac{g(z)}{1-Xg(z)}=\sum_{r\geq1}H_r(X)z^r.
 \tag{1.3}
\]

Differentiating with respect to \(X\) gives the exact convolution

\[
 \boxed{
 H'_r(X)=\sum_{a=1}^{r-1}H_a(X)H_{r-a}(X).}
 \tag{1.4}
\]

This is the second-kind Faber identity in row form.  It is useful for exact
calculation, but it is not a finite three-term recurrence, and a common
zero of \(H_r,H'_r\) is not forced to be a zero of one lower row.

---

## 2. Exact dyadic reduction

For any \(q\geq1\), define the integral dyadic normalization

\[
 c_q:=2^{q+1},
 \qquad
 f_q(z):=\frac{E_q(c_qz)}{c_q},
 \qquad
 \widehat P_{q,r}(X):=c_q^rP_{q,r}(X/c_q).
 \tag{2.1}
\]

The coefficient of \(z^n\) in \(f_q\) has valuation

\[
 v_2([z^n]f_q)
 =q\bigl(n-1-v_2(n)\bigr)+s_2(n)-1.
 \tag{2.2}
\]

It follows that \(f_q\in\mathbf Z_2[[z]]\) and, independently of \(q\),

\[
 \boxed{f_q(z)\equiv z+z^2\pmod2.}
 \tag{2.3}
\]

The derivative coefficient formula is

\[
 \widehat P'_{q,r}(X)
 =r\sum_{k=1}^r[z^r]f_q(z)^kX^{k-1}.
 \tag{2.4}
\]

Let \(r=2s\), let \(a=v_2(r)\), and put

\[
 D_{q,r}(X):=2^{-a}\widehat P'_{q,r}(X)\in\mathbf Z_2[X].
 \tag{2.5}
\]

Since \(r/2^a\) is odd, reduction of (2.4) gives

\[
\begin{aligned}
 \overline D_{q,r}(X)
 &=\sum_{k=s}^{2s}\binom{k}{2s-k}X^{k-1}\\
 &=X^{s-1}
   \sum_{j=0}^{s}\binom{s+j}{s-j}X^j.
\end{aligned}
\tag{2.6}
\]

The quotient in (2.6) has a standard Lucas interpretation.  Over
\(\mathbf F_2\), let

\[
 L_0=0,\qquad L_1=X,\qquad
 L_n=X(L_{n-1}+L_{n-2}).
 \tag{2.7}
\]

Then

\[
 L_{2s+1}(X)
 =X^{s+1}\Lambda_{2s+1}(X),
 \qquad
 \Lambda_{2s+1}(X)
 =\sum_{j=0}^{s}\binom{s+j}{s-j}X^j.
 \tag{2.8}
\]

### Lemma 2.1 -- Lucas quotient separability

For every \(s\geq1\), \(\Lambda_{2s+1}(0)=1\) and
\(\Lambda_{2s+1}\) is square-free over \(\overline{\mathbf F}_2\).

#### Proof

Let \(w,w_*\) be the roots of

\[
 U^2-XU-X=0.
\]

The recurrence gives \(L_n=w^n+w_*^n\).  For \(X\ne0\), put
\(\zeta=w/w_*\).  Then a nonzero root of \(L_n\) corresponds to

\[
 \zeta^n=1,
 \qquad \zeta\ne1,
 \qquad X=\zeta+\zeta^{-1}.
\]

When \(n=2s+1\) is odd, the \(n\)-th roots of unity are simple in
characteristic two.  The only identification in the displayed map is
\(\zeta\leftrightarrow\zeta^{-1}\).  Hence it gives exactly \(s\)
distinct nonzero roots.  Since \(\deg\Lambda_{2s+1}=s\), the quotient is
square-free. \(\square\)

### Theorem 2.2 -- dyadic half-separation

For every \(q\geq1\) and every even \(r=2s\), the polynomial
\(P'_{q,r}\) has at least \(s\) simple roots.  Under the scaling (2.1),
they are exactly the roots of valuation zero reducing to the roots of
\(\Lambda_{2s+1}\).  Every possible repeated root has strictly positive
2-adic valuation.

#### Proof

Equation (2.6) factors the full-degree reduction of \(D_{q,r}\) as

\[
 X^{s-1}\Lambda_{2s+1}(X),
 \qquad \gcd(X,\Lambda_{2s+1})=1.
\]

Each of the \(s\) nonzero residual roots is simple by Lemma 2.1 and hence
has a unique simple Hensel lift.  The remaining factor has degree \(s-1\)
and reduces to \(X^{s-1}\).  Scaling and nonzero scalar multiplication do
not change multiplicities. \(\square\)

An immediate quantitative consequence, uniform in \(q\), is

\[
 \deg\gcd(P'_{q,r},P''_{q,r})\leq \frac r2-1.
 \tag{2.9}
\]

This is not DS: (2.9) still permits repeated roots in the inner disk.

---

## 3. A uniform prime-successor family

The following result is valid for all orders, not only \(q=1\).

### Theorem 3.1

Let \(p\) be an odd prime and \(q\geq1\).  Then

\[
 \boxed{P'_{q,p+1}(X)\text{ is square-free over }\mathbf Q.}
 \tag{3.1}
\]

In particular DS holds for every even row \(r=p+1\).

#### Proof

Write

\[
 A_q(z)=\frac{E_q(z)}z
 =\sum_{n\geq0}
 \frac{(-1)^n}{(n+1)!(n+1)^q}z^n
\]

and, for \(m=p+1\),

\[
 P'_{q,m}(X)=\sum_{j=0}^{p}d_jX^j,
 \qquad
 d_j=m[z^{p-j}]A_q(z)^{j+1}.
 \tag{3.2}
\]

At the prime \(p\), the constant coefficient has valuation \(-1\).  In
\(d_1\), the unique lowest terms are the two copies of
\(a_{p-1}a_0\), so

\[
 v_p(d_0)=-1,
 \qquad v_p(d_1)=-(q+1).
 \tag{3.3}
\]

For \(2\leq j\leq p-1\), every coefficient of \(A_q\) that can occur has
index at most \(p-2\), hence \(v_p(d_j)\geq0\).  Finally
\(d_p=m=p+1\) is a unit.  Thus the derivative Newton polygon has exactly
two edges,

\[
 (0,-1)\longrightarrow(1,-q-1)
 \longrightarrow(p,0).
 \tag{3.4}
\]

The first edge has length one.  After adjoining a uniformizer for the
possibly fractional second slope, its nonzero-root initial form is the
binomial

\[
 u+vY^{p-1}.
\]

It is separable in characteristic \(p\), because \(p\nmid p-1\).  Every
root on both edges is therefore simple. \(\square\)

The rows in (3.1) have counting function \(\pi(X-1)\sim X/\log X\).
This is an unconditional infinite family, but it has density zero among
the even integers and does not prove DS.

---

## 4. Fixed odd polar offsets

The same Newton polygon gives more prime-shift families.  For an odd
\(s\geq1\), define in the positive-sign normalization

\[
 B_s(X):=2H_s(X)+XH'_s(X).
 \tag{4.1}
\]

### Proposition 4.1

Fix an odd \(s\).  If \(B_s\) is square-free over \(\mathbf Q\), then for
all but finitely many primes \(p>s\),

\[
 \boxed{P'_{1,p+s}(X)\text{ is square-free over }\mathbf Q.}
 \tag{4.2}
\]

#### Proof

For \(m=p+s<2p\), the moving-prime derivative polygon is

\[
 (0,-1)\to(1,-2)\to(s,-2)\to(m-1,0).
 \tag{4.3}
\]

The first edge is linear and the last has a separable binomial residual.
The residual polar congruence on the middle edge is, up to a nonzero
scalar,

\[
 p^2P_m(X)\equiv \frac{X^2}{s}P'_s(X)\pmod p.
\]

After differentiation and removal of the nonzero monomial factor, the
unit-root residual polynomial is \(B_s\), up to \(X\mapsto-X\).  A fixed
square-free rational polynomial has square-free reduction away from the
finite set of primes dividing its cleared discriminant and leading
coefficient.  At every other prime, all three root clusters are simple.
\(\square\)

The first explicit cases are

\[
 B_1=2,
\]

\[
 B_3\doteq72X^2+27X+2,
 \qquad \operatorname {Disc}=3^2\cdot17,
 \tag{4.4}
\]

and

\[
 B_5\doteq
 7200X^4+6000X^3+1700X^2+175X+4,
\]

\[
 \operatorname {Disc}(B_5)
 =-2^{10}3^3 5^6\cdot7\cdot137\cdot311.
 \tag{4.5}
\]

Here \(\doteq\) means equality up to a nonzero rational scalar.  The
moving-prime certificate therefore proves:

- \(P'_{1,p+3}\) is square-free for every prime \(p>3\), except possibly
  the residual-exception prime \(p=17\);
- \(P'_{1,p+5}\) is square-free for every prime \(p>5\), except possibly
  \(p\in\{7,137,311\}\).

The word “possibly” is deliberate: failure of this particular residual
certificate does not imply that the characteristic-zero derivative is
inseparable.  In fact the exact audit in Section 5 separately certifies the
four exceptional rows \(20,12,142,316\).  Combining the two certificates
gives the exception-free families

\[
 \boxed{
 P'_{1,p+3}\text{ is square-free for every prime }p>3,}
 \tag{4.6}
\]

\[
 \boxed{
 P'_{1,p+5}\text{ is square-free for every prime }p>5.}
 \tag{4.7}
\]

---

## 5. Exact finite audit through 5000

The companion program

```text
output/research/even_derivative_separability_audit.cpp
```

uses the fixed prime

\[
 \ell=998244353>5000.
\]

All denominators \(n n!\), \(n\leq5000\), are units modulo \(\ell\).
It computes the triangular coefficient array

\[
 c_{n,k}=[z^n]g(z)^k\pmod\ell
\]

by exact truncated convolution.  It then applies the Euclidean algorithm
both to \(H_r,H'_r\) for every even row and to \(B_s,B'_s\) for every
nonconstant odd polar row.  A constant modular gcd is a rigorous
good-reduction certificate for characteristic-zero square-freeness.
For odd (3\leq s\leq4999), the leading coefficient of (B_s) is
(s+1), and the relevant leading coefficients of both (B_s) and
(B_s') are nonzero modulo (998244353); thus their degrees are preserved
under reduction.

The command

```text
g++ -O3 -std=c++17 \
  output/research/even_derivative_separability_audit.cpp \
  -o even_ds_audit
./even_ds_audit --bound 5000
```

returns exactly

```text
BOUND=5000
MODULUS=998244353
EVEN_ROWS_TESTED=2500
FAILURES=[]
DS_AUDIT=PASS
NONCONSTANT_ODD_POLAR_ROWS_TESTED=2499
POLAR_FAILURES=[]
POLAR_AUDIT=PASS
```

Therefore

\[
 \boxed{
 P'_r\text{ is square-free over }\mathbf Q
 \quad(2\leq r\leq5000,\ r\text{ even}).}
 \tag{5.1}
\]

The same run also proves

\[
 \boxed{
 B_s\text{ is square-free over }\mathbf Q
 \quad(1\leq s\leq4999,\ s\text{ odd}),}
 \tag{5.2}
\]

where \(B_1=2\) is the trivial constant case.  Consequently each of these
2500 offsets satisfies the hypothesis of Proposition 4.1.

This is an exact finite theorem, not an asymptotic inference.  A separate
exact-rational SymPy calculation cross-checked the coefficient convention
and gcd result through \(r=12\).

Reproducibility hashes:

```text
d9c6f7c6438a9e7bf5d0aed50bbce727f460efcacc720f520c97b444b3f83b4d  even_derivative_separability_audit.cpp
1e4b4073527d7d2543c8a087c37f0888fdbd99c7ca2b7880a418e7c533e6617b  even_derivative_separability_audit_5000.txt
```

---

## 6. Why the natural completions still fail

### 6.1 Raw reduction modulo two

The Faber trace reduction attached to \(z+z^2\) is \(L_r\).  For even
\(r=2s\), Frobenius gives

\[
 L_{2s}=L_s^2,
\]

so \(L'_{2s}=0\) in characteristic two.  Raw mod-two differentiation
contains no separability information; division by the exact dyadic content
in Section 2 is essential.

### 6.2 Iterating the first dyadic face

Theorem 2.2 does not automatically recurse.  For \(q=1,r=10\), the Newton
polygon of \(\widehat P'_{1,10}\) contains the segment

\[
 (2,3)\longrightarrow(4,1).
\]

Its residual polynomial is

\[
 1+Y^2=(1+Y)^2
 \quad\text{over }\mathbf F_2.
\]

Thus the standard simple-root Hensel lemma stops on an actual inseparable
intermediate face.  This is a barrier to the proof method, not a
counterexample to DS.

### 6.3 Reality

The even derivative rows are not real-rooted.  For example

\[
 H_4(X)=X^3+\frac34X^2+\frac{25}{144}X+\frac1{96}
\]

has negative discriminant.  Hence a Sturm or interlacing proof covering
all roots cannot be based on real-rootedness.

### 6.4 Finite prime shifts

The prime-successor and fixed-offset families each have prime-counting
size, but a finite union of them does not cover all even integers.  Turning
Proposition 4.1 into DS would require both square-freeness of every odd
polar \(B_s\) and a pointwise prime-selection theorem.  Neither statement
is proved here.

---

## 7. Referee-status ledger

| Claim | Status | Exact reason |
|---|---|---|
| Identity (1.4) | **PROVED** | Differentiate the exact resolvent |
| Dyadic reduction (2.6) | **PROVED** | Integral scaling and coefficient extraction |
| At least half the roots of every even \(P'_{q,r}\) are simple, all \(q\) | **PROVED** | Lucas quotient plus simple-root Hensel lifting |
| \(P'_{q,p+1}\) square-free for all \(q\geq1\), odd prime \(p\) | **PROVED** | Two-edge Newton polygon with separable residuals |
| Fixed-offset Proposition 4.1 | **PROVED** | Three-edge polygon and good reduction of \(B_s\) |
| DS for every even \(r\leq5000\) | **EXACT COMPUTATION** | One good finite-field witness for every row |
| \(B_s\) square-free for odd \(s\leq4999\) | **EXACT COMPUTATION** | Same fixed-prime gcd audit |
| DS for every even \(r\) | **OPEN** | Inner dyadic faces can be inseparable |
| Counterexample to DS | **NONE FOUND** | Exact audit through 5000 |

### Strongest honest conclusion

Hypothesis DS survives a substantially stronger test and has new infinite
unconditional families, but it is not closed.  The most promising remaining
target is a higher-order lifting theorem for the inner dyadic factor in
(2.6), capable of resolving inseparable faces such as \(1+Y^2\).  Neither
the finite audit nor the prime-shift families should be promoted to an
all-row theorem.

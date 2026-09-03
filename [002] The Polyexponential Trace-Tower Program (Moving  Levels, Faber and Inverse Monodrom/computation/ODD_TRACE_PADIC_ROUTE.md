# An isolated-branch $p$-adic criterion for odd trace monodromy

## Status

This note gives a rigorous replacement for direct discriminant computation
in the odd-degree trace problem.  It does **not** yet prove the unrestricted
all-odd statement.  It proves:

1. a uniform sufficient criterion, valid for every polyexponential order
   $q\geq1$, which produces an isolated transposition from one small
   finite-field gcd;
2. for the original exponential-integral tower $q=1$, exact modular
   verification of that criterion for every odd degree
   \(7\leq m\leq100000\);
3. together with the pre-existing exact degrees \(m=3,5\), geometric and
   arithmetic monodromy \(S_m\) for every odd \(3\leq m\leq100000\).

The conceptual gain is important: the degree-$m$ critical-value
discriminant is replaced by the square-freeness of a trace derivative of
degree $r-1=m-p-1$, where $p$ is a prime just below $m$.  In the exact
run through $100000$, the largest residual degree was only $72$, and no
degree required more than the two largest eligible primes.

---

## 1. Trace polynomials

For $q\geq1$, put

\[
 E_q(z)=\operatorname {Ein}_q(z)
 =\sum_{n\geq1}\frac{(-1)^{n-1}}{n!n^q}z^n,
 \qquad
 A_q(z)=\frac{E_q(z)}z
 =\sum_{n\geq0}a_nz^n,
\]

where

\[
 a_n=\frac{(-1)^n}{n!(n+1)^{q+1}}.
\]

Define

\[
 P_{q,m}(X)=-m[z^m]\log(1-XE_q(z)).
\]

Then

\[
 P'_{q,m}(X)=\sum_{j=0}^{m-1}d_jX^j,
 \qquad
 d_j=m[z^{m-j-1}]A_q(z)^{j+1}.
 \tag{1.1}
\]

The all-order Faber--$2$-adic theorem in the main trace note proves that
every $P_{q,m}$ is indecomposable over \(\overline{\mathbf Q}\).  Thus its
geometric monodromy is primitive.

---

## 2. Bertrand-prime Newton polygon

Let $m\geq7$ be odd.  Choose an odd prime satisfying

\[
 \frac{m+1}{2}<p<m,
 \qquad r=m-p.
 \tag{2.1}
\]

Thus $r$ is even and $2\leq r\leq p-2$.  Since all coefficient indices
in (1.1) are below $2p$, there is at most one $p$-singular factor in
each contributing product.  The exceptional coefficient is

\[
 v_p(a_{p-1})=-(q+1),
\]

whereas $v_p(a_n)=-1$ for $p\leq n\leq m-1$, and all remaining relevant
$a_n$ are $p$-integral.  It follows that

\[
\begin{aligned}
 v_p(d_0)&=-1,\\
 v_p(d_1)&=-(q+1),\\
 v_p(d_j)&\geq-(q+1) &&(1\leq j\leq r),\\
 v_p(d_r)&=-(q+1),\\
 v_p(d_j)&\geq0 &&(j>r),\\
 v_p(d_{m-1})&=0.
\end{aligned}
\tag{2.2}
\]

For example, the unique dominant term in $d_1$ is

\[
 2m a_{p-1}a_{r-1},
\]

and the unique dominant term in $d_r$ is

\[
 (r+1)m a_{p-1}.
\]

Consequently the Newton polygon of $P'_{q,m}$ has exactly the three
segments

\[
 (0,-1)\longrightarrow(1,-q-1)
 \longrightarrow(r,-q-1)\longrightarrow(m-1,0).
 \tag{2.3}
\]

Hence the critical points split into:

* one simple point \(\alpha\) with \(v_p(\alpha)=q\);
* $r-1$ unit critical points;
* $p-1$ critical points of valuation
  \(-(q+1)/(p-1)\).

At the isolated point, the first two derivative terms give

\[
 d_1\alpha=-d_0+\text{higher-valuation terms}.
\]

Since $p$ is odd,

\[
 b:=P_{q,m}(\alpha)
 =\frac12d_0\alpha+\text{higher-valuation terms},
 \qquad
 \boxed{v_p(b)=q-1.}
 \tag{2.4}
\]

---

## 3. The residual polar polynomial

Let

\[
 R_{q,r}(X):=P'_{q,r}(X)\in\mathbf F_p[X].
 \tag{3.1}
\]

For $1\leq j\leq r$, set

\[
 C_j=[z^{r-j}]A_q(z)^j\pmod p.
\]

Then

\[
 R_{q,r}(X)=r\sum_{j=1}^r C_jX^{j-1}.
 \tag{3.2}
\]

Keeping precisely the terms of valuation \(-(q+1)\) in the large trace
polynomial gives, up to a nonzero scalar in \(\mathbf F_p\),

\[
 p^{q+1}P_{q,m}(X)
 \equiv \frac{X^2}{r}R_{q,r}(X)\pmod p,
 \tag{3.3}
\]

and differentiation gives the corresponding residual equation for unit
critical points.

Suppose that $R_{q,r}$ is square-free in \(\mathbf F_p[X]\).  If a unit
critical point \(\beta\) had elevated critical value, (3.3) and its
derivative would imply

\[
 R_{q,r}(\bar\beta)=R'_{q,r}(\bar\beta)=0,
\]

contrary to square-freeness.  Therefore every unit critical point satisfies

\[
 v_p(P_{q,m}(\beta))=-(q+1)<0.
 \tag{3.4}
\]

On the final Newton segment, only $d_rX^r$ and $mX^{m-1}$ are principal
in the derivative.  There is one denominator that requires care when one
passes from $P'$ back to $P$, namely $c_p=d_{p-1}/p$.  It causes no extra
principal term, because

\[
 d_{p-1}=m[z^r]A_q(z)^p
 \equiv m[z^r]A_q(z^p)=0\pmod p
 \qquad(0<r<p).
 \tag{3.5a}
\]

Thus $c_p$ is $p$-integral.  At a critical point $\beta$ on that segment,

\[
 m\beta^{m-1}=-d_r\beta^r+\text{higher terms}.
\]

Thus the principal part of the critical value is

\[
 d_r\beta^{r+1}
 \left(\frac1{r+1}-\frac1m\right)
 =d_r\beta^{r+1}\frac{p-1}{m(r+1)},
\]

whose displayed rational factor is a $p$-adic unit.  Consequently

\[
 v_p(P_{q,m}(\beta))
 =-\frac{m(q+1)}{p-1}<0.
 \tag{3.5}
\]

Equations (2.4), (3.4), and (3.5) show that $b$ is the unique critical
value of nonnegative $p$-adic valuation.  Its critical point $\alpha$
is simple.  Therefore inertia around $b$ is one transposition.

### Theorem 3.1 -- isolated-branch criterion

If (2.1) holds and

\[
 \gcd(P'_{q,r},P''_{q,r})=1
 \quad\text{in }\mathbf F_p[X],
 \tag{3.6}
\]

then

\[
 \boxed{
 \operatorname {Gal}
 (P_{q,m}(X)-T/\overline{\mathbf Q}(T))=S_m.}
 \tag{3.7}
\]

Indeed, indecomposability gives primitivity, and a primitive permutation
group containing a transposition is the full symmetric group.  Since the
arithmetic group contains the geometric group, it is also $S_m$.

### Corollary 3.2 -- an unconditional infinite all-order family

Take $r=2$.  The residual derivative $P'_{q,2}$ is linear and therefore
square-free over every odd finite field.  Hence for every $q\geq1$ and
every prime $p\geq5$,

\[
 \boxed{
 G^{\rm geom}_{q,p+2}=G^{\rm ar}_{q,p+2}=S_{p+2}.}
 \tag{3.8}
\]

Thus the criterion is not merely computational: it proves symmetric
monodromy in infinitely many odd degrees, simultaneously for every
polyexponential order.

Two formerly immediate gaps are covered without computation:

| degree $m$ | prime $p$ | residual degree $r$ | conclusion |
|---:|---:|---:|---|
| $403$ | $401$ | $2$ | geometric and arithmetic $S_{403}$ for all $q$ |
| $441$ | $439$ | $2$ | geometric and arithmetic $S_{441}$ for all $q$ |

Thus the first odd geometric degree beyond the old $401$ cutoff and the
first unresolved odd-square arithmetic candidate are both removed by the
same structural argument.

More generally, fix an even $r\geq2$ and an order $q$ for which
$P'_{q,r}$ is square-free over $\mathbf Q$.  After clearing denominators,
only finitely many primes divide its derivative discriminant.  Therefore
for all but finitely many primes $p>r+1$, Theorem 3.1 applies to
$m=p+r$.  Each such residual degree consequently supplies an unconditional
infinite shifted-prime family of symmetric trace monodromy.

---

## 4. Exact certification for the original tower

The script

* `output/research/odd_trace_padic_certify.py`

constructs $E_1\bmod p$, computes $P'_{1,r}\bmod p$ by truncated exact
convolution, and checks (3.6) by a polynomial gcd.  Running

```text
python output/research/odd_trace_padic_certify.py \
  --max-m 100000 --order 1 --prime-trials 12
```

returns

```text
order q=1
certified odd degrees: 7 <= m <= 100000
number of certified degrees: 49997
largest residual degree r: 72
largest number of prime trials used: 2
status: PASS
```

The script SHA-256 is

```text
0a9d2183d90356a929bb938da0c83726fdd31a512a2c357aa14883208b8ebc54
```

Combining this exact run with the earlier exact certificates in degrees
$3$ and $5$ proves

\[
 \boxed{
 G^{\rm geom}_{1,m}=G^{\rm ar}_{1,m}=S_m
 \quad(3\leq m\leq100000, m\text{ odd}).}
 \tag{4.1}
\]

Together with the unconditional even-degree theorem, this gives $S_m$ for
every $2\leq m\leq100000$.

This is a finite theorem backed by exact certificates, not an all-$m$
theorem.  The computation is unusually light: although $m$ reaches
$100000$, only residual derivatives through degree $72$ occur.

---

## 5. What remains for an all-odd theorem

Bertrand's theorem always supplies at least one prime in
$(m/2,m)$, but it does not itself guarantee (3.6).  Thus the remaining
global statement is the following purely finite-field selection lemma:

> For every sufficiently large odd $m$, at least one prime
> \((m+1)/2<p<m\) makes $P'_{1,m-p}$ square-free modulo $p$.

The exact run shows this through $100000$, always using one of the two
largest eligible primes.  This is compelling evidence, but it is not a
proof at infinity.

There is also a second, apparently uniform route.  Direct exact calculations
show that for every tested odd $m\leq33$, the critical-value discriminant
has an odd-length Newton segment at $p=3$, except at powers of $3$, where
$p=2$ supplies one.  Proving this two-prime Newton pattern would remove the
selection lemma entirely.  At present it remains a conjectural next gate.

The present theorem is nevertheless stronger than the previous fixed-prime
degree-$401$ audit in two ways: it reaches $100000$, and it explains the
transposition structurally through a small residual polar rather than by
sampling quadratic characters of the full discriminant.

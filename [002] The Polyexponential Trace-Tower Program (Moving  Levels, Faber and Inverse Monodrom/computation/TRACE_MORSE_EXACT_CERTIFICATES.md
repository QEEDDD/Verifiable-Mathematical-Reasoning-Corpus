# Exact trace-polynomial computations and finite-field certificates

## 1. Definition and coefficient identities

Put

\[
 E(z)=\operatorname {Ein}(z)
 =\sum_{n\geq1}\frac{(-1)^{n-1}}{n\,n!}z^n,
 \qquad
 P_m(X)=-m[z^m]\log(1-XE(z)).
\]

Then

\[
 [X^k]P_m(X)=\frac{m}{k}[z^m]E(z)^k
 =(-1)^{m-k}\frac{(k-1)!}{(m-1)!}
 B_{m,k}\left(1,\frac12,\ldots,\frac1{m-k+1}\right),
\]

where \(B_{m,k}\) is the exponential partial Bell polynomial.  In
particular, every nonzero coefficient has sign \((-1)^{m-k}\).  Equivalently,

\[
 P_m(X)=\sum_{k=1}^m(-1)^{m-k}\frac{m}{k}
 \sum_{\substack{n_1+\cdots+n_k=m\\n_i\geq1}}
 \prod_{i=1}^k\frac1{n_i n_i!}\,X^k.
\]

Logarithmic differentiation of the generating series gives the useful
recurrence

\[
 P_1(X)=X,
 \qquad
 P_m(X)=\frac{(-1)^{m-1}}{m!}X
 +X\sum_{j=1}^{m-1}\frac{(-1)^{j-1}}{j\,j!}P_{m-j}(X).
\]

The first upper coefficients are

\[
 P_m(X)=X^m-\frac m4X^{m-1}
 +\frac{m(9m-11)}{288}X^{m-2}+\cdots
 +\frac{(-1)^{m-1}}{m!}X.
\]

## 2. Small exact polynomials

\[
\begin{aligned}
P_2&=X^2-\frac12X,\\
P_3&=X^3-\frac34X^2+\frac16X,\\
P_4&=X^4-X^3+\frac{25}{72}X^2-\frac1{24}X,\\
P_5&=X^5-\frac54X^4+\frac{85}{144}X^3-\frac{35}{288}X^2+\frac1{120}X,\\
P_6&=X^6-\frac32X^5+\frac{43}{48}X^4-\frac{25}{96}X^3
 +\frac{1507}{43200}X^2-\frac1{720}X.
\end{aligned}
\]

## 3. Faber interpretation and an all-order composition obstruction

First take a general normalized formal series

\[
 f(z)=z+\sum_{n\ge2}a_nz^n,
 \qquad
 P_m^{(f)}(X)=-m[z^m]\log(1-Xf(z)).
\]

If \(c_k=[X^k]P_m^{(f)}\), then

\[
 c_k=\frac{m}{k}[z^m]f(z)^k
 =m a_{m-k+1}+Q_k(a_2,\ldots,a_{m-k}).
\]

Consequently

\[
 (a_2,\ldots,a_m)\longmapsto(c_{m-1},\ldots,c_1)
\]

is a triangular polynomial automorphism with every diagonal entry equal to
\(m\).  Thus, as the \((m-1)\)-jet of \(f\) varies, the normalized trace
polynomial is literally the generic monic degree-\(m\) polynomial with zero
constant term.  This separates the universal Faber mechanism from the hard
specialization problem at the particular jet of \(\operatorname {Ein}\).

Let

\[
 M(w)=\frac1{f(1/w)}=w+d_0+d_1w^{-1}+d_2w^{-2}+\cdots
\]

for a general normalized series \(f(z)=z+\sum_{n\ge2}a_nz^n\), and use the
standard Faber convention

\[
 \log\frac{M(w)-X}{w}
   =-\sum_{n\ge1}\frac{\Phi_n(X)}n w^{-n}.
\]

Subtracting the same identity at \(X=0\) shows precisely that

\[
 P_m(X)=\Phi_m(X)-\Phi_m(0).
\]

Thus \(P_m\) is the *normalized* Faber polynomial (the subtraction is
essential under the displayed standard convention).

Suppose \(m=ab\) with \(a,b>1\) and that \(P_m=G\circ H\).  Normalize the
decomposition so that \(G,H\) are monic, \(H(0)=G(0)=0\).  The Faber
property gives

\[
 P_m(M(w))=w^m-\Phi_m(0)+O(w^{-1}).
\]

Applying the formal inverse branch of \(G\) at infinity shows

\[
 H(M(w))=w^b+\text{constant}+O(w^{-1}).
\]

Uniqueness of the polynomial which cancels all positive powers now gives
\(H=\Phi_b-\Phi_b(0)=P_b\).  Moreover, the first Faber tail coefficient is

\[
 \Phi_b(M(w))=w^b+b d_b w^{-1}+O(w^{-2}),
 \qquad d_b=[z^b]\frac1{f(z)}.
\]

In \(G(P_b(M(w)))\), the coefficient of \(w^{m-b-1}\) is uniquely
\(ab d_b=m d_b\); lower powers of the outer polynomial cannot contribute
at that exponent.  Since \(P_m(M(w))\) has no positive powers below \(w^m\),
every decomposition with inner degree \(b\) forces

\[
 \boxed{d_b=0.}
\]

For \(f=\operatorname {Ein}\), none of these obstructions vanishes.  Indeed,
write

\[
 A(z)=\frac{\operatorname {Ein}(z)}z
 =\sum_{n\ge0}\frac{(-1)^n}{n!(n+1)^2}z^n,
 \qquad B(z)=\frac1{A(z)}=\sum_{n\ge0}B_nz^n.
\]

Legendre's formula gives

\[
 v_2\!\left(\frac{4^n}{n!(n+1)^2}\right)
 =n+s_2(n)-2v_2(n+1).
\]

This is zero for \(n=0,1\) and positive for every \(n\ge2\).  For the only
nontrivial case \(r=v_2(n+1)\ge1\), the last \(r\) binary digits of \(n\)
are all one, so \(s_2(n)\ge r\) and the displayed valuation is at least
\(n-r>0\).  Hence

\[
 A(4z)\equiv1+z\pmod2,
 \qquad
 B(4z)\equiv(1+z)^{-1}=\sum_{n\ge0}z^n\pmod2.
\]

It follows that \(4^nB_n\) is a 2-adic unit and

\[
 v_2(B_n)=-2n.
\]

Since \([z^b](1/\operatorname {Ein}(z))=B_{b+1}\), every \(d_b\) is
nonzero.  We therefore obtain the all-order theorem

\[
 \boxed{P_m\text{ is indecomposable over every characteristic-zero field}
 \quad(m\ge2).}
\]

## 4. Exact Morse criterion

Let

\[
 C_m(T)=\operatorname {Res}_X(P_m'(X),P_m(X)-T).
\]

If \(P_m'\) is square-free and \(C_m\) is square-free, the \(m-1\)
critical points of \(P_m\) are simple and have pairwise distinct critical
values.  Thus \(P_m\) is a Morse polynomial.  Since \(P_m(X)-T\) is
irreducible over \(\mathbf Q(T)\), its geometric monodromy is transitive;
the finite branch cycles are transpositions, and a transitive group generated
by transpositions is \(S_m\).  Consequently

\[
 \operatorname {Gal}(P_m(X)-T/\mathbf Q(T))=S_m.
\]

For a compact exact certificate, clear denominators, reduce modulo a good
prime \(p>m\), prove \(P_m'\) irreducible in \(\mathbf F_p[X]\), and prove
the corresponding \(C_m\) square-free in \(\mathbf F_p[T]\).  Both
properties then lift to characteristic zero.  Degree is preserved in this
test: all coefficient denominators have prime factors at most \(m\), while
the leading coefficient of the derivative is \(m\); hence \(p>m\) keeps
\(\deg P_m'=m-1\), and the leading \(T\)-coefficient of the resultant is
nonzero.  The following primes certify
all \(4\leq m\leq55\); \(m=2,3\) are immediate by their displayed formulas.

| \(m\) | witness \(p\) | \(m\) | witness \(p\) | \(m\) | witness \(p\) |
|---:|---:|---:|---:|---:|---:|
|4|5|22|89|40|233|
|5|19|23|29|41|193|
|6|13|24|109|42|503|
|7|13|25|83|43|197|
|8|97|26|41|44|47|
|9|79|27|43|45|83|
|10|19|28|653|46|751|
|11|17|29|83|47|137|
|12|53|30|53|48|499|
|13|29|31|47|49|107|
|14|37|32|73|50|149|
|15|17|33|37|51|103|
|16|107|34|101|52|181|
|17|113|35|173|53|2027|
|18|23|36|67|54|89|
|19|31|37|89|55|83|
|20|193|38|599||| 
|21|107|39|251||| 

This is an exact finite theorem, not merely floating-point evidence:

\[
 \boxed{\operatorname {Gal}(P_m(X)-T/\mathbf Q(T))=S_m
 \quad(2\leq m\leq55).}
\]

The attached `trace_morse_certificates.py` reproduces the certificates.

## 5. Müller classification and a near-all-order symmetric-group theorem

Center the polynomial by

\[
 \widehat P_m(Y)=P_m(Y+1/4)-P_m(1/4).
\]

Direct use of the first four upper coefficients gives, for \(m\ge4\),

\[
 [Y^{m-2}]\widehat P_m=-\frac m{144},
 \qquad
 [Y^{m-3}]\widehat P_m=\frac m{576}.
\]

Thus \(P_m\) is not linearly equivalent to a power map (the cyclic case),
and it is not linearly equivalent to a Chebyshev polynomial (the dihedral
case).  Müller's classification of primitive monodromy groups of
indecomposable polynomials over \(\mathbf Q\) then leaves \(A_m,S_m\), apart
from the explicit exceptional degrees \(6,9,10\), which are already covered
by the exact Morse computation above.

For a monic degree-\(m\) polynomial,

\[
 \operatorname {LC}_T\operatorname {Disc}_X(P_m(X)-T)
 =(-1)^{m(m-1)/2+m-1}m^m.
\]

Consequently the discriminant is automatically nonsquare when \(m\) is
even (its \(T\)-degree is odd), and for odd nonsquare \(m\) its leading
coefficient is not a rational square.  Hence

\[
 \operatorname {Gal}(P_m(X)-T/\mathbf Q(T))=S_m
\]

for every \(m\ge2\) except possibly odd perfect squares.  The exact Morse
certificates settle \(m=9,25,49\).

For the next square degrees, reduction modulo \(409\) gives the following
nonsquare discriminant specializations.  Each listed residue has Legendre
symbol \(-1\) modulo \(409\).

| \(m\) | specialization \(T=t\) | \(\operatorname {Disc}(P_m-t)\bmod409\) |
|---:|---:|---:|
|81|0|29|
|121|4|268|
|169|0|47|
|225|3|110|
|289|0|95|
|361|3|260|

Here \(409>401\), so reduction preserves every denominator and degree.
A square in \(\mathbf Q(T)\) would reduce to a square and take square values
at every nonvanishing specialization, so these are exact certificates.
Combining them with the classification yields

\[
 \boxed{\operatorname {Gal}(P_m(X)-T/\mathbf Q(T))=S_m
 \quad(2\le m\le401).}
\]

There is a stronger geometric certificate.  If a polynomial
\(D(T)\in\mathbf Q[T]\) is a square over \(\overline{\mathbf Q}(T)\), then
unique factorization and Galois invariance give

\[
 D(T)=cR(T)^2,
 \qquad c\in\mathbf Q^\times,\quad R(T)\in\mathbf Q[T].
\]

At every good finite-field reduction, all nonzero values \(D(t)\) must
therefore have the same quadratic character, namely the character of \(c\).
For every odd

\[
 57\le m\le401,
\]

an exact computation in \(\mathbf F_{409}\) finds two regular values
\(t_+,t_-\) for which

\[
 \left(\frac{\operatorname {Disc}(P_m-t_+)}{409}\right)=+1,
 \qquad
 \left(\frac{\operatorname {Disc}(P_m-t_-)}{409}\right)=-1.
\]

For odd \(m\le55\), geometric \(S_m\) was already proved by the exact Morse
certificates; for even \(m\), the inertia generator at infinity is an odd
\(m\)-cycle and excludes \(A_m\).  Therefore the strengthened conclusion is

\[
 \boxed{\operatorname {Gal}(P_m(X)-T/\overline{\mathbf Q}(T))=S_m
 \quad(2\le m\le401).}
\]

In particular, arithmetic and geometric monodromy coincide in this range.
Run

```text
python output/research/trace_galois_401.py --all-odd
```

from the workspace root to regenerate every opposite-character pair.  The
script also checks the compact six-row table above on every invocation.  For
the current script, the deterministic command

```text
python output/research/trace_galois_401.py --all-odd | sha256sum
```

returns

```text
816d88a4208128e0d8bc276098598901e3cfec1f7bcf34665514d833e70bb4a5  -
```

More generally, without finite computation beyond the low exceptional
degrees, the only still-open indices for **arithmetic** monodromy are odd
perfect squares.  For **geometric** monodromy, every odd index beyond the
two-character certified range remains a priori an \(A_m/S_m\) question;
the leading-coefficient square-class argument alone does not distinguish
those two geometric groups.

Primary classification reference: P. Müller, *Primitive monodromy groups of
polynomials*, in **Recent Developments in the Inverse Galois Problem**,
Contemporary Mathematics 186 (1995), 385--401.

## 6. Further observed structure

Exact factorization over \(\mathbf Q\) gives:

- \(P_m'\) is irreducible for every \(4\leq m\leq55\);
- \(C_m(T)\) is irreducible for every \(4\leq m\leq20\) checked directly;
- `decompose(P_m)` returns only \(P_m\) itself for every \(2\leq m\leq30\).

The finite-field witnesses prove the first assertion and imply
indecomposability throughout \(4\leq m\leq55\).  They strongly support the
all-order Trace--Morse conjecture, but they do not constitute an all-\(m\)
proof.

## 7. Uniform transfer to every polyexponential order

For an integer \(q\ge1\), put

\[
 \operatorname {Ein}_q(z)=
 \sum_{n\ge1}\frac{(-1)^{n-1}}{n!\,n^q}z^n,
 \qquad
 P_{q,m}(X)=-m[z^m]\log(1-X\operatorname {Ein}_q(z)).
\]

The all-order Faber obstruction is uniform in \(q\).  Indeed,

\[
 A_q(z)=\frac{\operatorname {Ein}_q(z)}z
 =\sum_{n\ge0}\frac{(-1)^n}{n!(n+1)^{q+1}}z^n.
\]

For \(r=v_2(n+1)\),

\[
 v_2\!\left(
 \frac{2^{(q+1)n}}{n!(n+1)^{q+1}}
 \right)
 =nq+s_2(n)-(q+1)r.
\]

The value is zero at \(n=0,1\) and positive for \(n\ge2\): when \(r\ge1\),
\(s_2(n)\ge r\) and the expression is at least \(q(n-r)>0\).
Consequently

\[
 A_q(2^{q+1}z)\equiv1+z\pmod2.
\]

If \(B_q=1/A_q=\sum B_{q,n}z^n\), then

\[
 v_2(B_{q,n})=-(q+1)n.
\]

Every coefficient \([z^b](1/\operatorname {Ein}_q)=B_{q,b+1}\) is therefore
nonzero, and the Faber obstruction proves

\[
 \boxed{P_{q,m}\text{ is indecomposable for all }q\ge1, m\ge2.}
\]

There is also a uniform exclusion of the cyclic and dihedral cases.  For a
general \(f=z+a_2z^2+a_3z^3+a_4z^4+\cdots\), the first centered coefficients
are

\[
 [Y^{m-2}]\widehat P_m=m(a_3-a_2^2),
 \qquad
 [Y^{m-3}]\widehat P_m=m(a_2^3-2a_2a_3+a_4).
\]

For \(f=\operatorname {Ein}_q\), the first is nonzero by unique
factorization, while clearing the positive denominator in the second gives

\[
 4^{q+1}-3^{q+1}-6^q,
\]

which is \(1\pmod3\).  Hence no \(P_{q,m}\) is of cyclic or Chebyshev type
for \(m\ge4\).  The remaining uniform problem is to exclude the alternating
and three low exceptional monodromy possibilities without a finite bound on
\(q,m\).

Together with Müller and the leading discriminant coefficient, this already
implies the uniform partial classification

\[
 \operatorname {Gal}(P_{q,m}(X)-T/\mathbf Q(T))=S_m
\]

for every \(q\ge1\) and every \(m\) outside the odd perfect squares and the
two still-possible exceptional degrees \(6,10\).  Geometrically, the same
conclusion holds for every even \(m\notin\{6,10\}\); at odd degrees the
remaining generic alternative is \(A_m\) versus \(S_m\) (with degree \(9\)
also belonging to Müller's explicit exceptional list).

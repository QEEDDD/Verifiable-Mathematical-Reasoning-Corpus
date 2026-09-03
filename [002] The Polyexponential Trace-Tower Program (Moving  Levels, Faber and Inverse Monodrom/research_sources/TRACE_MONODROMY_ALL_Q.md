# Uniform monodromy of polyexponential trace polynomials

## Scope and status

This note proves an all-order structural theorem for the trace polynomials
attached to every integer-order polyexponential.  The proof has four parts:

1. normalized Faber rigidity turns a polynomial decomposition into a
   vanishing coefficient of a reciprocal series;
2. a uniform 2-adic argument proves that none of those reciprocal
   coefficients vanishes;
3. two centered affine invariants exclude the cyclic, dihedral, and three
   exceptional rational polynomial-monodromy cases in Müller's
   classification;
4. the discriminant separates the geometric and arithmetic conclusions.

The result does **not** prove that every trace polynomial is Morse.  It proves
indecomposability for every pair of indices and reduces its monodromy to the
alternating/symmetric dichotomy, with the precise conclusions stated below.

Throughout, \(q\geq1\) and \(m\geq2\) are integers, and

\[
 E_q(z):=\operatorname {Ein}_q(z)
 =\sum_{n\geq1}\frac{(-1)^{n-1}}{n!\,n^q}z^n,
\]

\[
 P_{q,m}(X):=-m[z^m]\log(1-XE_q(z)).
\]

The coefficient formula

\[
 [X^k]P_{q,m}(X)=\frac{m}{k}[z^m]E_q(z)^k
\]

shows that \(P_{q,m}\in\mathbf Q[X]\), that its constant term is zero, and
that it is monic of degree \(m\).

---

## 1. A general normalized-Faber rigidity lemma

We first work with an arbitrary normalized formal series

\[
 f(z)=z+\sum_{n\geq2}a_nz^n
\]

over a characteristic-zero field and define

\[
 P_m^{(f)}(X):=-m[z^m]\log(1-Xf(z)).
\]

Put

\[
 M(w):=\frac1{f(1/w)}
 =w+d_0+d_1w^{-1}+d_2w^{-2}+\cdots .
\]

Let \(\Phi_m\) be the standard Faber polynomial of \(M\), normalized by

\[
 \log\frac{M(w)-X}{w}
 =-\sum_{m\geq1}\frac{\Phi_m(X)}m w^{-m}.
\]

### Lemma 1 (normalized Faber identity)

For every \(m\geq1\),

\[
 P_m^{(f)}(X)=\Phi_m(X)-\Phi_m(0).
\]

#### Proof

Since \(f(1/w)=M(w)^{-1}\),

\[
 \log(1-Xf(1/w))
 =\log\frac{M(w)-X}{w}-\log\frac{M(w)}w.
\]

Comparing the coefficient of \(w^{-m}\) gives the formula. \(\square\)

### Lemma 2 (inner-factor rigidity)

Suppose \(m=ab\) with \(a,b>1\).  If

\[
 P_m^{(f)}=G\circ H
\]

over a characteristic-zero extension field, then the decomposition may be
normalized so that \(G,H\) are monic, \(G(0)=H(0)=0\), and under this
normalization

\[
 H=P_b^{(f)}.
\]

#### Proof

The Faber identity gives

\[
 P_m^{(f)}(M(w))=w^m-\Phi_m(0)+O(w^{-1}).
\]

Let \(\Psi\) be the formal inverse branch of the monic degree-\(a\)
polynomial \(G\) at infinity.  It has a Puiseux expansion

\[
 \Psi(U)=U^{1/a}+c_0+c_1U^{-1/a}+c_2U^{-2/a}+\cdots .
\]

Substitution of \(U=w^{ab}+O(1)\) shows

\[
 H(M(w))=w^b+\text{constant}+O(w^{-1});
\]

in particular, there are no powers \(w^{b-1},\ldots,w\).  The defining
uniqueness of the degree-\(b\) Faber polynomial implies that \(H\) differs
from \(\Phi_b\) by a constant.  The normalization \(H(0)=0\) then gives
\(H=\Phi_b-\Phi_b(0)=P_b^{(f)}\). \(\square\)

### Lemma 3 (reciprocal-coefficient obstruction)

With

\[
 \frac1{f(z)}=z^{-1}+d_0+d_1z+d_2z^2+\cdots,
\]

a decomposition of \(P_m^{(f)}\) having inner degree \(b\) forces

\[
 d_b=[z^b]\frac1{f(z)}=0.
\]

#### Proof

The first negative Faber coefficient is

\[
 \Phi_b(M(w))=w^b+b d_bw^{-1}+O(w^{-2}).
\]

Here is a formal-residue verification.  If \(L\) is the compositional
inverse of \(M\) at infinity, then \(\Phi_b(X)\) is the polynomial part of
\(L(X)^b\).  Formal change of variables gives

\[
 [X^{-1}]L(X)^b
 =\operatorname {res}_X L(X)^b\,dX
 =\operatorname {res}_w w^bM'(w)\,dw
 =-bd_b.
\]

Substituting \(X=M(w)\) into the polynomial/negative-power decomposition of
\(L(X)^b\) therefore gives the displayed coefficient \(+bd_b\).  Hence

\[
 P_b^{(f)}(M(w))
 =w^b-\Phi_b(0)+bd_bw^{-1}+O(w^{-2}).
\]

In \(G(P_b^{(f)}(M(w)))\), the coefficient at

\[
 w^{m-b-1}=w^{b(a-1)-1}
\]

has the unique contribution \(ab d_b=md_b\) from the leading power of
\(G\).  Indeed, a constant selection creates deficit \(b\), a negative term
\(w^{-j}\) creates deficit \(b+j\), and there are no terms of degrees
\(b-1,\ldots,1\); neither another selection in the leading outer power nor
a lower outer power can reach deficit \(b+1\).  On the other hand,
\(P_m^{(f)}(M(w))\) has no positive power below \(w^m\).  Therefore
\(md_b=0\), and characteristic zero gives \(d_b=0\). \(\square\)

### Remark (generic jet coordinates)

If \(c_k=[X^k]P_m^{(f)}\), then

\[
 c_k=ma_{m-k+1}+Q_k(a_2,\ldots,a_{m-k}).
\]

Thus

\[
 (a_2,\ldots,a_m)\longmapsto(c_{m-1},\ldots,c_1)
\]

is a triangular polynomial automorphism with diagonal entries \(m\).  The
specialized polyexponential problem is therefore not caused by a defect in
the universal trace construction: the general \((m-1)\)-jet produces the
generic monic degree-\(m\), zero-constant polynomial.

---

## 2. Uniform 2-adic nonvanishing

Write

\[
 A_q(z):=\frac{E_q(z)}z
 =\sum_{n\geq0}\frac{(-1)^n}{n!(n+1)^{q+1}}z^n,
 \qquad
 B_q(z):=\frac1{A_q(z)}=\sum_{n\geq0}B_{q,n}z^n.
\]

### Theorem 4 (exact reciprocal valuations)

For all \(q\geq1\) and \(n\geq0\),

\[
 v_2(B_{q,n})=-(q+1)n.
\]

In particular, every \(B_{q,n}\) is nonzero.

#### Proof

Let \(s_2(n)\) be the sum of the binary digits of \(n\), and put
\(r=v_2(n+1)\).  Legendre's formula \(v_2(n!)=n-s_2(n)\) gives

\[
 v_2\!\left(
 \frac{2^{(q+1)n}}{n!(n+1)^{q+1}}
 \right)
 =qn+s_2(n)-(q+1)r.
\]

This value is zero for \(n=0,1\).  If \(n\geq2\) and \(r=0\), it is
positive.  If \(r\geq1\), the final \(r\) binary digits of \(n\) are all
one, so \(s_2(n)\geq r\), and

\[
 qn+s_2(n)-(q+1)r
 =q(n-r)+(s_2(n)-r)>0.
\]

It follows that

\[
 A_q(2^{q+1}z)\equiv1+z\pmod2.
\]

Taking formal reciprocals in \(\mathbf Z_2[[z]]\),

\[
 B_q(2^{q+1}z)
 \equiv(1+z)^{-1}
 =\sum_{n\geq0}z^n\pmod2.
\]

Thus every \(2^{(q+1)n}B_{q,n}\) is a 2-adic unit, which is exactly the
claimed valuation. \(\square\)

Since

\[
 \frac1{E_q(z)}=z^{-1}B_q(z),
 \qquad
 [z^b]\frac1{E_q(z)}=B_{q,b+1},
\]

Lemmas 2--3 immediately give the central structural result.

### Theorem 5 (all-order indecomposability)

For every \(q\geq1\) and \(m\geq2\), the polynomial \(P_{q,m}\) is
indecomposable over \(\overline{\mathbf Q}\), and hence over every
characteristic-zero subfield.

---

## 3. Centered invariants and the cyclic/dihedral cases

For a general series

\[
 f(z)=z+a_2z^2+a_3z^3+a_4z^4+\cdots,
\]

the first upper coefficients of \(P_m^{(f)}\) are

\[
\begin{aligned}
P_m^{(f)}(X)={}&X^m+ma_2X^{m-1}
 +m\left(a_3+\frac{m-3}{2}a_2^2\right)X^{m-2}\\
&+m\left(a_4+(m-4)a_2a_3
 +\frac{(m-4)(m-5)}6a_2^3\right)X^{m-3}+\cdots .
\end{aligned}
\]

The last displayed term and the corresponding formula below are understood
for \(m\ge4\); the \(Y^{m-2}\) formula is valid for \(m\ge3\).

Center it by

\[
 \widehat P_m(Y):=P_m^{(f)}(Y-a_2)-P_m^{(f)}(-a_2).
\]

A direct expansion yields

\[
 [Y^{m-2}]\widehat P_m=m(a_3-a_2^2),
\]

\[
 [Y^{m-3}]\widehat P_m=m(a_2^3-2a_2a_3+a_4).
\]

For \(f=E_q\),

\[
 a_2=-\frac1{2^{q+1}},\qquad
 a_3=\frac1{2\cdot3^{q+1}},\qquad
 a_4=-\frac1{3\cdot2^{2q+3}}.
\]

Define

\[
 N_A(q):=2^{2q+1}-3^{q+1},
 \qquad
 N_B(q):=2^{2q+2}-3^{q+1}-6^q.
\]

Then

\[
 a_3-a_2^2
 =\frac{N_A(q)}{2^{2q+2}3^{q+1}},
\]

\[
 a_2^3-2a_2a_3+a_4
 =\frac{N_B(q)}{2^{3q+3}3^{q+1}}.
\]

The first numerator is nonzero by unique factorization, and

\[
 N_B(q)\equiv1\pmod3.
\]

Thus both centered coefficients are nonzero.  A polynomial with cyclic
monodromy is linearly equivalent to a power map, whose centered coefficient
of degree \(m-2\) vanishes, so the cyclic case is excluded for \(m\ge3\).
A polynomial with dihedral monodromy is linearly
equivalent to a Chebyshev polynomial, whose centered coefficient of degree
\(m-3\) vanishes, so the proper dihedral case is excluded for \(m\ge4\).
In degree \(3\), the dihedral group is \(D_3\cong S_3\), while the cyclic
case has already been excluded.  Degree \(2\) is immediate.

---

## 4. Excluding Müller's exceptional degrees 6, 9, and 10

For a monic centered polynomial

\[
 F(Y)=Y^m+C_2Y^{m-2}+C_3Y^{m-3}+\cdots,
 \qquad C_2\ne0,
\]

the quantity

\[
 \mathcal I(F):=\frac{C_3^2}{C_2^3}
\]

is invariant under linear equivalence: after monic normalization, input
scaling has weights \(2\) and \(3\) on \(C_2,C_3\) (with reciprocal weights
under the opposite input-scaling convention), and output scaling is fixed by
making the polynomial monic.  In either convention the displayed ratio is
unchanged.

For \(P_{q,m}\), the preceding formulas give

\[
 \mathcal I(P_{q,m})=\frac{R_q}{m},
 \qquad
 R_q:=3^{q+1}\frac{N_B(q)^2}{N_A(q)^3}.
\]

Müller's three exceptional rational polynomials have the following centered
invariants:

| degree | representative | \(\mathcal I\) |
|---:|---|---:|
|6|\(X^4(X^2+6X+25)\)|\(18/5\)|
|9|\(9X^9+108X^7+72X^6+\cdots\)|\(1/27\)|
|10|\((X^2-405)^4(X^2+50X+945)\)|\(-8/81\)|

For completeness, the centered pairs \((C_2,C_3)\) are respectively

\[
 (10,-60),\qquad(12,8),\qquad(-1800,-24000).
\]

Both \(N_A(q)\) and \(N_B(q)\) are 3-adic units.  Moreover \(R_1=-9\),
while \(R_q>0\) for \(q\geq2\): indeed \(N_A(2)=5>0\), and the ratio of
the two exponential terms increases by a factor \(4/3\) with \(q\).  We can
now exclude each row:

- Degree \(10\) would require \(R_q=-80/81\).  The sign excludes
  \(q\geq2\), and \(R_1=-9\ne-80/81\).
- Degree \(9\) would require \(R_q=1/3\), impossible because
  \(v_3(R_q)=q+1\).
- Degree \(6\) would require \(R_q=108/5\).  Comparing 3-adic valuations
  forces \(q=2\); but \(N_A(2)=5\), \(N_B(2)=1\), and
  \(R_2=27/125\ne108/5\).

Therefore none of Müller's exceptional rational monodromy polynomials is
linearly equivalent to any \(P_{q,m}\).

---

## 5. Monodromy theorem

Let

\[
 G^{\mathrm{geom}}_{q,m}
 :=\operatorname {Gal}
 \bigl(P_{q,m}(X)-T\,/\,\overline{\mathbf Q}(T)\bigr),
\]

\[
 G^{\mathrm{arith}}_{q,m}
 :=\operatorname {Gal}
 \bigl(P_{q,m}(X)-T\,/\,\mathbf Q(T)\bigr),
\]

where `Gal` denotes the Galois group of the splitting field.

We use the rational-coefficient form of Müller's classification: the
geometric monodromy of an indecomposable polynomial in \(\mathbf Q[X]\) is
alternating or symmetric, cyclic, dihedral, or belongs to one of the three
explicit rational exceptional cases above.  Linear equivalence is taken over
\(\mathbf C\), equivalently here over \(\overline{\mathbf Q}\).  Theorems 5
and Sections 3--4 remove every case except alternating and symmetric.

### Theorem 6 (uniform alternating/symmetric reduction)

For all \(q\geq1\) and \(m\geq3\),

\[
 G^{\mathrm{geom}}_{q,m}\in\{A_m,S_m\}.
\]

In fact \(G^{\mathrm{geom}}_{q,3}=S_3\) by the degree-3 observation in
Section 3.  For \(m=2\), both geometric and arithmetic groups are \(S_2\).

The discriminant is

\[
 D_{q,m}(T):=\operatorname {Disc}_X(P_{q,m}(X)-T),
\]

and, because \(P_{q,m}\) is monic of degree \(m\),

\[
 \deg_TD_{q,m}=m-1,
\]

\[
 \operatorname {LC}_T D_{q,m}
 =(-1)^{m(m-1)/2+m-1}m^m.
\]

### Theorem 7 (precise unconditional conclusions)

For every \(q\geq1\):

1. If \(m\) is even, then
   \[
   G^{\mathrm{geom}}_{q,m}
   =G^{\mathrm{arith}}_{q,m}=S_m.
   \]
2. If \(m\) is odd and not a perfect square, then
   \[
   G^{\mathrm{arith}}_{q,m}=S_m,
   \]
   while for odd \(m\ge5\) geometrically the present argument leaves
   \(G^{\mathrm{geom}}_{q,m}=A_m\) or \(S_m\).  Degree \(3\) is already
   \(S_3\).
3. If \(m\) is an odd perfect square, both the arithmetic square-class test
   and the geometric test require additional information.

#### Proof

For even \(m\), the inertia generator at infinity is an \(m\)-cycle and is
odd, so the geometric group cannot be \(A_m\).  Equivalently,
\(D_{q,m}\) has odd degree \(m-1\) and cannot be a square.  Thus both groups
are \(S_m\).

Now let \(m\) be odd.  The square class of the leading coefficient is

\[
 (-1)^{(m-1)/2}m.
\]

If \(m\equiv3\pmod4\), this is negative and hence not a rational square.  If
\(m\equiv1\pmod4\) but \(m\) is not a square, it is again not a rational
square.  Therefore \(D_{q,m}(T)\) is not a square in \(\mathbf Q(T)\), so
the arithmetic group is not contained in \(A_m\).  Since the geometric group
is \(A_m\) or \(S_m\), the arithmetic group is \(S_m\).

Finally, every odd square is \(1\pmod8\), so its displayed leading
coefficient is itself a square and \(m-1\) is even.  The leading-term test
then gives no conclusion. \(\square\)

---

## 6. The remaining boundary

The exact unresolved boundary of the uniform proof is therefore:

- **arithmetic:** odd perfect-square degrees \(m\ge9\);
- **geometric:** odd degrees \(m\ge5\), where one must distinguish \(A_m\)
  from \(S_m\).

These are different questions.  A nonsquare rational constant multiplying a
square polynomial can make the arithmetic group \(S_m\) while the geometric
group remains \(A_m\).  To prove geometric \(S_m\), one must show that
\(D_{q,m}(T)\) is not of the form

\[
 cR(T)^2,
 \qquad c\in\mathbf Q^\times, R\in\mathbf Q[T].
\]

For the original order \(q=1\), exact finite-field certificates currently
prove

\[
 G^{\mathrm{geom}}_{1,m}=G^{\mathrm{arith}}_{1,m}=S_m
 \qquad(2\leq m\leq401).
\]

For odd \(57\leq m\leq401\), the certificate uses two regular
specializations modulo \(409\) at which the discriminant has opposite
quadratic characters; this rules out \(cR(T)^2\).  The reproducible code and
the lower-order exact-Morse certificates are in

- `output/research/trace_galois_401.py`,
- `output/research/trace_morse_certificates.py`,
- `output/research/TRACE_MORSE_EXACT_CERTIFICATES.md`.

This finite verification does not replace an all-\(m\) proof and should be
reported as a certified range.

---

## Reference

P. Müller, “Primitive monodromy groups of polynomials,” in *Recent
Developments in the Inverse Galois Problem*, Contemporary Mathematics **186**
(1995), 385--401.

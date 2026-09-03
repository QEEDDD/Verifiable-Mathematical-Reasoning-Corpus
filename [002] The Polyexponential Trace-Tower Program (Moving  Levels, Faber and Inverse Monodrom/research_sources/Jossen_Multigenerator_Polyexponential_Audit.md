# Multigenerator Jossen audit for the resonant polyexponential algebra

**Status:** rigorous reduction plus two complete non-cyclic subclasses.  This note does **not** claim the full Jossen conjecture for the algebra below.

## 1. The algebra and the arithmetic generic-point theorem

Put

\[
  E_{q,\lambda}(z)=\operatorname{Ein}_q(\lambda z),\qquad
  \mathscr A=\overline{\mathbf Q}
  [E_{q,\lambda}:q\ge 1,\ \lambda\in\overline{\mathbf Q}^{\times}],
\]

and let

\[
  K_{\exp}=\overline{\mathbf Q}
  (e^\alpha:\alpha\in\overline{\mathbf Q}).
\]

Only finitely many generators occur in any element of \(\mathscr A\).

### Theorem 1.1 (polynomiality and algebraic-time genericity)

After identifying repeated pairs \((q,\lambda)\), the functions
\(E_{q,\lambda}\) are algebraically independent over
\(\overline{\mathbf Q}\).  Hence

\[
  \mathscr A\simeq
  \overline{\mathbf Q}[X_{q,\lambda}]
\]

is a polynomial UFD in the finite-subset sense.

For every \(\beta\in\overline{\mathbf Q}^{\times}\), evaluation at \(z=\beta\)
is injective on \(\mathscr A\), and the point

\[
  \Phi(\beta)=
  (\operatorname{Ein}_q(\lambda\beta))_{q,\lambda}
\]

is a generic point over \(K_{\exp}\): every finite set of its distinct
coordinates is algebraically independent over \(K_{\exp}\).

Consequently, if \(F\in\mathscr A\) is nonconstant, then

\[
  F(\beta)\notin K_{\exp}
  \quad(\beta\in\overline{\mathbf Q}^{\times}).                 \tag{1.1}
\]

More generally, \(\Phi(\beta)\) misses every proper algebraic subvariety
defined over \(K_{\exp}\).

#### Proof

Apply Theorem 8.3 and Corollary 8.4 of 001 to the finitely many pairs
occurring in a proposed relation, with the arguments \(\lambda\beta\).
They are distinct exactly when the corresponding \(\lambda\)'s are distinct,
and the theorem simultaneously includes all selected orders \(q\).  A
functional polynomial relation would specialize at any fixed nonzero
algebraic \(\beta\), contradicting the value theorem.  The remaining claims
are immediate.

This is stronger than ordinary Zariski density: **every** nonzero algebraic
time is generic.  It does not say anything comparable at a transcendental
time.

### Corollary 1.2 (complete algebraic-zero exclusion)

For nonconstant \(F\in\mathscr A\) and \(a\in K_{\exp}\), every zero of
\(F(z)-a\), other than a possible zero at \(z=0\), is transcendental.
In particular, no nonzero element of \(\mathscr A\) has a nonzero algebraic
zero.

### Proposition 1.3 (every fiber is infinite)

For every nonconstant \(F\in\mathscr A\) and every \(a\in\mathbf C\), the
fiber

\[
  \{z\in\mathbf C:F(z)=a\}
\]

is infinite.

#### Proof

Every element of \(\mathscr A\) is an E-function and is of exponential type,
hence has order at most one.  If \(F-a\) had only finitely many zeros,
Hadamard factorization would give

\[
  F(z)-a=e^{Az+B}R(z)                                      \tag{1.2}
\]

with \(R\in\mathbf C[z]\).

The functional proof of 001, Lemmas 8.1--8.2, is unchanged after adjoining
one extra exponential \(e^{Az}\): take a \(\mathbf Z\)-basis of the finitely
generated additive group spanned by \(A\) and all slopes \(\lambda\) occurring
in \(F\), and repeat the Laurent-character/Darboux-polynomial argument.
Thus the selected \(E_{q,\lambda}\)'s remain algebraically independent over

\[
  \mathbf C(z,e^{Az},e^{\lambda z}:\lambda\text{ selected}).
\]

Equation (1.2) is a nontrivial polynomial relation over this field, a
contradiction.

## 2. Exact reduction of both parts of Jossen's conjecture

Let \(F,G\in\mathscr A\setminus\{0\}\).  Since only finitely many variables
occur, their gcd \(D=\gcd_{\mathscr A}(F,G)\) is well-defined.  Write

\[
  F=DF_0,\qquad G=DG_0,\qquad \gcd_{\mathscr A}(F_0,G_0)=1.    \tag{2.1}
\]

### Theorem 2.1 (the exact remaining common-zero obstruction)

1. Neither \(F_0\) nor \(G_0\) can vanish at a nonzero algebraic point.
2. If \(F_0(0)=G_0(0)=0\), the common zero at the origin is explained by
   the nonunit E-function \(h(z)=z\): both \(F_0/z\) and \(G_0/z\) are
   E-functions.
3. Therefore the only unresolved case of Jossen part (ii) for
   \(\mathscr A\) is a **nonzero transcendental** point \(\xi\) satisfying

   \[
     F_0(\xi)=G_0(\xi)=0.                                  \tag{2.2}
   \]

Equivalently, for a finite coordinate map \(\Phi:\mathbf C\to\mathbf A^n\),
the hard locus is the transcendental-time pullback

\[
  \Phi^{-1}(V(P,Q)),\qquad \operatorname{codim}V(P,Q)\ge2,  \tag{2.3}
\]

for coprime \(P,Q\in\overline{\mathbf Q}[X_1,\ldots,X_n]\).

The factor \(z\) in item 2 is standard E-function zero removal at the
algebraic point zero.  The novelty of the reduction is that 001 removes all
other algebraic times simultaneously.

### Theorem 2.2 (an entire-quotient counterexample would be infinite)

Assume \(F/G\) is entire.  With (2.1), exactly one of the following occurs.

* \(G_0\) is constant, in which case \(F/G=F_0/G_0\in\mathscr A\), so
  Jossen part (i) holds inside \(\mathscr A\).
* \(G_0\) is nonconstant.  Then \(G_0\) has infinitely many zeros by
  Proposition 1.3, every one of them is a zero of \(F_0\), and all but a
  possible zero at the origin are transcendental.  Thus a failure of
  divisibility in \(\mathscr A\) would force an **infinite transcendental
  codimension-two intersection carrying the complete divisor of \(G_0\)**.

This is a useful sharpening of the gate: one isolated mysterious root is the
obstruction for part (ii), whereas part (i) requires an infinite divisor-sized
exceptional intersection.

### Origin contact and transversality

For a finite list \(E_i=E_{q_i,\lambda_i}\),

\[
  E_i(z)=\lambda_i z+O(z^2).
\]

Let \(P_d\) be the first nonzero homogeneous part of
\(P\in\overline{\mathbf Q}[X_1,\ldots,X_n]\).  If

\[
  P_d(\lambda_1,\ldots,\lambda_n)\ne0,
\]

then

\[
  \operatorname{ord}_{z=0}P(E_1(z),\ldots,E_n(z))=d.          \tag{2.4}
\]

In particular, the origin is a simple zero precisely under the familiar
first-order transversality condition

\[
  \sum_i\lambda_i\partial_iP(0)\ne0.                         \tag{2.5}
\]

If the expression in (2.5) vanishes, higher jets give an effective valuation
algorithm.  This completely settles the algebraic-time Jacobian question but
does not control (2.2).

## 2A. A general affine E-surface theorem

There is a substantially broader two-dimensional closure that does not use
any special identity of \(\operatorname{Ein}\).

### Theorem 2A.1 (factorial E-surface criterion)

Let \(B\) be a finitely generated factorial
\(\overline{\mathbf Q}\)-domain of Krull dimension two, embedded as a
subring of the ring of E-functions.  Assume that \(B\) contains at least one
nonconstant polynomial coordinate

\[
  \tau(z)\in\overline{\mathbf Q}[z].
\]

Then both parts of Jossen's conjecture hold for every nonzero
\(f,g\in B\) (so in particular the quotient below has \(g\ne0\)):

1. if \(f/g\) is entire, then \(f/g\) is an E-function;
2. if \(f\) and \(g\) have a common zero, they have a common nonunit
   E-function divisor.

#### Proof of the common-zero assertion

Take a gcd in the UFD \(B\):

\[
  f=df_0,\qquad g=dg_0,\qquad \gcd_B(f_0,g_0)=1.             \tag{2A.1}
\]

Let \(\xi\) be a common zero.  If \(d(\xi)=0\), then \(d\) itself is a
nonunit E-function divisor of \(f\) and \(g\).

Assume \(d(\xi)\ne0\).  Then \(f_0(\xi)=g_0(\xi)=0\).  Since \(f_0,g_0\)
are nonzero and \(B\) is a factorial domain, neither the height-zero prime nor
any height-one prime contains both of them.  Hence every prime over
\((f_0,g_0)\) has height two.  Because \(\dim B=2\),

\[
  B/(f_0,g_0)
\]

is a zero-dimensional affine \(\overline{\mathbf Q}\)-algebra.  The kernel
of evaluation at \(\xi\) is a prime over \((f_0,g_0)\), hence is maximal.
By Zariski's lemma its residue field is algebraic over
\(\overline{\mathbf Q}\), hence equals \(\overline{\mathbf Q}\).  In particular
\(\tau(\xi)\in\overline{\mathbf Q}\).  Since \(\xi\) is a root of the
nonzero polynomial \(\tau(T)-\tau(\xi)\), this proves
\(\xi\in\overline{\mathbf Q}\).

If \(\xi\ne0\), Beukers's algebraic-point zero-removal proposition gives

\[
  \frac{f_0(z)}{z-\xi},\qquad
  \frac{g_0(z)}{z-\xi}
\]

as E-functions; for \(\xi=0\), the same conclusion follows directly by
shifting the Taylor coefficients of an E-function that vanishes at the
origin.  Thus \(z-\xi\) is the required common nonunit E-function
divisor (after multiplying the displayed quotients by \(d\)).

#### Proof of the entire-quotient assertion

Cancel \(d\) as in (2A.1); the cancelled quotient extends to the same entire
function across the zeros of \(d\).  If \(f_0/g_0\) is entire, every zero of \(g_0\)
is a common zero of \(f_0,g_0\).  The zero-dimensional scheme above has only
finitely many closed points.  Each such point fixes an algebraic value of
\(\tau\), and a nonconstant polynomial has finite fibers.  Thus \(g_0\) has
finitely many zeros, all algebraic.  Let

\[
  r(z)=\prod_\xi(z-\xi)^{\operatorname{ord}_\xi g_0}
  \in\overline{\mathbf Q}[z].                               \tag{2A.2}
\]

Repeated algebraic-point zero removal shows that \(g_0/r\) is a zero-free
E-function.  A zero-free entire function of order at most one is
\(Ce^{az}\) by Hadamard factorization.  Here

\[
  C=(g_0/r)(0)\in\overline{\mathbf Q}^{\times},\qquad
  a=(g_0/r)'(0)/(g_0/r)(0)\in\overline{\mathbf Q},
\]

so \(g_0/r=Ce^{az}\) is a unit E-function.  Entirety also gives
\(\operatorname{ord}_\xi f_0\ge\operatorname{ord}_\xi g_0\), hence
\(f_0/r\) is an E-function.  Finally,

\[
  \frac fg=\frac{f_0/r}{Ce^{az}}
\]

is an E-function.

### Corollary 2A.2 (one arbitrary E-function plus \(z\))

Let \(F\) be any nonpolynomial E-function.  Then \(z\) and \(F(z)\) are
algebraically independent: an entire function algebraic over
\(\overline{\mathbf Q}(z)\) is a polynomial.  Consequently

\[
  B_F=\overline{\mathbf Q}[z,F(z)]
  \simeq\overline{\mathbf Q}[X,Y]
\]

is a factorial affine E-surface, and **both parts of Jossen's conjecture hold
unconditionally throughout \(B_F\)**.

In direct plane language, if coprime \(P,Q\in\overline{\mathbf Q}[X,Y]\)
have a common pullback zero \(\xi\), then
\((\xi,F(\xi))\in V(P,Q)\).  The plane intersection is finite and defined
over \(\overline{\mathbf Q}\), so \(\xi\) is algebraic and \(z-\xi\) is the
common E-factor.  For an entire quotient, the same finite intersection traps
all denominator zeros and the preceding Hadamard argument completes the
proof.

Equivalently, for arbitrary \(P,Q\) and
\(D=\gcd(P,Q)\), one has the exact set-theoretic decomposition

\[
 \begin{aligned}
 Z(P(z,F))\cap Z(Q(z,F))
  ={}& Z(D(z,F))\\
    &{}\cup S_{P,Q,F},
 \end{aligned}                                                \tag{2A.3}
\]

where \(S_{P,Q,F}\) is a finite set of algebraic numbers.  Thus every
transcendental common zero is automatically carried by the explicit common
E-factor \(D(z,F)\); only finitely many algebraic residual points require the
linear factors \(z-\xi\).

The polynomial case reduces to the univariate algebra
\(\overline{\mathbf Q}[z]\) and is elementary.  Thus the corollary holds for
every E-function \(F\), with the nonpolynomial case being the genuinely
two-dimensional one.

More generally, if \(\tau\in\overline{\mathbf Q}[z]\) is any nonconstant
polynomial and \(F\) is a nonpolynomial E-function, then \(\tau(z),F(z)\)
are algebraically independent (otherwise \(F\) would be algebraic over
\(\overline{\mathbf Q}(z)\)).  Therefore

\[
  \overline{\mathbf Q}[\tau(z),F(z)]
\]

also satisfies both parts of Jossen.

For \(F=e^{\beta z}\), this recovers the familiar one-support exponential-
polynomial situation.  The point of Corollary 2A.2 is that no exponential,
hypergeometric, differential-order, or zero-geometry assumption on \(F\) is
needed beyond the E-function axioms.

In particular, every nonconstant \(F\in\mathscr A\) is nonpolynomial (by the
functional independence in 001), and hence

\[
  \boxed{\overline{\mathbf Q}[z,F]\text{ satisfies both parts of Jossen}}
                                                                  \tag{2A.4}
\]

for **every single polyexponential polynomial observable** \(F\).  This is a
strict extension of the cyclic result
\(\overline{\mathbf Q}[F]\): the numerator and denominator may depend
independently on the physical variable \(z\) and on \(F(z)\).

This surface theorem explains precisely why adding a second independent
polyexponential beyond \(z,F\) changes the problem: in Krull dimension three,
two coprime equations can leave a positive-dimensional intersection, and the
argument forcing \(\xi\) algebraic disappears.

### Corollary 2A.3 (holonomic transfer)

The proof is not intrinsically restricted to Siegel E-functions.  Let
\(\mathcal H_{\overline{\mathbf Q}}^{\mathrm{fin}}\) be the ring of
finite-order entire functions that are D-finite over
\(\overline{\mathbf Q}(z)\) and have algebraic Taylor coefficients.  It is
closed under sums and products and under division by \(z-\xi\) at an
algebraic zero, with finite order preserved.  A zero-free finite-order entire
function \(h\) is \(Ce^{A(z)}\) with \(A\) a polynomial.  Normalize this
representation by taking \(A(0)=0\) and \(C=h(0)\).  Then
\(C\in\overline{\mathbf Q}^{\times}\), and the formal logarithm of \(h/C\)
shows that \(A\in\overline{\mathbf Q}[z]\).  Hence \(h^{-1}=C^{-1}e^{-A(z)}\)
is again D-finite of finite order with algebraic Taylor coefficients.

Therefore Theorem 2A.1, with "E-function" replaced by "finite-order entire
D-finite function with algebraic Taylor coefficients," remains valid.  In
particular, every factorial affine holonomic surface containing a nonconstant
polynomial coordinate is closed under its entire quotients and has the same
common-zero factor property.  This is an elementary algebraic--analytic
transfer to the holonomic setting.

## 3. A complete genuinely bivariate blow-up subclass inside \(\mathscr A\)

The next result is not merely cyclic in one generator.  It exhibits the
geometric mechanism by which a codimension-two point becomes an E-divisor.

Choose

\[
  H(z)=\operatorname{Ein}(\lambda z),\qquad
  R(z)=\operatorname{Ein}_p(\mu z),
\]

with \((p,\mu)\ne(1,\lambda)\), and fix
\(a\in\overline{\mathbf Q}\), \(m\ge1\).  Theorem 1.1 makes \(H,R\)
algebraically independent.  Put

\[
  U=a+H^mR.                                                   \tag{3.1}
\]

Then \(H,U\) are also algebraically independent, so
\(\mathscr B=\overline{\mathbf Q}[H,U]\) is a genuine polynomial
two-generator subalgebra of \(\mathscr A\).

For \(0\ne P\in\overline{\mathbf Q}[X,Y]\), expand

\[
  P(X,a+Y)=\sum_{i,j\ge0}c_{ij}X^iY^j
\]

and define the weighted exceptional valuation

\[
  \nu_m(P)=\min\{i+mj:c_{ij}\ne0\}.                          \tag{3.2}
\]

### Theorem 3.1 (exact pullback gcd)

If \(P,Q\in\overline{\mathbf Q}[X,Y]\) are coprime, then, up to a nonzero
algebraic constant,

\[
 \gcd_{\mathscr A}\bigl(P(H,U),Q(H,U)\bigr)
 =H^{\min(\nu_m(P),\nu_m(Q))}.                               \tag{3.3}
\]

#### Proof

Substitution gives

\[
  P(H,U)=\sum c_{ij}H^{i+mj}R^j
         =H^{\nu_m(P)}P^\sharp(H,R),
\]

where \(P^\sharp\) is not divisible by \(H\).  After inverting \(H\), the
substitution is the isomorphism

\[
 \overline{\mathbf Q}[X,Y,X^{-1}]
 \xrightarrow{\sim}
 \overline{\mathbf Q}[H,R,H^{-1}],
 \quad X\mapsto H,\quad Y\mapsto a+H^mR,
\]

whose inverse sends \(R\) to \((Y-a)/X^m\).  Coprimality therefore forbids
every common irreducible factor other than \(H\), and (3.3) follows.

### Corollary 3.2 (complete Jossen common-zero theorem at the contracted point)

Assume

\[
  \sqrt{(P,Q)}=(X,Y-a),                                      \tag{3.4}
\]

so the affine complete intersection of \(P\) and \(Q\) is exactly the point
\((0,a)\).  Then

\[
 \{P(H,U)=Q(H,U)=0\}=\{H=0\}.                               \tag{3.5}
\]

The right side is infinite; zero is its only algebraic point, and all its
other points are transcendental.  Every zero is simple.  All of these common
zeros, including the transcendental ones, are explained by the explicit
nonunit E-function factor in (3.3).  Thus Jossen part (ii) holds completely
for this bivariate class.

Indeed,

\[
 H'(z)=\frac{1-e^{-\lambda z}}z.
\]

A multiple nonzero zero would have \(\lambda z=2\pi ik\).  But

\[
 \Re\operatorname{Ein}(2\pi ik)
 =\int_0^1\frac{1-\cos(2\pi kt)}t\,dt>0\qquad(k\ne0),         \tag{3.6}
\]

so this is impossible.  The zero at zero is simple because \(H'(0)=\lambda\).
There are infinitely many zeros since otherwise Hadamard factorization would
make \(H=e^{Az+B}S(z)\) and hence \(H'\) would have only finitely many zeros,
whereas \(H'(2\pi ik/\lambda)=0\) for every \(k\ne0\).  Their transcendence
follows from Theorem 1.1.

A basic example is

\[
  P=X,\qquad Q=Y-a,
\]

for which the coprime bivariate pair pulls back to

\[
  H,\qquad H^mR.
\]

It has infinitely many transcendental common zeros, but the common factor is
exactly \(H\).  Geometrically, (3.1) contracts the divisor \(H=0\) to the
codimension-two point \((0,a)\); Jossen's factor is the exceptional divisor.

### Theorem 3.3 (an exact non-cyclic entire-quotient window)

Let \(1\le\nu\le m\) and \(P\in\overline{\mathbf Q}[X,Y]\setminus\{0\}\).
Then

\[
 \frac{P(H,U)}{H^\nu}\text{ is entire}
 \quad\Longleftrightarrow\quad
 \partial_X^jP(0,a)=0\quad(0\le j<\nu)                     \tag{3.7}
\]

and, whenever these equivalent conditions hold,

\[
  \frac{P(H,U)}{H^\nu}\in\mathscr A.                        \tag{3.8}
\]

Hence Jossen part (i) holds for this whole bivariate numerator class and the
denominators \(H^\nu\), \(1\le\nu\le m\).

#### Proof

For weights strictly below \(\nu\le m\), only the pure terms \(c_{i0}X^i\)
can occur in (3.2); every term involving \(Y-a\) acquires a factor \(H^m\).
Thus the derivative conditions in (3.7) are equivalent to
\(\nu_m(P)\ge\nu\), which makes the quotient in (3.8) a polynomial in
\(H,R\).  If one derivative does not vanish, the first offending pure
\(H^i\)-term produces a pole at every simple zero of \(H\).  This proves the
reverse implication.

For example,

\[
  \frac{U-a}{H^m}=R
\]

recovers an independent polyexponential coordinate as an entire E-function
quotient; this is not contained in the cyclic algebra
\(\overline{\mathbf Q}[H]\).

## 4. A natural differential two-generator subclass

Let

\[
  H=\operatorname{Ein}(\lambda z),\qquad
  \Theta H=zH'=1-e^{-\lambda z}.
\]

The pair \((H,\Theta H)\) is algebraically independent over
\(\overline{\mathbf Q}\), by the functional exponential/polyexponential
theorem in 001.  Equation (3.6) proves

\[
  \{H=0\}\cap\{\Theta H=0\}=\{0\}.                          \tag{4.1}
\]

Consequently, for any \(P,Q\in\overline{\mathbf Q}[X,Y]\) satisfying

\[
  \sqrt{(P,Q)}=(X,Y),                                       \tag{4.2}
\]

the common-zero set of \(P(H,\Theta H)\) and
\(Q(H,\Theta H)\) is exactly \(\{0\}\), and the common zero is explained by
the E-function factor \(z\).  This is a complete non-cyclic common-zero
theorem in the first differential closure of \(\mathscr A\).

There is also a broad imported quotient theorem.  Fischler--Rivoal prove that
if \(g^r\) is an E-function and \(L\in\overline{\mathbf Q}(z)[d/dz]\) is such
that \(L(g)/g\) is entire, then \(L(g)/g\) is a polynomial.  Thus Jossen part
(i) holds for every pair \((L(G),G)\) lying in \(\mathscr A^2\).  For example,
\(\Theta\) maps

\[
 \overline{\mathbf Q}[\operatorname{Ein}_q(\lambda z):q\ge2]
 \quad\text{into}\quad\mathscr A.
\]

For a nonconstant \(G\) in this subalgebra, \(\Theta G/G\) is in fact never
entire: Proposition 1.3 supplies a nonzero zero of \(G\), and the logarithmic
derivative has a pole there.

## 5. Why the full multigenerator statement is still open

### 5.1 Algebraic independence is not codimension-two avoidance

An algebraically nondegenerate finite-order entire curve can meet a
codimension-two target infinitely often.  The elementary map

\[
  z\longmapsto(\sin z,z\sin z)
\]

is algebraically nondegenerate and meets \((0,0)\) at every \(z\in\pi\mathbf Z\).
Here the hidden divisor \(\sin z\) explains the intersection.  This is exactly
the sort of divisor that Jossen asks one to recover inside the E-function
ring.  Therefore Theorem 1.1 alone cannot settle (2.3).

### 5.2 Why standard Nevanlinna gcd estimates do not immediately close it

Nevanlinna gcd theorems on algebraic tori give
\(o(T)\)-type bounds for codimension-two intersections under zero-free or
small-zero hypotheses on the coordinate functions.  The polyexponential
coordinates have infinite divisors of their own, so those hypotheses are not
automatic.  Even an \(o(T)\) upper bound would need a matching lower bound for
the zero counting function of every possible denominator \(Q(\Phi)\) before
it could prove Jossen part (i).

Thus a usable Nevanlinna route requires two new ingredients:

1. a gcd estimate adapted to the additive/iterated-integral differential
   group containing the \(\operatorname{Ein}_q\)'s, rather than a torus; and
2. a uniform lower zero-density theorem for every nonconstant element of
   \(\mathscr A\), stronger than Proposition 1.3.

### 5.3 The exact high-tier gate

Any one of the following would be a genuinely high-tier advance.

* **Transcendental codimension-two saturation:** if coprime
  \(P,Q\in\mathscr A\) have a nonzero common root, prove that their pullbacks
  share a nonunit E-function factor (necessarily outside \(\mathscr A\)).
* **Strong avoidance:** prove that a full-\(\mathscr A\)-coprime pair has no
  nonzero common root at all.  This is stronger than Jossen and may be false;
  it should not be asserted without a new zero theorem.
* **Divisor-sized gcd estimate:** for coprime \(P,Q\), show that the common-zero
  counting function is too small to contain the complete divisor of
  \(Q(\Phi)\).  Together with Theorem 2.2 this proves the entire-quotient part.
* **Bourget-type seed:** already the assertion that two distinct primitive
  coordinates \(\operatorname{Ein}_q(\lambda z)\) and
  \(\operatorname{Ein}_p(\mu z)\) have no common nonzero zero is not supplied
  by 001.  Proving it uniformly would be a natural first step.

## 6. Literature boundary and value assessment

Fischler--Rivoal state Jossen's conjecture as follows:

1. if E-functions \(f,g\) have an entire quotient \(f/g\), then that quotient
   is an E-function;
2. if two E-functions have a common root, then they have a common nonunit
   E-function divisor.

They record that part (ii) is known when the common root is algebraic, part
(i) is known for polynomial denominators, and prove the differential-operator
case used above.  Under Schanuel they obtain much stronger common-zero results
for exponential polynomials.  The transcendental-root case for general
E-functions remains the hard boundary.

Primary sources:

* S. Fischler and T. Rivoal, [*Zeros of E-functions and of exponential
  polynomials defined over* \(\overline{\mathbf Q}\)](https://doi.org/10.1007/s12215-026-01475-x),
  *Rend. Circ. Mat. Palermo (2)* **75** (2026), Art. 158; see also the
  [2025 preprint](https://arxiv.org/abs/2503.20345), especially Conjecture 1.1,
  Theorem 1.2, and Sections 5--6.
* F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
  Ann. of Math. 163 (2006), 369--379, especially the algebraic-point
  zero-removal proposition used in Theorem 2A.1.
* A. Levin and J. T.-Y. Wang, [*Greatest common divisors of analytic functions
  and Nevanlinna theory on algebraic tori*](https://arxiv.org/abs/1903.03876).
* 001, Theorem 8.3 and Corollary 8.4, for the resonant value and functional
  independence used throughout.

### Honest tier assessment

* Theorems 1.1, 2.1, and 2.2 give a sharp and useful reduction of the full
  problem, but do not solve it.
* The factorial E-surface theorem 2A.1 is a useful commutative-algebra
  packaging: it proves both parts of Jossen for
  \(\overline{\mathbf Q}[z,F]\) with an arbitrary E-function \(F\), and more
  generally for every factorial affine E-surface containing a nonconstant
  polynomial.  It does not cross the general transcendental-root boundary:
  after taking a gcd, dimension two and the polynomial coordinate force all
  residual roots to be algebraic, reducing the proof to known zero removal
  and the classification of E-function units.  The statement does not appear
  explicitly in Fischler--Rivoal, but it is an elementary, possibly folklore
  wrapper around known ingredients; priority should be checked before any
  novelty claim.
* The blow-up theorem (3.1--3.8) is a real non-cyclic closure, including
  infinitely many transcendental common roots and an exact entire-quotient
  window.  It is suitable as a strong section or companion-note result.
* The differential pointed-complete-intersection theorem (4.1--4.2) is natural
  and complete, but partly rests on an elementary critical-point computation.
* None of these results alone is Annals-level.  Closing the transcendental
  codimension-two saturation gate in Section 5.3 plausibly would be.

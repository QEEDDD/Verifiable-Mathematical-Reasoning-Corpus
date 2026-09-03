# A finite-rank Gamma-jet spectral sieve across all polyexponential orders

**Research status (2026-09-01).**  This note is conditional on the joint
algebraic-independence theorem imported from [001].  Its analytic statements
about the fibers of \(\operatorname{Ein}_q\) use the all-order inverse-surface
theorem proved in the companion research note
`ALL_ORDER_POLYEXPONENTIAL_INVERSE_MONODROMY.md`.  It proves no unconditional
irrationality or transcendence statement about Euler's constant.

Put

\[
 K=\overline{\mathbf Q}
   (e^\xi:\xi\in\overline{\mathbf Q})
\]

and assume the arithmetic input

\[
 \bigl(\operatorname{Ein}_q(\beta)\bigr)_
 {(q,\beta)\in\mathbf N_{\geq1}\times
 \overline{\mathbf Q}^{\times}}
 \quad\text{is jointly algebraically independent over }K        \tag{0.1}
\]

in the finite-subset sense; the coordinate labels are the ordered pairs
\((q,\beta)\).

For positive algebraic \(\alpha\) and \(k\geq0\), define

\[
 U_{\alpha,k}=[s^k]\Gamma(s,\alpha)
 =\frac1{k!}\int_\alpha^\infty
 e^{-u}\frac{(\log u)^k}{u}\,du.                              \tag{0.2}
\]

Writing

\[
 \Gamma(s)=s^{-1}+\sum_{k\geq0}g_ks^k,
\]

the lower/upper incomplete-Gamma splitting gives

\[
 U_{\alpha,k}=g_k+R_{\alpha,k},                                \tag{0.3}
\]

where, with \(L_\alpha=\log\alpha\),

\[
 R_{\alpha,k}=-\frac{L_\alpha^{k+1}}{(k+1)!}
 +\sum_{j=0}^k
 \frac{(-1)^jL_\alpha^{k-j}}{(k-j)!}
 \operatorname{Ein}_{j+1}(\alpha).                            \tag{0.4}
\]

## 1. The all-order spectral sieve

Let \(\Lambda\subset\overline{\mathbf Q}_{\geq1}\) consist of distinct
positive algebraic numbers whose multiplicative span has rank \(r<\infty\).
For \(\alpha\in\Lambda\), \(q\geq1\), and fixed \(k\geq0\), set

\[
 \mathcal D_{\alpha,q,k}
 =\{z\in\mathbf C:
 \operatorname{Ein}_q(z)=U_{\alpha,k}\}.                      \tag{1.1}
\]

> **Theorem 1 (finite-rank all-order spectral sieve).**  Among all pairs
> \((\alpha,q)\in\Lambda\times\mathbf N\), at most \(r+1\) divisors
> \(\mathcal D_{\alpha,q,k}\) contain an algebraic point.  More precisely:
>
> 1. if a divisor contains an algebraic point, that point is its unique real
>    point \(\beta\) in \((0,1)\); in particular it contains no nonreal
>    algebraic point;
> 2. for any fixed \(\alpha\), at most one outer order \(q\) can give such an
>    algebraic point;
> 3. every divisor outside the at most \(r+1\) exceptional pairs is infinite
>    and consists wholly of transcendental numbers.

### Proof

For \(\alpha\geq1\), every integrand in (0.2) is nonnegative and

\[
 \sum_{k\geq0}U_{\alpha,k}
 =\int_\alpha^\infty e^{-u}\,du=e^{-\alpha}.
\]

Consequently

\[
 0<U_{\alpha,k}<e^{-\alpha}\leq e^{-1}.                       \tag{1.2}
\]

On the other hand, the alternating series gives, for every \(q\geq1\),

\[
 \operatorname{Ein}_q(1)
 >1-\frac1{2^{q+1}}\geq\frac34>e^{-1}.                        \tag{1.3}
\]

The real restriction of \(\operatorname{Ein}_q\) is strictly increasing,
vanishes at zero, and is onto.  Therefore the equation
\(\operatorname{Ein}_q(x)=U_{\alpha,k}\) has exactly one real solution,
and (1.2)--(1.3) put it in \((0,1)\).

If a nonreal algebraic \(\beta\) belonged to the divisor, then its distinct
conjugate would also belong to it because \(\operatorname{Ein}_q\) has real
coefficients.  This would give

\[
 \operatorname{Ein}_q(\beta)
 =\operatorname{Ein}_q(\overline\beta),
\]

contradicting (0.1).  Thus any algebraic point is the unique real point just
described.

For fixed \(k\), differentiation under the integral sign gives

\[
 \frac{\partial}{\partial\alpha}U_{\alpha,k}
 =-\frac{e^{-\alpha}(\log\alpha)^k}{k!\alpha}<0
 \quad(\alpha>1),                                             \tag{1.4}
\]

with strict decrease from \(\alpha=1\) as well.  Hence distinct cuts give
distinct levels.  Also, if the same cut \(\alpha\) had algebraic inverse
points \(\beta_1,\beta_2\) at two distinct outer orders \(q_1,q_2\), then

\[
 \operatorname{Ein}_{q_1}(\beta_1)
 =U_{\alpha,k}
 =\operatorname{Ein}_{q_2}(\beta_2),
\]

again contradicting (0.1).  Thus bad pairs use distinct cuts.

Suppose now that \(s\) distinct bad pairs
\((\alpha_i,q_i)\) exist, with algebraic inverse points
\(\beta_i\in(0,1)\).  Let \(X\) be the collection of all source coordinates

\[
 \operatorname{Ein}_j(\alpha_i),
 \qquad 1\leq i\leq s,\quad1\leq j\leq k+1,
\]

and put \(M=|X|\).  The new coordinates

\[
 Y_i=\operatorname{Ein}_{q_i}(\beta_i)=U_{\alpha_i,k}
\]

have mutually distinct coordinate labels, and their labels are disjoint
from those of \(X\), because \(\beta_i\in(0,1)\) while
\(\alpha_i\geq1\).  Assumption (0.1) therefore
gives

\[
 \operatorname{trdeg}_K K(X,Y_1,\ldots,Y_s)=M+s.              \tag{1.5}
\]

Choose logarithms \(\lambda_1,\ldots,\lambda_{r'}\), with
\(r'\leq r\), spanning the logarithms of the selected cuts over
\(\mathbf Q\).  Equations (0.3)--(0.4) show that

\[
 K(X,Y_1,\ldots,Y_s)
 \subset K(X,\lambda_1,\ldots,\lambda_{r'},g_k).
\]

The right side has transcendence degree at most \(M+r'+1\).  Comparison
with (1.5) yields

\[
 s\leq r'+1\leq r+1.                                         \tag{1.6}
\]

Finally, the all-order inverse-surface theorem shows that every fiber of
\(\operatorname{Ein}_q\) is infinite.  This proves the theorem. \(\square\)

## 2. The rank-one cut tower

Fix a positive algebraic \(A>1\) and put \(\alpha_n=A^n\), \(n\geq1\).
Its multiplicative rank is one.

> **Corollary 2 (two-exception theorem across the whole \((n,q)\)-grid).**
> For each fixed \(k\geq0\), among all pairs \((n,q)\in\mathbf N^2\), at
> most two divisors
> \[
>  \operatorname{Ein}_q(z)-U_{A^n,k}
> \]
> contain any algebraic zero.  Every other divisor is infinite and all of
> its zeros are transcendental.

This is stronger than a density-one statement in each row: the total number
of exceptional entries in the entire countable two-dimensional grid is at
most two.

At outer order \(q=1\), every positive real level is regular, because the
critical values of \(\operatorname{Ein}\) are nonreal.  Hence, for fixed
\(k\), all but at most two of

\[
 \operatorname{Ein}(z)-U_{A^n,k}
\]

are infinite, simple, pairwise disjoint divisors consisting wholly of
transcendental points.  Their inverse monodromy is the full finitary
symmetric group.

The most classical row is \(k=0\):

\[
 U_{A^n,0}=E_1(A^n).
\]

Thus, for example, among every divisor

\[
 \operatorname{Ein}_q(z)-E_1(2^n),
 \qquad n,q\geq1,
\]

at most two can contain an algebraic point.

## 3. A cofinite algebraically independent spectral forest

The fixed-order upper-jet defect theorem from the Moving-Level manuscript
says that, after deleting at most \(r+1\) cuts, the levels
\(U_{\alpha,k}\) are algebraically independent over \(K\).  Delete also the
at most \(r+1\) cuts occurring in Theorem 1.  We obtain:

> **Corollary 3 (cofinite all-transcendental trace forest).**  There is a
> subset \(E\subset\Lambda\), \(|E|\leq2r+2\), such that:
>
> * the levels \(\{U_{\alpha,k}:\alpha\in\Lambda\setminus E\}\) are jointly
>   algebraically independent over \(K\);
> * for every \(\alpha\notin E\) and every \(q\geq1\), the divisor
>   \(\mathcal D_{\alpha,q,k}\) consists wholly of transcendental points;
> * if one chooses arbitrary orders \(q_\alpha\geq1\) and
>   \(m_\alpha\geq2\), then the reciprocal traces
>   \[
>    T_{q_\alpha,m_\alpha}(U_{\alpha,k})
>    =P_{q_\alpha,m_\alpha}(U_{\alpha,k}^{-1})
>   \]
>   are jointly algebraically independent over \(K\).

For the tower \(A^n\), one may take \(|E|\leq4\).  At \(q=1\) this gives a
cofinite family of pairwise disjoint, simple, wholly transcendental spectral
divisors whose arbitrary one-trace transversal is jointly algebraically
independent.

The last assertion follows because every
\(P_{q,m}(X)\in\mathbf Q[X]\) is a nonconstant monic polynomial: adjoining
\(P_{q,m}(U^{-1})\) makes \(U\) algebraic, so separate independent level
coordinates remain independent after the coordinatewise polynomial maps.

## 4. Extremal rigidity

The defect bound also records exactly what two exceptional algebraic roots
would cost.

> **Corollary 4 (two exceptions force Euler--logarithm independence).**
> Let \(A>1\) be algebraic.  If, at one fixed \(k\), two distinct pairs
> \((n_1,q_1)\), \((n_2,q_2)\) have algebraic inverse points, then
> \[
>  \log A\quad\text{and}\quad g_k
> \]
> are algebraically independent over \(K\).  For \(k=0\), since
> \(g_0=-\gamma\), this forces
> \[
>  \boxed{\ \gamma\text{ and }\log A
>  \text{ jointly algebraically independent over }K.\ }
> \]

Indeed, with two bad pairs, equality holds at both ends of the
transcendence-degree comparison:

\[
 M+2
 =\operatorname{trdeg}_K K(X,Y_1,Y_2)
 \leq\operatorname{trdeg}_K K(X,\log A,g_k)
 \leq M+2.
\]

Thus \(\log A,g_k\) are algebraically independent even over \(K(X)\).
This is a conditional fork, not a proof of the transcendence of
\(\gamma\).

## 5. Significance and boundary

The result is a Diophantine finiteness theorem for algebraic inverse images
of explicit upper incomplete-Gamma jets.  Its distinctive point is the
quantifier order: the \(r+1\) bound holds **simultaneously over every outer
polyexponential order \(q\)**.  In rank one, a two-parameter infinite grid
has at most two algebraically contaminated divisors.

The bound is the strongest conclusion available from (0.1) without new
information on the \(r\) logarithmic coordinates and the single Gamma
coefficient \(g_k\).  Removing the last \(r+1\) possibilities would require
genuinely new arithmetic input; the extremal rigidity corollary explains
why Euler's constant already appears at \(k=0\).

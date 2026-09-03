# Order-axis Hankel double scaling: exact ramp equilibrium, free energy, and arithmetic phase transition

## 0. Scope and normalization

For \(\alpha>0\), put

\[
w_\alpha(y)=1-e^{-\alpha e^{-y}},\qquad
\mu_{\alpha,k}=\int_0^\infty y^k w_\alpha(y)\,dy
=k!\,\Ein_{k+1}(\alpha),
\]

and define the size-\(N\) order-axis Hankel determinant

\[
H_N(\alpha)=\det[\mu_{\alpha,i+j}]_{i,j=0}^{N-1}.
\]

The purpose of this note is to close the simultaneous limit

\[
\frac{\log\alpha_N}{N}\longrightarrow c\in\mathbf R
\]

at the level of the equilibrium measure, zero distribution, determinant
free energy, and the transition from Marchenko--Pastur to arcsine behavior.
The final section records the arithmetic strengthening supplied by [001].

Throughout,

\[
\mathcal I_c(\mu)
=\int_0^\infty (x-c)_+\,d\mu(x)
-\iint\log|x-y|\,d\mu(x)d\mu(y),
\]

and \(\mathcal F(c)=\inf_{\mu\in\mathcal P([0,\infty))}\mathcal I_c(\mu)\).

---

## 1. Master theorem

### Theorem 1 (exact order-axis double-scaling law)

Let \(\alpha_N>0\) and assume

\[
c_N:=\frac{\log\alpha_N}{N}\longrightarrow c\in\mathbf R.
\]

Then:

1. The effective fields after \(y=Nx\),

   \[
   Q_N(x)=-\frac1N\log w_{\alpha_N}(Nx),
   \]

   converge uniformly on \([0,\infty)\) to

   \[
   V_c(x)=(x-c)_+.
   \]

2. The normalized zero-counting measures of the degree-\(N\) monic
   orthogonal polynomials for \(w_{\alpha_N}(y)dy\), after division of their
   zeros by \(N\), converge weakly to the unique minimizer \(\mu_c\) of
   \(\mathcal I_c\).

3. The Hankel determinant satisfies

   \[
   \boxed{\ \log H_N(\alpha_N)
   =N^2\log N-N^2\mathcal F(c)+o(N^2).\ }
   \]

4. For \(c\le0\),

   \[
   d\mu_c(x)=\frac1{2\pi}\sqrt{\frac{4-x}{x}}\,
   \mathbf1_{(0,4)}(x)\,dx,
   \qquad
   \mathcal F(c)=\frac32-c.
   \]

5. For \(c>0\), let \(\phi=\phi(c)\in(0,\pi/2)\) be the unique solution

   \[
   \boxed{\ c=\frac{2\pi\cos^2\phi}
   {\phi+\sin\phi\cos\phi}.\ } \tag{1.1}
   \]

   Set

   \[
   D(\phi)=\phi+\sin\phi\cos\phi,
   \qquad
   b=b(c)=\frac{2\pi}{D(\phi)}.
   \tag{1.2}
   \]

   Thus \(c=b\cos^2\phi\) and \(b-c=b\sin^2\phi\). The support is exactly
   \([0,b]\), and on \(0<x<b\), \(x\ne c\), its density is

   \[
   \boxed{
   \begin{aligned}
   \rho_c(x)
   &=\frac{\phi}{\pi^2}\sqrt{\frac{b-x}{x}}\\
   &\quad+\frac1{2\pi^2}
   \log\left|
   \frac{\sqrt{c(b-x)}+\sqrt{(b-c)x}}
        {\sqrt{c(b-x)}-\sqrt{(b-c)x}}
   \right|.
   \end{aligned}} \tag{1.3}
   \]

   Equivalently,

   \[
   \rho_c(x)=\frac1{2\pi^2}\sqrt{\frac{b-x}{x}}
   \left[
   2\phi+\sqrt{\frac{x}{b-x}}
   \log\left|
   \frac{\cot\phi+\sqrt{x/(b-x)}}
        {\cot\phi-\sqrt{x/(b-x)}}
   \right|
   \right]. \tag{1.4}
   \]

6. The mass lying in the linearly confined part of the potential is

   \[
   \boxed{\ p(c):=\mu_c([c,b])
   =\frac{b\phi^2}{\pi^2}
   =\frac{2\phi^2}{\pi D(\phi)}.\ } \tag{1.5}
   \]

7. The equilibrium free energy is

   \[
   \boxed{
   \mathcal F(c)=
   \frac32+\log\frac{2D(\phi)}\pi
   -\frac{2\phi\cos^2\phi
   \bigl(2\phi+\sin\phi\cos\phi\bigr)}{D(\phi)^2},
   \qquad c>0.} \tag{1.6}
   \]

   It obeys the envelope identity

   \[
   \mathcal F'(c)=-p(c). \tag{1.7}
   \]

---

## 2. Uniform reduction to the ramp potential

For every \(t>0\),

\[
(1-e^{-1})\min(1,t)\le1-e^{-t}\le\min(1,t).
\]

Taking \(t=\alpha_Ne^{-Nx}\) gives the uniform bounds

\[
(x-c_N)_+
\le Q_N(x)
\le(x-c_N)_++\frac{-\log(1-e^{-1})}{N}. \tag{2.1}
\]

Since

\[
\sup_{x\ge0}|(x-c_N)_+-(x-c)_+|\le|c_N-c|,
\]

the convergence \(Q_N\to V_c\) is uniform on the whole half-line, not
merely locally away from the kink.

Heine's identity and \(y_i=Nx_i\) give

\[
H_N(\alpha_N)
=\frac{N^{N^2}}{N!}
\int_{[0,\infty)^N}\Delta(x)^2
\prod_{j=1}^N e^{-NQ_N(x_j)}\,dx_j. \tag{2.2}
\]

The logarithmic-gas Laplace principle, together with (2.1), yields

\[
\frac1{N^2}\log\frac{H_N(\alpha_N)}{N^{N^2}}
\longrightarrow-\mathcal F(c). \tag{2.3}
\]

Here is the short triangular-array reduction implicit in this step. Put

\[
\delta_N=\lVert Q_N-V_c\rVert_{L^\infty([0,\infty))}=o(1)
\]

and let \(Z_N[Q]\) denote the \(N\)-particle integral in (2.2), with
\(Q_N\) replaced by \(Q\). Direct comparison of the integrands gives

\[
e^{-N^2\delta_N}Z_N[V_c]
\le Z_N[Q_N]\le
e^{N^2\delta_N}Z_N[V_c]. \tag{2.4}
\]

Thus the partition-function limit for the triangular array follows from
the classical fixed-field limit for \(V_c\). The same reduction applies to
zeros. Write
\(\lVert p\rVert^2_{Q,N}=\int_0^\infty |p(x)|^2e^{-NQ(x)}\,dx\).
If \(p_N^{(N)}\) is the monic degree-\(N\) extremal polynomial for
\(Q_N\), and \(p_N^{(c)}\) is the corresponding extremal polynomial for
\(V_c\), then

\[
\lVert p_N^{(N)}\rVert^2_{V_c,N}
\le e^{2N\delta_N}
\lVert p_N^{(c)}\rVert^2_{V_c,N}. \tag{2.5}
\]

Consequently \(p_N^{(N)}\) is asymptotically extremal for the fixed
admissible field \(V_c\), and the standard weighted zero-distribution
theorem gives the same equilibrium limit. Equations (2.4)--(2.5) isolate
all dependence on the varying sequence \(Q_N\).

For precision, the standard varying-weight result used here is the following
Gonchar--Rakhmanov/Mhaskar--Saff form. If \(Q_N\to Q\) uniformly on a closed
real set, \(Q\) is continuous and admissible
\(\bigl(Q(x)-2\log(1+|x|)\to+\infty\bigr)\), and the reference measure has
positive density almost everywhere, then the normalized zeros of the monic
degree-\(N\) \(L^2(e^{-NQ_N}dx)\)-extremal polynomials converge to the
weighted equilibrium measure for \(Q\). The corresponding log-gas partition
functions obey the energy Laplace principle (2.3). On an unbounded set this
is reduced to the compact theorem by the classical restricted-range
inequality.

All hypotheses are explicit here. Equation (2.1) gives uniform convergence,
and, because \(c_N\) is eventually bounded,

\[
Q_N(x)\ge x-C\qquad(x\ge C+1)
\]

with one constant \(C\). Thus admissibility, exponential tightness, and the
restricted-range reduction are uniform in \(N\). Lebesgue measure has
positive density everywhere. This proves both the zero-counting statement
and (2.3). This is the only place where general weighted-potential theory is
used; all remaining formulas are obtained explicitly below.

For \(c\le0\), \(V_c(x)=x-c\) on \([0,\infty)\). Adding the constant \(-c\)
does not alter the minimizer, so it is the Laguerre/Marchenko--Pastur
equilibrium measure. Its first moment is one and its logarithmic energy gives
\(\mathcal F(0)=3/2\): explicitly, the MP law has
\(\int x\,d\mu_0=1\), \(\int\log x\,d\mu_0=-1\), and evaluating the
Euler--Lagrange constant at the hard edge gives \(\ell=-2\), so
\(\mathcal F(0)=(1-\ell)/2=3/2\). Hence
\(\mathcal F(c)=3/2-c\).

---

## 3. Solution of the ramp equilibrium problem for \(c>0\)

### 3.1 Resolvent and endpoint

Suppose the support is \([0,b]\), with \(b>c\). Let

\[
M_c(z)=\int_0^b\frac{d\mu_c(x)}{z-x},
\qquad
R(z)=\sqrt{\frac{z-b}{z}},\qquad R(z)\to1\quad(z\to\infty).
\]

The differentiated Euler--Lagrange condition is

\[
M_{c,+}(x)+M_{c,-}(x)=V_c'(x)
=\mathbf1_{(c,b)}(x). \tag{3.1}
\]

The scalar Riemann--Hilbert solution is

\[
M_c(z)=\frac{R(z)}{2\pi}
\int_c^b\frac{1}{z-s}\sqrt{\frac{s}{b-s}}\,ds. \tag{3.2}
\]

The condition \(M_c(z)=z^{-1}+O(z^{-2})\) is precisely

\[
\int_c^b\sqrt{\frac{s}{b-s}}\,ds=2\pi. \tag{3.3}
\]

Put \(c=b\cos^2\phi\), \(b-c=b\sin^2\phi\). Evaluating (3.3) gives

\[
b\bigl(\phi+\sin\phi\cos\phi\bigr)=2\pi,
\]

which is (1.1)--(1.2). The map

\[
c(\phi)=\frac{2\pi\cos^2\phi}{D(\phi)}
\]

is a decreasing bijection from \((0,\pi/2)\) onto \((0,\infty)\), with
\(c(\phi)\to\infty\) as \(\phi\downarrow0\) and \(c(\phi)\to0\) as
\(\phi\uparrow\pi/2\), since

\[
c'(\phi)
=-\frac{4\pi\cos\phi(\cos\phi+\phi\sin\phi)}{D(\phi)^2}<0. \tag{3.4}
\]

Thus the endpoint is unique.

The integral in (3.2) is elementary. With consistent branches one may also
write

\[
\boxed{
M_c(z)=\frac1\pi\left[
\arctan\left(\tan\phi\sqrt{\frac{z}{z-b}}\right)
-\phi\sqrt{\frac{z-b}{z}}
\right].} \tag{3.5}
\]

### 3.2 Density and Frostman verification

Taking the jump of (3.2) gives

\[
\rho_c(x)=\frac1{2\pi^2}\sqrt{\frac{b-x}{x}}
\operatorname{PV}\!\int_c^b
\frac1{s-x}\sqrt{\frac{s}{b-s}}\,ds. \tag{3.6}
\]

If

\[
a=\sqrt{\frac{x}{b-x}},\qquad u_c=\sqrt{\frac{c}{b-c}}=\cot\phi,
\]

then direct integration yields

\[
\operatorname{PV}\!\int_c^b
\frac1{s-x}\sqrt{\frac{s}{b-s}}\,ds
=2\phi+a\log\left|\frac{u_c+a}{u_c-a}\right|. \tag{3.7}
\]

The right side is strictly positive both for \(a<u_c\) and \(a>u_c\).
Hence (1.3) defines a positive probability density on \((0,b)\).

Equation (3.1) makes the Frostman expression constant on \([0,b]\). For
\(x>b\), the derivative of

\[
V_c(x)-2\int\log|x-y|\,d\mu_c(y)
\]

is \(1-2M_c(x)>0\): the Stieltjes transform decreases from
\(M_c(b+)=1/2\). Thus the required Frostman inequality holds off the support.
This proves that (1.3) is the unique equilibrium measure, rather than only a
formal solution of the singular-integral equation.

The three distinguished local behaviors are

\[
\rho_c(x)\sim\frac{\phi\sqrt b}{\pi^2\sqrt x}
\quad(x\downarrow0), \tag{3.8}
\]

\[
\rho_c(x)=\frac1{2\pi^2}
\log\frac{4c(b-c)}{b|x-c|}+O(1)
\quad(x\to c), \tag{3.9}
\]

and

\[
\rho_c(x)\sim
\frac{\phi+\cot\phi}{\pi^2\sqrt b}\sqrt{b-x}
\quad(x\uparrow b). \tag{3.10}
\]

Thus the hard edge survives, the ramp kink produces an integrable logarithmic
bulk singularity, and the right endpoint is soft.

---

## 4. Tail mass and exact free energy

Under \(x=b\sin^2\theta\), the kink corresponds to
\(\theta=\pi/2-\phi\). Integrating (1.4) over \([c,b]\) gives

\[
p(c)=\frac{b}{\pi^2}
\int_0^{\tan\phi}
\left[
\frac{2\phi t^2}{(1+t^2)^2}
+\frac{t}{(1+t^2)^2}
\log\frac{\tan\phi+t}{\tan\phi-t}
\right]dt. \tag{4.1}
\]

The two integrals are

\[
\phi(\phi-\sin\phi\cos\phi),
\qquad
\phi\sin\phi\cos\phi,
\]

respectively. Hence (1.5) follows.

Since \(\mu_c\) has no atom at \(c\), the envelope theorem gives

\[
\mathcal F'(c)
=\int\partial_c(x-c)_+\,d\mu_c(x)
=-\mu_c((c,\infty))=-p(c). \tag{4.2}
\]

Using \(c=2\pi\cos^2\phi/D(\phi)\), one checks

\[
\frac{d}{d\phi}\left[
\log D(\phi)
-\frac{2\phi\cos^2\phi
(2\phi+\sin\phi\cos\phi)}{D(\phi)^2}
\right]
=-p(c(\phi))c'(\phi). \tag{4.3}
\]

At \(\phi=\pi/2\), \(c=0\), \(D=\pi/2\), and
\(\mathcal F(0)=3/2\). Integrating (4.3) proves (1.6).

---

## 5. The MP-to-arcsine interpolation and its phase transition

### 5.1 Onset at \(c=0\)

Write \(\phi=\pi/2-\varepsilon\). Then

\[
c=4\varepsilon^2+O(\varepsilon^4),
\qquad
b=4+\frac{2}{3\pi}c^{3/2}+O(c^2), \tag{5.1}
\]

\[
p(c)=1-\frac{2}{\pi}\sqrt c+O(c), \tag{5.2}
\]

and

\[
\boxed{
\mathcal F(c)=\frac32-c+\frac{4}{3\pi}c^{3/2}+O(c^2)
\qquad(c\downarrow0).} \tag{5.3}
\]

For \(c<0\), \(\mathcal F(c)=3/2-c\). Therefore \(\mathcal F\) is
\(C^1\) but not \(C^2\) at \(c=0\); more precisely,

\[
\mathcal F''(c)\sim\frac1{\pi\sqrt c}\qquad(c\downarrow0).
\]

This is a genuine continuous hard-edge onset transition with singular
exponent \(3/2\). Calling it a third-order transition would be inaccurate
under the usual derivative-based convention.

### 5.2 Arcsine limit

As \(c\to\infty\),

\[
\phi=\frac\pi c-\frac{2\pi^3}{3c^3}+O(c^{-5}),
\qquad
b=c+\frac{\pi^2}{c}+O(c^{-3}), \tag{5.4}
\]

\[
p(c)=\frac1c-\frac{\pi^2}{3c^3}+O(c^{-5}), \tag{5.5}
\]

and

\[
\mathcal F(c)=\log\frac4c-\frac{\pi^2}{6c^2}+O(c^{-4}). \tag{5.6}
\]

Let \(\nu_c\) be the pushforward of \(\mu_c\) by \(x\mapsto x/c\). Then

\[
\boxed{
\nu_c\Longrightarrow
\frac{\mathbf1_{(0,1)}(u)}{\pi\sqrt{u(1-u)}}\,du
\qquad(c\to\infty).} \tag{5.7}
\]

Indeed, for fixed \(0<u<1\), (1.3) gives

\[
c\rho_c(cu)\longrightarrow\frac1{\pi\sqrt{u(1-u)}},
\]

while \(b/c\to1\) and the tail mass above the kink is \(p(c)\to0\).
Thus this single explicit equilibrium family starts at the parameter-one
Marchenko--Pastur law and ends, after its natural macroscopic rescaling, at
the arcsine equilibrium law of a compact interval.

---

## 6. Arithmetic strengthening from [001]

Let

\[
K=\overline{\mathbf Q}
\bigl(e^\beta:\beta\in\overline{\mathbf Q}\bigr).
\]

The arithmetic input [001, Corollary 8.4] says that all
\(\Ein_q(\alpha)\), jointly for \(q\ge1\) and nonzero algebraic \(\alpha\),
are algebraically independent over \(K\).

### Theorem 2 (an algebraically independent phase-transition sequence)

For every sequence \(\alpha_N\in\overline{\mathbf Q}_{>0}\), the countable
family

\[
\{H_N(\alpha_N):N\ge1\}
\]

is algebraically independent over \(K\), in the finite-subset sense.

#### Proof

For fixed \(N\), the coordinate

\[
\mu_{\alpha_N,2N-2}=(2N-2)!\Ein_{2N-1}(\alpha_N)
\]

occurs only in the bottom-right entry of the \(N\)-by-\(N\) Hankel matrix.
Expansion in this coordinate gives

\[
H_N(\alpha_N)
=H_{N-1}(\alpha_N)\mu_{\alpha_N,2N-2}+B_N, \tag{6.1}
\]

where \(B_N\) does not involve \(\mu_{\alpha_N,2N-2}\), and
\(H_{N-1}(\alpha_N)\ne0\) by strict positivity. No earlier determinant
\(H_j(\alpha_j)\), \(j<N\), uses the coordinate
\((\alpha_N,2N-1)\). Since all underlying polyexponential coordinates are
jointly algebraically independent, (6.1) proves the assertion inductively.
For completeness, there is no hidden cancellation in this pivot argument.
If a nonzero relation \(R(H_1,\ldots,H_N)=0\) had degree \(d\) in its last
variable, induction would make its leading coefficient
\(R_d(H_1,\ldots,H_{N-1})\) nonzero. After substituting (6.1) and viewing
the result as a polynomial in the new coordinate
\(\mu_{\alpha_N,2N-2}\), its leading coefficient would be

\[
R_d(H_1,\ldots,H_{N-1})H_{N-1}(\alpha_N)^d\ne0.
\]

This contradicts the algebraic independence of that coordinate from all
coordinates occurring earlier. The reasoning also covers repeated values
among the \(\alpha_N\), because the order \(2N-1\) coordinate cannot occur
in a determinant of smaller size.

For every real \(c\), one can choose positive rational \(\alpha_N\) with
\(\log\alpha_N/N\to c\). Combining Theorems 1 and 2 therefore produces,
for every \(c\in\mathbf R\), an explicit sequence of positive, jointly
algebraically independent transcendental Hankel determinants satisfying

\[
\log H_N(\alpha_N)
=N^2\log N-N^2\mathcal F(c)+o(N^2),
\]

with the nonanalytic \(3/2\)-onset at \(c=0\) and the MP-to-arcsine
spectral interpolation. This is the cleanest direct bridge between the
arithmetic theorem of [001] and a macroscopic random-matrix phase diagram.

---

## 7. Literature boundary and honest level assessment

The general mechanisms used here are classical:

* logarithmic equilibrium and varying-weight zero asymptotics go back to
  Gonchar--Rakhmanov and weighted-potential theory;
* the Laguerre endpoint \(c\le0\) is the parameter-one
  Marchenko--Pastur law;
* the \(c\to\infty\) endpoint is the classical equilibrium/arcsine law on
  an interval;
* large-\(N\) asymptotics for analytic one-cut varying weights were
  developed by Deift--Kriecherbauer--McLaughlin--Venakides--Zhou.

Targeted searches did not locate a paper treating the exact weight
\(1-e^{-\alpha e^{-y}}\), the exact ramp field \((x-c)_+\) with the formulas
(1.1)--(1.7), or its coupling to an algebraically independent
polyexponential Hankel tower. This is evidence of specificity, not a
complete priority proof; MathSciNet/Zentralblatt and specialist review are
still required before asserting historical novelty.

As a standalone result, Theorem 1 is a strong explicit
potential-theory/random-matrix theorem, but not credibly Annals-level by
itself. Its value rises materially when packaged with the STP/Jacobi and
arithmetic-generic results. The genuinely higher-tier continuation is the
local analysis of the logarithmic kink (3.9): the mean spacing there is of
order \((N\log N)^{-1}\) in the scaled \(x\)-coordinate, while the original
Gumbel smoothing of the weight occurs on the larger \(N^{-1}\) scale.
A rigorous local kernel, recurrence-coefficient asymptotics, and a uniform
critical expansion across \(c=0\) would constitute a substantially deeper
Riemann--Hilbert problem.

### Primary background located

* A. A. Gonchar and E. A. Rakhmanov, [*Equilibrium measure and the
  distribution of zeros of extremal polynomials*](https://ui.adsabs.harvard.edu/abs/1986SbMat..53..119G),
  Math. USSR-Sb. 53 (1986), 119--130.
* P. Deift, T. Kriecherbauer, K. T.-R. McLaughlin, S. Venakides and
  X. Zhou, [*Uniform asymptotics for polynomials orthogonal with respect to
  varying exponential weights and applications to universality questions
  in random matrix theory*](https://doi.org/10.1002/(SICI)1097-0312(199911)52:11%3C1335::AID-CPA1%3E3.0.CO;2-1),
  Comm. Pure Appl. Math. 52 (1999), 1335--1425.
* A. B. J. Kuijlaars and P. M. J. Tibboel, *The asymptotic behaviour of
  recurrence coefficients for orthogonal polynomials with varying
  exponential weights*, [arXiv:0708.3956](https://arxiv.org/abs/0708.3956).

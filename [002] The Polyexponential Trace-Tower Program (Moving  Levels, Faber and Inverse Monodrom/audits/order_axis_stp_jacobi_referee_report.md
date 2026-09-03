# Referee audit: order-axis STP/Jacobi note

## Bottom line

Conditional on [001, Corollary 8.4], the central theorem

\[
(\alpha,q)\longmapsto \Gamma(q)\Ein_q(\alpha)
\]

being STP\(_\infty\) on \((0,\infty)^2\) is correct.  The two-stage
continuous Cauchy--Binet proof has the right orientation and a valid
positive-measure strictness cell.  The arithmetic-generic matrix,
Grassmannian, moment/Hankel, finite-Jacobi, quadrature, and generic Galois
consequences are also correct after a few qualifications below.

This is a strong specialist-paper package, but not on present evidence an
Annals-level theorem: the arithmetic depth is imported from [001], while the
new transfer uses classical total-positivity, moment, inverse-spectral, and
potential-theoretic machinery.

## Confirmed

1. **Master STP theorem.**  In
   \[
   1-e^{-\alpha e^{-y}}
   =\int_0^\infty {\bf1}_{u<\alpha}e^{-y}e^{-u e^{-y}}\,du,
   \]
   the Volterra determinant is nonnegative, and on
   \(0<u_1<\alpha_1<u_2<\cdots<u_r<\alpha_r\) it equals one.  Since
   \(-e^{-y}\) increases with \(y\), the second determinant is an
   \(e^{uv}\) determinant with both coordinates increasing and is strictly
   positive.  Composition with \(y^{q-1}=e^{(q-1)\log y}\) proves strict
   total positivity for every real \(q>0\).

2. **Arithmetic-generic matrices.**  With distinct algebraic sample points
   and distinct positive integral orders, the entries are independent
   indeterminates over \(K\), up to nonzero factorial scalars.  Therefore:
   every minor is positive and transcendental; maximal minors have exactly
   the Pluecker ideal and affine-cone transcendence degree
   \(r(s-r)+1\); the projective row span is a generic positive
   Grassmannian point; and leading principal minors are jointly algebraically
   independent by the private-variable induction.

3. **Oscillation/Galois.**  A square strict-TP sample has positive simple
   eigenvalues with the Gantmacher--Krein sign-variation pattern.  Its
   characteristic coefficients are algebraically independent: specializing
   a universal matrix to a diagonal matrix reduces any putative relation to
   one among elementary symmetric functions.  Hence its eigenvalues are
   jointly algebraically independent, and the characteristic polynomial has
   generic group \(S_n\) over its coefficient field.

4. **Moment/Hankel tower.**  The Stieltjes representation, Carleman
   determinacy, strict Hankel total positivity, normalized-moment/cumulant
   birational changes, and joint independence of the principal Hankel
   determinants are correct.  The private variable is
   \(\mu_{2d-2}\), with coefficient \(H_{d-1}\ne0\).

5. **Finite Jacobi inverse spectra.**  The finite Favard map is birational.
   A consecutive monic pair \((p_N,p_{N-1})\) recovers all
   \(a_0,\ldots,a_{N-1},b_1,\ldots,b_{N-1}\) by the Euclidean algorithm.
   Thus the combined consecutive spectra have transcendence degree and
   number of elements \(2N-1\), hence are jointly algebraically independent.
   The two coefficient tuples are independent generic polynomial tuples, so
   their splitting group is \(S_N\times S_{N-1}\).  Gaussian nodes and
   masses are a finite extension of, and recover, the first \(2N\) moments;
   their \(2N\) coordinates are therefore jointly algebraically independent.

6. **Exact law and endpoint limits.**  The survival function, MGF, poles at
   every positive integer, non-D-finiteness/non-P-recursiveness, likelihood-
   ratio monotonicity, and the Laguerre and shifted-Legendre fixed-degree
   limits check out.  The two fixed-\(d\) Hankel endpoint formulae are also
   correct.

7. **Determinant free energy.**  The comparison
   \((1-e^{-\alpha})e^{-y}\le w_\alpha(y)\le\alpha e^{-y}\) gives the
   determinant bounds in Loewner order, and Barnes--Stirling asymptotics give
   \(H_{\alpha,d}^{1/d^2}/d\to e^{-3/2}\).

## Correct but needs a lemma/citation before publication

1. **Chebyshev wording.**  Replace “at most \(r-1\) zeros” by “at most
   \(r-1\) distinct zeros”, unless an extended-Chebyshev/Wronskian argument
   counting multiplicities is added.  Define the function class and transform
   if retaining the blanket “variation diminishing” sentence.

2. **Full flag statement.**  The claim is right at the function-field level,
   but state explicitly that raw Pluecker coordinates form the multicone;
   after separate projectivization the transcendence degree is
   \(n(n-1)/2\).  Cite the defining flag incidence ideal rather than leave
   “usual” implicit.

3. **Infinite Jacobi operator.**  Spell out the standard chain: Carleman
   determinacy implies essential self-adjointness and polynomial density;
   the resulting multiplication operator has spectral measure
   \(w_\alpha(y)dy/\Ein(\alpha)\), hence simple purely a.c. spectrum
   \([0,\infty)\).

4. **Spectral flow.**  Markov's theorem gives the stated strict direction
   because \(\partial_\alpha\log w_\alpha(y)\) is strictly increasing in
   \(y\), but cite a version allowing the fixed unbounded support and verify
   differentiation/dominating hypotheses.

5. **Fixed-\(\alpha\) Marchenko--Pastur law.**  It is correct: after
   \(y=Nx\), the bounded multiplier of \(e^{-Nx}\) contributes
   \(o(1)\) uniformly to the external field.  “Norm comparison” alone is not
   a proof; cite and check an unbounded-support varying-weight zero theorem.

6. **Double scaling.**  The proposed limit field
   \(V_c(x)=(x-c)_+\), endpoint equation, Tricomi density, kink logarithm,
   \(b_c-c\sim\pi^2/c\), and large-\(c\) arcsine rescaling are internally
   consistent (the formula returns MP with \(b_0=4\)).  However, this entire
   subsection should be labeled a theorem only after supplying:
   (i) a precise varying-weight zero theorem on \([0,\infty)\);
   (ii) tightness/admissibility verification; (iii) a short derivation that
   convexity gives one-cut support \([0,b_c]\); and (iv) the Tricomi inversion
   and normalization computation.  Until then call it **provisional**, not a
   closed result.

## Corrections / deletions

* Fix the recurrence indexing: use
  \(p_{n+1}=(y-a_n)p_n-b_n p_{n-1}\) for \(n\ge1\), \(b_n>0\), and list
  \(b_1,b_2,\ldots\); or shift every \(b\)-index consistently.
* Do not say a web search establishes priority.  Use “no exact precedent was
  found in the searches below”; a MathSciNet/Zentralblatt/reference-chain
  audit is still needed.
* No central theorem needs deletion.  The only material demotion is the
  double-scaling subsection pending a fully cited potential-theory proof.

## Literature check

Targeted searches for the exact kernel under `Ein`, “entire exponential
integral”, and “polyexponential” nomenclature found no prior statement of its
STP\(_\infty\) property, its Jacobi weight, or the arithmetic-generic
Grassmannian consequences.  This is evidence, not a priority proof.

Add the basic polyexponential source omitted from the note:

* K. N. Boyadzhiev, *Polyexponentials*, arXiv:0710.1332
  (https://arxiv.org/abs/0710.1332).  It records basic properties and Mellin
  representations but its abstract/source search exposes no total-positivity
  result.

Verified close primary precedents:

* D. St. P. Richards, *Totally positive kernels, Polya frequency functions,
  and generalized hypergeometric series*, LAA 137/138 (1990), 467--478,
  DOI 10.1016/0024-3795(90)90139-4.
* V. Buchstaber and A. Glutsyuk, *Total positivity, Grassmannian and modified
  Bessel functions*, arXiv:1708.02154
  (https://arxiv.org/abs/1708.02154).  Its exact result concerns matrices of
  integer-index modified-Bessel values.
* D. S. P. Salazar, *Strict Total Positivity from Spectral Darboux and Toeplitz
  Smoothing Mechanisms*, arXiv:2607.02778
  (https://arxiv.org/abs/2607.02778).  Its stated application is the real-order
  modified-Bessel kernel, not Ein/polyexponentials.
* A. Postnikov, *Total positivity, Grassmannians, and networks*,
  arXiv:math/0609764 (https://arxiv.org/abs/math/0609764).

## Referee-level valuation

* STP master theorem: **confirmed, publishable centerpiece**.
* Arithmetic generic matrices/Grassmannian/Galois: **confirmed conditional on
  [001]**, strong and visually distinctive, but mostly formal transfer.
* Jacobi/quadrature tower: **confirmed with standard lemmas written out**.
* Fixed-parameter large degree: **correct, citation needed**.
* Double scaling: **promising new analytic theorem, currently provisional**.
* Overall: credible strong specialist paper or a major section of the main
  manuscript; not responsibly classifiable as Annals-level by itself.

# Referee audit: generic Taylor, incomplete Gamma, and Mahler

**Date:** 2026-09-01  
**Scope:** `ANNALS_APERTURES_MONODROMY_DA_GALOIS.md`, Theorem 7 and (2.2), and
`Gamma_Tail_DT_Zero_Density_Motive_Audit.md`, Theorem 3.  The arithmetic
independence theorem quoted from [001] is treated as an input and is not
re-proved here.

## Verdicts

| Claim | Verdict | Reason |
|---|---|---|
| Generic Taylor lemma, hence Theorem 7 | **PASS after minor proof revision** | The finite-support specialization argument is valid, but the constant derivation and the evaluation homomorphism should be made explicit. |
| Incomplete-Gamma independence (2.2) | **PASS after minor proof revision** | Differential transcendence degree is preserved under the stated differential-algebraic base extension; the two tower-law equalities should be displayed. |
| `Gamma(s,1)` is DT over `C(s)` | **PASS** | Mahler's 1971 theorem has exactly the strength used, and the tail lower bound forces infinite coefficient-field transcendence degree. Add one normalization sentence. |

No fatal base-field, coefficient-support, constant-derivation, or Mahler-hypothesis
error was found.

## 1. Generic Taylor lemma

Equip

\[
A=k(a_{i,n}:i\in I,n\geq0)
\]

with the **constant derivation** `D(a_{i,n})=0`, and equip `A(u)` with
`D(u)=1`.  This convention is essential and should be stated.

Suppose that a nonzero relation exists.  After clearing every denominator,
write it as

\[
Q(u,F_i,F_i',\ldots,F_i^{(r)}:i\in I_0)=0,
\qquad
Q\in k[a_{i,n}:(i,n)\in S][u,\mathbf Y]\setminus\{0\},
\]

where `I_0` and `S` are finite.  Choose `N` so that all blocks
`(i,N),...,(i,N+r)`, `i in I_0`, avoid `S`.  Because `k` is infinite,
specialize the variables in `S`, choose \(u_0\in k^\times\), and choose target jets
`b_{i,j}` so that the specialized value of `Q(u_0,b)` is nonzero.

For each `i`, the matrix

\[
W_i=\left((D^j u^{N+\ell})(u_0)\right)_{0\leq j,\ell\leq r}
\]

is invertible.  Indeed, after row and column scaling it is the evaluation
matrix of the falling factorial polynomials
`(N+ell)_{j}`, whose determinant is a nonzero Vandermonde determinant; the
remaining power of `u_0` is nonzero.  Hence the fresh block can be assigned
so that the specialized polynomial `F_i` has precisely the target jet,
after accounting for the coefficients in `S`.  Assign zero to all remaining
coefficient variables.  This defines an evaluation homomorphism from the
universal polynomial ring.  The formal identity becomes an identity between
polynomials in `u`, and evaluation at `u_0` contradicts `Q(u_0,b) != 0`.

This version closes the only real exposition gap in the current proof.  It
also makes clear why putting *all* Taylor coefficients in the base field does
not cause a relation: a differential polynomial can use only finitely many of
them.

The extension from `A` to an algebraic constant-field extension is also
valid.  Any proposed relation uses finitely many algebraic coefficients, so
it lies in a finite algebraic extension; multiplying its constant-field
conjugates (equivalently, taking a norm) descends a nonzero relation.

## 2. Passage to lower incomplete Gamma

For a finite family `alpha_i`, put

\[
F=\mathcal P(u),\qquad
E=\mathcal P(\log\alpha_i,\alpha_i^u:i)(u).
\]

Choose one logarithm `lambda_i=log(alpha_i)` for each `i`.  The extension
`E/F` is differential algebraic because

\[
D\lambda_i=0,\qquad D(\alpha_i^u)=\lambda_i\alpha_i^u.
\]

Let `G=(G_{alpha_i})` and `M=E\langle G\rangle`.  Since `E/F` is
differential algebraic, so is `M/F\langle G\rangle`; therefore

\[
\operatorname{dtrdeg}_F M
=\operatorname{dtrdeg}_F F\langle G\rangle
=\#\{i\}.
\]

The tower law and `dtrdeg_F E=0` then give

\[
\operatorname{dtrdeg}_E M=\#\{i\}.
\]

Thus the `G_{alpha_i}` remain jointly differential-algebraically independent
over `E`.  Finally,

\[
G_{\alpha_i}(u)=-u^{-1}-\alpha_i^u\gamma_<(-u,\alpha_i)
\]

is an invertible affine change over `E`, so the lower incomplete-Gamma
functions have the same differential transcendence degree.  This proves
(2.2).  The branch choice only affects the separate factors; their product
is the branch-independent meromorphic germ given by the displayed series.

## 3. Mahler and the fixed-cut upper incomplete Gamma

Mahler's paper was checked directly: K. Mahler, *A remark on algebraic
differential equations*, Rend. Accad. Naz. Lincei, Ser. VIII 50 (1971),
402--412.  Its abstract and sections 3--5 state precisely the needed facts:

1. the argument is formal and works over any coefficient field of
   characteristic zero;
2. if a formal series satisfies an algebraic differential equation over
   such a field, it consequently satisfies one with rational-integer
   coefficients;
3. the field generated over `Q` by all coefficients of the series is a
   finitely generated extension of `Q` (a finite transcendence basis and one
   algebraic generator).

Mahler writes the series in exponential-generating normalization

\[
f(z)=\sum_{n\geq0} f_n z^n/n!.
\]

For `U(s)=Gamma(s,1)=sum T_n s^n`, his coefficient field is therefore

\[
\mathbf Q(n!T_n:n\geq0)=\mathbf Q(T_n:n\geq0),
\]

so the normalization does not alter the argument.  This sentence should be
added near the citation.

The contradiction is sound:

\[
\operatorname{trdeg}_K K(T_0,T_1,\ldots)=\infty
\]

implies infinite transcendence degree over `Q`, since every finite subset
algebraically independent over `K` is also algebraically independent over
`Q`.  If `U` were differential algebraic over `C(s)`, clearing rational
denominators would put it under Mahler's theorem with the characteristic-zero
constant field `C`, forcing its coefficient field over `Q` to be finitely
generated, a contradiction.

The proof is formal at the decisive step; analyticity is only used to
identify the Taylor coefficients by differentiation under the integral.

## Recommended labels in the main note

- Theorem 7: retain **Theorem**, after inserting the constant derivation and
  rigorous finite-support specialization paragraph.
- Equation (2.2): retain **proved**, after displaying the two tower-law
  equalities.
- Fixed-cut DT theorem: retain **Theorem**.  Cite Mahler's exact pages and add
  the factorial-normalization equality above.

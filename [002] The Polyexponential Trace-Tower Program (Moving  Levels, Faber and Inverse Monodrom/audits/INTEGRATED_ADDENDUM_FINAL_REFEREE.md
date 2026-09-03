# Final hostile referee audit of the integrated barrier-escape addendum

> **SUPERSEDED FREEZE SNAPSHOT.**  This report documents the discovery and
> repair of the seven-class \(m=27\) issue, but it predates the integrated
> even-row separability results and final status-legend correction.  The
> controlling publication verdict is `FINAL_FREEZE_REFEREE.md`.

## Scope and final verdict

I audited the latest
`KEIO_Moving_Level_Trace_Towers_v2_4_Barrier_Escape_Addendum.md`, its two
exact audit programs and logs, and the companion proof/referee notes cited
in its reproducibility map.  The audit covered theorem quantifiers,
Newton-polygon and polar formulas, conditional-status boundaries,
finite-field periodicity, the million-degree endpoint logic, hashes, and
the Morse-versus-group distinction.

**Verdict on the latest integrated addendum: PASS, after one material finite
certificate repair made during this audit.**  The current addendum has
SHA-256

```text
416ea5104f8d787b1411fef0b13469f28dbe5929dbb7184f6850f85e15deb399
```

The repaired all-order audit now genuinely proves the finite theorem through
degree (1001).  All U-PASS, X-PASS, C-PASS, and OPEN labels in the current
addendum have the advertised logical strength.  In particular, Hypothesis
DS is used only in Theorem 8.1, and no DS-conditional statement leaks into
the unconditional prime-degree, moving-prime, large-order, transfer, or
finite-range theorems.  No claim about irrationality or transcendence of
Euler's constant is made or implied.

The theorem package itself needs no further mathematical patch.  Before a
publication/reproducibility bundle is frozen, however, five stale companion
artifacts must be corrected or explicitly marked superseded; exact file-level
recommendations appear in the final section of this report.

## Claim ledger

| Integrated claim | Verdict | Exact qualification |
|---|---|---|
| Imported indecomposability and (A_m/S_m) reduction | **PASS** | Imported structural theorem; (q\ge1,m\ge2), with the (A_m/S_m) reduction stated only for (m\ge3). |
| Prime-degree Morse theorem | **PASS (U)** | Complete for every (q\ge1) and prime (m\ge3); degree (2) is separately structural. |
| Strict-window moving-prime criterion | **PASS (U)** | The strict inequality (p>(m+1)/2) and square-free residual derivative are essential. |
| Family (m=p+2) | **PASS (U)** | (p\ge5), every (q\ge1); the residual derivative is linear. |
| Fixed-degree, large-order Morse theorem | **PASS (U)** | Effective (Q(m)), not uniform in (m). |
| Single-spike Faber transfer | **PASS (U)** | Isolated transposition under (7.1); full (S_m) additionally requires indecomposability. |
| Logarithmic--Stirling (S_{p+2}) family | **PASS (U)** | Absolute indecomposability is supplied by the nonzero reciprocal coefficients. |
| Every (q\ge1), (2\le m\le1001) | **PASS (X), after repair** | Group (S_m), not an all-rectangle Morse theorem. |
| (q=1), (2\le m\le10^6) | **PASS (X)** | Group (S_m), not an all-degree Morse theorem. |
| DS-conditional density-one theorem | **PASS (C)** | Exactly conditional on (Delta_r\ne0) for every even (r\ge2). |
| Universal window selection / all odd composites | **OPEN** | No asymptotic all-degree selection lemma is proved. |
| Irrationality or transcendence of (gamma) | **OPEN** | Untouched and not an input. |

## 1. Prime-degree and moving-prime proofs

The coefficient identity

\[
[X^j]P'_{q,m}=m[z^{m-j-1}]A_q^{j+1}
\]

has the correct indices.  At a prime degree (m), the valuations

\[
v_m(d_0)=-q,\qquad v_m(d_j)\ge1\ (1\le j\le m-2),
\qquad v_m(d_{m-1})=1
\]

give a single Newton edge.  The residual binomial has degree (m-1),
which is prime to the residue characteristic, so all critical points are
simple.  The monomial (X^m) is uniquely dominant at every critical point;
the residual critical values are a nonzero scalar times the distinct
critical-root residues.  This proves the full Morse assertion, not merely
one transposition.

For a strict window (m=p+r), (2\le r\le p-2), the three derivative
edges, root counts, and valuations in (4.2) are exact.  The polar identities
(4.4)--(4.5) have the correct factors (X^2/r) and
(X(2R+XR')/r).  Frobenius removes the only potentially dangerous
integration denominator at (X^p).  Square-freeness of
(P'_{q,r}\bmod p) prevents all unit-face critical-value cancellation,
while the other two clusters have strictly different critical-value
valuations.  The isolated length-one point therefore gives a transposition.
The imported indecomposability theorem gives primitivity, and primitive plus
a transposition gives (S_m).

The addendum correctly treats residual square-freeness as a sufficient
first-polar criterion.  It never promotes failure of that test to an actual
critical-value collision.

## 2. Material repair of the (m=27) certificate

The earlier certificate contained the false implication

\[
q\equiv1075\pmod{1584}\quad\Longrightarrow\quad q\equiv11\pmod{28}.
\]

In fact (1584\equiv16\pmod{28}), so the progression occupies seven
classes:

\[
\{3,7,11,15,19,23,27\}\pmod{28}.
\]

The latest addendum and `trace_allq_modp_audit.py` now derive those classes
using the gcd of the two periods and certify every class separately modulo
(29).  I independently recomputed the displayed pairs
((T,D_q(T))), where
(D_q(T)=\operatorname{Disc}_X(P_{q,27}(X)-T)):

| (q\bmod28) | square value | nonsquare value |
|---:|---:|---:|
| 3 | ((3,7)) | ((0,17)) |
| 7 | ((0,16)) | ((4,11)) |
| 11 | ((0,22)) | ((5,27)) |
| 15 | ((2,16)) | ((1,12)) |
| 19 | ((1,16)) | ((0,18)) |
| 23 | ((0,22)) | ((1,15)) |
| 27 | ((0,22)) | ((1,3)) |

All fourteen values are nonzero.  Opposite quadratic characters rule out
"constant times a square" for each discriminant polynomial.  This is the
right certificate: the (q\equiv19\pmod{28}) discriminant is not
square-free modulo (29) (its gcd with its derivative has degree (2)),
but it is still not a constant times a square.  The latest addendum no
longer asserts an incorrect equivalence between square-freeness and the
two-character test.

The corrected exact run returns the seven classes and all witness pairs,
then `AUDIT=PASS`.  Its archived hashes are

```text
trace_allq_modp_audit.py
36ba3fd004df1e5a56a7bb6c61ed49cf7542d6f7c934ba458f88c1ebe105c31c

trace_allq_modp_audit_1001.txt
1d4867aa086b4315d45d70c52ef27090ad4d1c256cd956cb6b18d72a8be374be
```

The (m=989) patch is unchanged and valid: the bad classes modulo (918)
are odd, the bad classes modulo (928) are even, and the simultaneous CRT
locus is empty.  With the 492 uniform witnesses and six prime-degree
fallbacks, the count is (492+6+2=500), exactly the number of odd degrees
from (3) through (1001).

## 3. Million-degree (q=1) audit

The hardened `window_prime_selection_audit.py` includes prime endpoints,
obtains its prime ceiling dynamically, and asserts the strict-window
inequality for both the nearest and fallback primes.  Its conclusion is

```text
BOUND=1000000
LARGEST_NEAREST_RESIDUAL=114
NEAREST_PRIME_FAILURES=[(215, 211, 4), (69649, 69623, 26)]
TWO_PRIME_FAILURES=[]
SELECTION_AUDIT=PASS
```

The two artifact hashes printed in the current addendum are exact:

```text
window_prime_selection_audit.py
e2eb3b8a14f758d84c0d80a4ed3c0ed11a3cf7eb38e3935960be3122d8fdcbf0

window_prime_selection_audit_1000000.txt
51d3a027e9f0ce42f4918b39058288cdfdf808e25ded994ed009a701bc7c44f5
```

I independently reran the hardened million-degree program.  It completed in
92.031 seconds and its stdout was byte-for-byte identical to the archived
log.  I also independently reran the repaired all-order program through
degree 1001; it completed in 151.850 seconds and likewise matched its
archived log byte for byte.

The computation supplies an isolated transposition in each audited odd
degree.  Even degrees use the imported structural theorem, and degrees
(3,5) use the prime theorem.  The addendum consistently states only full
symmetric monodromy in this rectangle, not the Morse property.

## 4. Large-order theorem

The composition-product lower bound

\[
n_1\cdots n_k\ge m-k+1
\]

and the scaling in Section 6 leave exactly the endpoint binomial

\[
S_m(y)=y^m+\frac{(-1)^{m-1}}{(m-1)!}y.
\]

Every intermediate coefficient is bounded by

\[
O_m\!\left(\left(
\frac{m^{(r-1)/(m-1)}}r\right)^q\right),
\]

whose base is strictly below one.  The roots of (S_m') and their images
are two distinct regular polygons.  Since the Morse locus is open and all
error constants are explicit, the eventual-Morse conclusion and the
effectivity of (Q(m)) are justified.  The theorem is row-wise in (m),
not a uniform all-((q,m)) statement; the current abstract and ledger make
that distinction.

## 5. Single-spike Faber transfer

Under (7.1), the four exact derivative vertices are

\[
(0,-s),(1,-h),(r,-h),(m-1,0).
\]

The endpoint at (j=1) uses the unit (a_{r-1}), at most one deep
coefficient (a_{p-1}) can occur, and all no-spike tail terms lie strictly
above depth (-h).  This proves the claimed Newton polygon.  The reduction
in (7.2) correctly uses only the integral truncation below (p-1).  The
multinomial Frobenius divisibility is by the integer (p), so the
(X^p)-coefficient remains integral even at a ramified place.

The three critical-value valuations

\[
h-2s,\qquad -h,\qquad -\frac{mh}{p-1}
\]

are strictly separated because (h>s).  Thus the local theorem gives an
isolated transposition.  The current theorem statement and ledger correctly
add indecomposability as a separate hypothesis for the global (S_m)
conclusion.  The parameters in the polylogarithmic and hypergeometric-type
examples are now explicitly quantified as positive integers.

For (f=-\log(1-z)), the Stirling coefficient formula is correctly
normalized and monic.  The identity

\[
\frac z{-\log(1-z)}=\int_0^1(1-z)^t\,dt
\]

shows that every positive-degree reciprocal coefficient is nonzero.  With
the exact index shift
(d_b=[z^b](1/f)=[z^{b+1}](z/f)), the imported Faber obstruction proves
absolute indecomposability.  Hence the (S_{p+2}) logarithmic--Stirling
family is genuinely unconditional.

## 6. Shifted discriminants and conditional density one

For (F_r=(r!)^2P'_{1,r}), termwise composition divisibility gives
(F_r\in\mathbf Z[X]), and for (p>r) the scaling and leading
coefficient are units.  Therefore

\[
P'_{1,r}\bmod p\text{ is not square-free}
\iff p\mid\Delta_r
\]

is exact.  The coefficient height and Mahler bounds give
(log|\Delta_r|=O(r^2\log r)) only when (Delta_r\ne0), exactly as
the addendum states.

Under DS, splitting at (H=X^{5/16}) gives (H^3\log H) short-offset
exceptions and (X^{5/4+\varepsilon}/H) long-gap exceptions.  Both are
(O_\varepsilon(X^{15/16+\varepsilon})).  The theorem is visibly C-PASS,
and the open selection problem is separately quantified for every
(q\ge1) and sufficiently large odd composite (m).  No conditional
density statement is used to justify either exact finite rectangle.

## 7. Exact required package patches

The integrated addendum is correct, but the following stale companion
artifacts presently contradict it and must be patched or labelled
**superseded by this final referee audit** before packaging.

1. **`ODD_TRACE_MODP_ROUTE.md`, Section 5.**  Replace the sentence claiming
   that (q\equiv1075\pmod{1584}) implies
   (q\equiv11\pmod{28}), and replace its one-class modulo-(29)
   certificate by the seven residue classes and witness table in Section 2
   above.  Replace the obsolete audit-script hash
   `86ecea91...` by the current script/log hashes
   `36ba3fd...` and `1d4867a...`.
2. **`odd_trace_modp_route.py`.**  Its docstring and `certificate_m27()`
   still encode the false one-class implication.  Either replace that
   routine by the seven-class gcd-period and opposite-character check now in
   `trace_allq_modp_audit.py`, or remove it from the reproducibility bundle
   in favor of the corrected audit script.
3. **`NEW_BARRIER_ESCAPE_REFEREE.md`.**  Its (m=27) discussion repeats
   the false implication and its source hash is obsolete.  Add a prominent
   supersession notice pointing to this report, or revise the discussion and
   hashes to the seven-class certificate.
4. **`WINDOW_PRIME_SELECTION_REFEREE.md`.**  The mathematics remains valid,
   but its final source hash `863c1f28...` predates the dynamic-prime and
   strict-window assertion hardening.  Replace it by `e2eb3b8...`, and mark
   the old `bound + 10_000` and missing-assertion caveats as resolved.
5. **LaTeX/PDF deliverables.**  At the time of this report,
   `output/source/KEIO_Trace_Barrier_Escape_Addendum_v2_4.tex` lines
   434--438 still contain the obsolete one-class (q\equiv11\pmod{28})
   certificate and blanket square-free wording.  Regenerate the TeX,
   standalone PDF, and consolidated PDF from the corrected Markdown before
   delivery, then render-check the corrected (m=27) table in the PDF.

For publication-grade computational documentation, one further
non-logical improvement remains advisable: emit the selected
((m,p,r)) witness for every finite row and provide a short independent
verifier that consumes the witness file.  The present deterministic exact
runs already establish the stated X-PASS theorems, but a witness/verifier
split would reduce trust in the search implementation.

Subject to the five companion-artifact cleanups above, the integrated
addendum is internally consistent and survives hostile review.  It is a
substantial theorem package, but it correctly stops short of claiming the
unproved universal all-odd selection theorem or any result on the arithmetic
nature of (gamma).

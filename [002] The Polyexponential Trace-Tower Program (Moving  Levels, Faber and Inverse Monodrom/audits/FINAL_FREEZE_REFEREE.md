# Publication-freeze hostile audit

## Controlling verdict

This report audits the latest
`KEIO_Moving_Level_Trace_Towers_v2_4_Barrier_Escape_Addendum.md` after the
even-row derivative results and the repaired degree-27 certificate were
integrated.  It also checks `ODD_TRACE_MODP_ROUTE.md`,
`odd_trace_modp_route.py`, the exact audit sources and logs, and the two
specialist referee reports behind the new Section 8.

**Verdict on the latest Markdown addendum: PASS.**  One status-legend
inconsistency was found and repaired by the coordinating author during this
audit: OPEN hypotheses are now stated to be used only in explicitly
conditional results, never in unconditional claims.  No further mathematical
patch is required in the Markdown.

The frozen Markdown SHA-256 is

```text
23fa034a7971d289ef5677c45419d91bcd2dc349873bd8495ea13d412fa8db75
```

Two packaging actions remain mandatory: regenerate the TeX/PDF files from
this Markdown, and treat the older `INTEGRATED_ADDENDUM_FINAL_REFEREE.md` as
superseded by the present report.  Those are artifact-version issues, not
defects in the current Markdown theorem package.

## Claim-by-claim freeze ledger

| Item | Verdict | Freeze conclusion |
|---|---|---|
| Theorem 8.1, dyadic half-separation | **PASS (U)** | For every `q >= 1` and even `r=2s`, exactly `s` unit roots are simple; every possible repeated root has positive 2-adic valuation. |
| Theorem 8.1, prime-successor rows | **PASS (U)** | `P'_{q,p+1}` is square-free over `Q` for every odd prime `p` and every `q >= 1`. |
| Corollary 8.2, even rows through 5000 | **PASS (X)** | A single good-prime computation certifies every even `2 <= r <= 5000` for `q=1`. |
| Corollary 8.2, odd polar rows | **PASS (X)** | Degree preservation is now explicit; the nonconstant odd rows through 4999 pass, and the constant row `s=1` is handled separately. |
| Hypothesis DS | **OPEN** | It is assumed only in conditional Theorem 8.3 and never feeds an unconditional claim. |
| Theorem 8.3, density-one selection | **PASS (C)** | The implication from DS and the exponent `15/16` are unchanged and correctly labelled conditional. |
| Degree `m=27` repair | **PASS (X)** | All seven order classes modulo 28 have opposite-character witnesses modulo 29. |
| All orders through degree 1001 | **PASS (X)** | The repaired exact audit terminates with `AUDIT=PASS`. |
| Original order through degree one million | **PASS (X)** | Frozen source and log hashes agree with the displayed hashes. |
| Universal all-odd theorem | **OPEN** | No finite audit or DS partial result is promoted to universal selection. |
| Irrationality/transcendence of Euler's constant | **OPEN** | Still explicitly untouched. |

## 1. Audit of the new Section 8

### 1.1 Dyadic half-separation

The normalization

\[
c_q=2^{q+1},\qquad f_q(z)=E_q(c_qz)/c_q,
\qquad \widehat P_{q,r}(X)=c_q^rP_{q,r}(X/c_q)
\]

agrees with `EVEN_DERIVATIVE_SEPARABILITY.md`.  The exact valuation formula
leaves

\[
f_q(z)\equiv z+z^2\pmod 2.
\]

For `r=2s` and `a=v_2(r)`, the reduction

\[
2^{-a}\widehat P'_{q,2s}(X)
 \equiv X^{s-1}\Lambda_{2s+1}(X)\pmod2
\]

has full degree `2s-1` and unit leading coefficient.  The Lucas quotient
`Lambda_{2s+1}` has exactly `s` distinct nonzero roots.  They lift simply;
all remaining roots reduce to zero.  Thus the wording "exactly the unit
roots" and "every possible repeated root lies in the positive-valuation
disk" is justified, not merely the weaker count of `s` simple roots.

This matches the independent verdict in
`EVEN_DERIVATIVE_SEPARABILITY_REFEREE.md`.

### 1.2 Prime-successor separability

For `m=p+1`, the derivative Newton polygon is

\[
(0,-1)\longrightarrow(1,-q-1)\longrightarrow(p,0).
\]

The first edge is linear.  After an algebraic-closure scaling, the nonzero
initial form on the second edge has exponent gap `p-1`, which is prime to
the residue characteristic `p`.  Hence both clusters are separable.  The
all-order characteristic-zero conclusion in (8.4) is correct.

### 1.3 Exact row and polar audit

The added degree-preservation sentence closes the only expository gap noted
by the specialist referee.  At the modulus `998244353`, the relevant polar
leading coefficients are

\[
s+1,\qquad (s-1)(s+1)
\]

for odd `3 <= s <= 4999`, and are nonzero.  The even-row and polar gcd tests
therefore retain their characteristic-zero degrees.  The exact hashes in
the addendum agree with the files:

```text
d9c6f7c6438a9e7bf5d0aed50bbce727f460efcacc720f520c97b444b3f83b4d  even_derivative_separability_audit.cpp
1e4b4073527d7d2543c8a087c37f0888fdbd99c7ca2b7880a418e7c533e6617b  even_derivative_separability_audit_5000.txt
```

The manuscript correctly records the inseparable residual face
`1+Y^2` in row `r=10` as a barrier to naive recursion, not as a
counterexample to DS.

## 2. The repaired degree-27 certificate

The simultaneous bad window-prime locus is

\[
q\equiv1075\pmod{1584}.
\]

Because `1584` has gcd `4` with `28`, this progression occupies exactly

\[
3,7,11,15,19,23,27\pmod{28}.
\]

The addendum now checks all seven classes.  An independent rerun of
`odd_trace_modp_route.py` returned

```text
m=27, q mod 28 in [3, 7, 11, 15, 19, 23, 27], p=29
gcd degrees={3: 0, 7: 0, 11: 0, 15: 0, 19: 2, 23: 0, 27: 0}
```

and the seven asserted opposite-character witness pairs.  In particular,
the class `q=19 mod 28` is handled by opposite characters, not by the false
claim that its critical-value polynomial is square-free.

`ODD_TRACE_MODP_ROUTE.md` lists resultants whereas the integrated addendum
lists discriminants.  In degree 27 these differ by a global minus sign.
Accordingly the numerical values in the two tables are negatives modulo 29;
there is no contradiction, and `-1` is a square modulo 29, so the quadratic
characters agree.

No stale one-class implication remains in either
`ODD_TRACE_MODP_ROUTE.md` or `odd_trace_modp_route.py`.  Their current hashes
are

```text
2acebc4b6214c91cb5a63a74e45d11364f109f7be99029c76b74f6a822eaaf19  ODD_TRACE_MODP_ROUTE.md
fe01328be367386db7f82a22a7dbc2097839114092697a02e033ade4d996a4c7  odd_trace_modp_route.py
```

The production all-order audit also reran to `AUDIT=PASS`, with the seven
classes and the unchanged empty simultaneous bad locus at `m=989`.  Its
frozen hashes match the addendum:

```text
36ba3fd004df1e5a56a7bb6c61ed49cf7542d6f7c934ba458f88c1ebe105c31c  trace_allq_modp_audit.py
1d4867aa086b4315d45d70c52ef27090ad4d1c256cd956cb6b18d72a8be374be  trace_allq_modp_audit_1001.txt
```

The count `492+6+2=500` covers exactly all odd degrees from 3 through 1001.

## 3. Numbering, cross-references, abstract, and ledger

All displayed equation tags are unique and sequential within Sections 3--8:

- (3.1)--(3.2);
- (4.1)--(4.9);
- (5.1)--(5.2);
- (6.1)--(6.5);
- (7.1)--(7.9);
- (8.1)--(8.9).

Every numbered equation cited in prose exists.  Theorem and corollary
numbering is consistent: Theorem 8.1 is unconditional partial separability,
Corollary 8.2 is the exact finite rectangle, and Theorem 8.3 is the
DS-conditional density-one result.

The abstract, integration map, and claim ledger now agree on all scope
boundaries:

- prime degrees and fixed-degree sufficiently large orders are Morse;
- the finite rectangles assert symmetric monodromy, not universal Morse;
- half-separation, prime-successor separability, and the row-5000 audit do
  not prove DS;
- density one is only for `q=1` under DS;
- universal odd-composite selection and every claim about Euler's constant
  remain open.

The million-degree source and log hashes also agree with the addendum:

```text
e2eb3b8a14f758d84c0d80a4ed3c0ed11a3cf7eb38e3935960be3122d8fdcbf0  window_prime_selection_audit.py
51d3a027e9f0ce42f4918b39058288cdfdf808e25ded994ed009a701bc7c44f5  window_prime_selection_audit_1000000.txt
```

## 4. Mandatory artifact-version patches before delivery

1. `output/source/KEIO_Trace_Barrier_Escape_Addendum_v2_4.tex` was still
   generated from a pre-repair Markdown snapshot during this audit: it
   contains the obsolete one-class degree-27 sentence and does not contain
   the new Section 8 partial-separability material.  Regenerate the TeX,
   standalone PDF, and consolidated PDF from the frozen Markdown and render
   check the seven-row table.
2. `INTEGRATED_ADDENDUM_FINAL_REFEREE.md` records an older addendum hash and
   the now-obsolete statement that DS is used in Theorem 8.1.  It is a useful
   historical audit of the degree-27 repair, but this report supersedes it as
   the controlling freeze verdict.

`NEW_BARRIER_ESCAPE_REFEREE.md` already carries a prominent supersession
notice, and `WINDOW_PRIME_SELECTION_REFEREE.md` already contains the hardened
source hash and records the strict-window repair as resolved.

Subject to the two artifact-version actions above, the package is internally
consistent and ready to freeze.  The mathematical verdict is **PASS**; the
remaining actions are regeneration and version-labeling only.

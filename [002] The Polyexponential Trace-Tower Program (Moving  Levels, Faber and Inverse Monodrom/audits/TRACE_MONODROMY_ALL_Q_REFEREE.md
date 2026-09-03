# Independent referee report: `TRACE_MONODROMY_ALL_Q.md`

## Verdict

**PASS.**  I found no mathematical error in the all-\((q,m)\) theorem.  The
argument proves what it claims and does not rely on the separate finite-range
Morse certificates for \(q=1\).

The precise unconditional output is:

\[
P_{q,m}\text{ is indecomposable over }\overline{\mathbf Q}
\quad(q\geq1,m\geq2),
\]

\[
G^{\rm geom}_{q,m}\in\{A_m,S_m\},
\]

with geometric and arithmetic \(S_m\) for even \(m\), and arithmetic
\(S_m\) for odd nonsquare \(m\).  The note correctly leaves geometric odd
degrees and arithmetic odd-square degrees unresolved by the uniform
argument.

## Checks performed

### 1. Faber decomposition obstruction

The normalized Faber identity has the correct sign and normalization.  If
\(P_m=G\circ H\), one can simultaneously make \(G,H\) monic and arrange
\(G(0)=H(0)=0\).  Applying the inverse branch of \(G\) at infinity to

\[
P_m(M(w))=w^m+O(1)
\]

shows that \(H(M(w))=w^b+\text{constant}+O(w^{-1})\); Faber uniqueness then
indeed gives \(H=P_b\).

The coefficient used in the obstruction is also correct:

\[
P_b(M(w))=w^b-\Phi_b(0)+b d_bw^{-1}+O(w^{-2}).
\]

In the leading outer power, the coefficient of
\(w^{b(a-1)-1}\) is uniquely \(ab d_b\).  A constant term creates deficit
\(b\), a negative term \(w^{-j}\) creates deficit \(b+j\), and there are no
terms of degrees \(b-1,\ldots,1\); hence neither another selection in
\(P_b^a\) nor a lower outer power can reach that exponent.  Thus a
decomposition forces \(d_b=0\).

### 2. Exact 2-adic valuation

For

\[
A_q(z)=\sum_{n\ge0}\frac{(-1)^n}{n!(n+1)^{q+1}}z^n,
\]

the scaled coefficient has valuation

\[
(q+1)n-v_2(n!)-(q+1)v_2(n+1)
=qn+s_2(n)-(q+1)r,
\quad r=v_2(n+1).
\]

It is zero exactly at \(n=0,1\) and positive for \(n\ge2\).  Therefore

\[
A_q(2^{q+1}z)\equiv1+z\pmod2,
\qquad
B_q(2^{q+1}z)\equiv(1+z)^{-1}\equiv\sum_{n\ge0}z^n\pmod2,
\]

which proves, coefficient by coefficient,

\[
v_2(B_{q,n})=-(q+1)n.
\]

I independently expanded \(B_q\) for \(1\le q\le4\), \(0\le n\le10\);
every value matches this formula.

### 3. Centered invariants and exceptional cases

Direct symbolic expansion confirms

\[
C_2=m(a_3-a_2^2),\qquad
C_3=m(a_2^3-2a_2a_3+a_4),
\]

and, for \(E_q\), the displayed \(N_A(q),N_B(q)\) formulas.  Here
\(N_A(q)\ne0\) and \(N_B(q)\equiv1\pmod3\), so the cyclic and proper
dihedral possibilities are excluded by the indicated centered
coefficients.

After making each of Müller's three rational exceptional representatives
monic and centered, symbolic calculation gives exactly

| degree | \(C_2\) | \(C_3\) | \(C_3^2/C_2^3\) |
|---:|---:|---:|---:|
| 6 | 10 | -60 | \(18/5\) |
| 9 | 12 | 8 | \(1/27\) |
| 10 | -1800 | -24000 | \(-8/81\) |

The sign and 3-adic arguments excluding equality with \(R_q/m\) are
correct.  Müller's rational-coefficient classification applies here because
indecomposability over \(\overline{\mathbf Q}\) makes the geometric
monodromy primitive, and \(P_{q,m}\in\mathbf Q[X]\).  Its rational theorem
leaves precisely the alternating/symmetric, cyclic/dihedral, and these three
sporadic cases.

### 4. Geometric versus arithmetic discriminant conclusions

For monic degree \(m\), the note has the correct leading term

\[
\operatorname{Disc}_X(P(X)-T)
=(-1)^{m(m-1)/2+m-1}m^mT^{m-1}+\cdots.
\]

For even \(m\), the inertia \(m\)-cycle at infinity is odd, so the geometric
group is \(S_m\), and consequently so is the arithmetic group.  For odd
\(m\), the leading square class is

\[
(-1)^{(m-1)/2}m.
\]

It is not a rational square when \(m\) is not a square; hence the arithmetic
discriminant is not a square in \(\mathbf Q(T)\), and the arithmetic group is
\(S_m\).  For odd squares, the note correctly claims only that this test is
silent.  It also correctly distinguishes the stronger geometric obstruction
\(D(T)\ne cR(T)^2\) from the arithmetic nonsquare test.

## Nonblocking editorial reinforcements

These are not corrections and do not change the PASS verdict:

1. In Lemma 3, add the one-sentence deficit argument above to make the word
   “unique” completely transparent.
2. At the first use of Müller, explicitly say that the cited rational
   theorem classifies the **geometric** monodromy of an indecomposable
   polynomial in \(\mathbf Q[X]\), and that linear equivalence is taken over
   \(\mathbf C\) (equivalently here over \(\overline{\mathbf Q}\)).
3. In the invariant paragraph, say that after monic normalization \(C_2,C_3\)
   scale by reciprocal weights \(2,3\) (or choose the opposite input-scaling
   convention); only the invariant ratio matters.

## Scope guard

Nothing in this report upgrades the all-\((q,m)\) result to a uniform Morse
theorem.  The \(q=1\), \(m\le401\) computation remains an independent finite
certificate and is correctly presented as such.

# Hostile referee audit: abstract Faber moving-prime transfer

## Scope and verdict

This report independently audits ABSTRACT_FABER_MOVING_PRIME_TRANSFER.md,
with special attention to indexing, residue characteristic, ramification,
Newton-polygon endpoints, critical-value separation, and the local-to-global
monodromy step.

**Overall verdict: PASS, with four expository qualifications and no fatal
mathematical gap.** The hypotheses (S1)--(S5) force the claimed derivative
Newton polygon. The horizontal polar is exactly the smaller trace derivative.
The possible division by \(p\) is integral, including at ramified places. The
three critical-value valuations are also correct. Under geometric
indecomposability, the isolated simple branch point forces full symmetric
geometric and arithmetic monodromy. The polylogarithmic and
hypergeometric-type valuation checks are correct over \(\mathbf Q_p\), and
the logarithmic--Stirling \(S_{p+2}\) family is unconditional.

The four qualifications are:

1. In the global clause of Theorem 4.1, say explicitly that \(L=K_v\), or
   that \(L\) is a valued extension of a completion of \(K\), and that the
   local hypotheses hold at that place.
2. In Section 3, \(\bar A\) must mean the reduction of the integral low
   truncation. The full \(A\) has negative-valuation coefficients and cannot
   literally be reduced.
3. In Section 6.2, write the index shift
   \(d_b=[z^b](1/f)=[z^{b+1}](z/f)\) before invoking Faber rigidity.
4. If the examples are transported from \(\mathbf Q_p\) to a ramified
   extension normalized by \(v(\pi)=1\), multiply the displayed \(h,s\) by
   the ramification index.

None of these changes alters a theorem or application.

## Claim-by-claim ledger

| Claim | Verdict | Referee conclusion |
|---|---|---|
| Universal identities (1.2)--(1.3) | **PASS** | Exact coefficient extraction; all indices are correct. |
| Monicity and zero constant term | **PASS** | The \(k=m\) term is \(X^m\), since \(a_0=1\). |
| Three-edge derivative Newton polygon | **PASS** | Exact endpoints at \(j=0,1,r,m-1\); intervening points lie on or above the hull. |
| Critical-root populations (2.5) | **PASS** | Edge lengths \(1,r-1,p-1\) give exactly the stated valuations. |
| Polar descent (3.4)--(3.5) | **PASS** | The factor is \(\bar m\eta/r\), and the shift is \(X^2R_r\). |
| Removal of the \(X^p\) denominator | **PASS** | \([z^r]A^p\in p\mathcal O\) for \(0<r<p\), also when \(v(p)>1\). |
| GCD obstruction (3.7) | **PASS** | Simultaneous first-polar cancellation is exactly \(R_r=R_r'=0\). |
| First-cluster critical value | **PASS** | One simple critical point, value valuation \(h-2s\). |
| Unit-cluster critical values | **PASS** | Each has valuation exactly \(-h\) under \(\gcd(R_r,R_r')=1\). |
| Outer-cluster critical values | **PASS** | Roots are simple and values have valuation \(-mh/(p-1)\). |
| Isolated transposition | **PASS** | Strict valuation separation leaves one simple ramification point over \(b\). |
| Primitive plus transposition | **PASS** | Geometric indecomposability gives primitivity and hence \(S_m\). |
| \(r=2\) automatic condition | **PASS** | \(R_2\) is linear with unit leading coefficient; necessarily \(p\ge5\). |
| Polylogarithmic application | **PASS** | Correct with \(h=\tau,s=0\) over \(\mathbf Q_p\). |
| Hypergeometric-type application | **PASS** | Correct with \(h=\sigma+\tau,s=\sigma\) over \(\mathbf Q_p\). |
| Logarithmic--Stirling formula | **PASS** | The factors \((m-1)!\) and \((k-1)!\) are correct. |
| Indecomposability of the logarithmic traces | **PASS** | Reciprocal coefficients are nonzero after the one-step index shift. |
| Unconditional logarithmic \(S_{p+2}\) family | **PASS** | Local transfer plus absolute indecomposability proves both groups. |

## 1. Universal identities

Expanding the logarithm gives

\[
 P_m^f(X)=m\sum_{k=1}^m\frac{X^k}{k}
 [z^{m-k}]A(z)^k.
\]

This proves (1.2). Differentiating and putting \(j=k-1\) gives

\[
 [X^j](P_m^f)'=m[z^{m-j-1}]A^{j+1},
\]

so (1.3) is exact. The \(k=m\) coefficient is \(a_0^m=1\), proving
monicity. There is no off-by-one error.

## 2. Newton-polygon audit

Put \(N_j=m-j-1=p+r-j-1\). The four vertices are exact:

- \(d_0=ma_{m-1}\), hence \(v(d_0)=-s\).
- In \(d_1=m[z^{m-2}]A^2\), a valuation-\(-h\) term must use
  \(a_{p-1}\), leaving degree \(r-1\). Its two placements give
  \(2ma_{p-1}a_{r-1}\). Since \(p\) is odd and \(m,a_{r-1}\) are units,
  there is no residual cancellation, so \(v(d_1)=-h\).
- For \(d_r\), the unique initial contribution uses one spike and \(r\)
  copies of \(a_0\), with multiplicity \(r+1\). Since \(r\le p-2\),
  \(r+1\) is a unit, so \(v(d_r)=-h\).
- \(d_{m-1}=m\) is a unit because \(m\equiv r\not\equiv0\pmod p\).

For \(1\le j\le r\), a term using the spike leaves degree \(r-j\) among
the other \(j\) factors, all in the integral low range. A term without the
spike contains at most one tail coefficient and has valuation at least
\(-s>-h\). For \(j>r\), \(N_j<p-1\), so only integral low coefficients
occur. Hence every nonvertex point is on or above

\[
 (0,-s)\longrightarrow(1,-h)\longrightarrow(r,-h)
 \longrightarrow(m-1,0).
\]

The edge lengths are \(1,r-1,p-1\), and the slopes are
\(-(h-s),0,h/(p-1)\). Root valuation is minus slope, giving (2.5).

The bounds \(2\le r\le p-2\) are essential here: they make \(m,r,r+1\)
units, prevent two spikes in one extraction, and give the last edge length
\(p-1\).

## 3. Polar descent and the apparent denominator

For \(1\le j\le r\), selecting the spike once gives

\[
 \overline{\pi^h d_j}
 =\bar m(j+1)\eta[z^{r-j}]\bar A(z)^j.
\]

Only \(a_0,\ldots,a_{r-j}\) occur, so this is the reduction of the low
integral truncation. Since the coefficient of \(X^{j+1}\) in \(P_m^f\) is
\(d_j/(j+1)\), summing gives

\[
 \bar m\eta\sum_{j=1}^r C_jX^{j+1}
 =\frac{\bar m\eta}{r}X^2R_r(X).
\]

Differentiation gives (3.5). The factors \(X^2\), \(1/r\), and \(j+1\)
are correctly placed.

The only coefficient integration can divide by the residue characteristic
is the coefficient of \(X^p\), namely \(d_{p-1}/p\). Since \(r<p\), every
coefficient used in \([z^r]A^p\) is integral. In the multinomial expansion,
a term whose multinomial coefficient is not divisible by \(p\) would have
all \(p\) choices equal, forcing total degree divisible by \(p\). That is
impossible for \(0<r<p\). Therefore

\[
 [z^r]A^p\in p\mathcal O.
\]

This is divisibility by the integer \(p\), not only by \(\pi\). Thus
division by \(p\) remains integral even if \(v(p)=e>1\).

For a unit critical reduction \(\beta\), the derivative initial form gives
\(2R_r(\beta)+\beta R_r'(\beta)=0\). If \(R_r(\beta)=0\), then
\(R_r'(\beta)=0\), because \(\beta\ne0\). Hence square-freeness of \(R_r\)
is exactly the advertised first-polar sufficient condition for a nonzero
principal critical value. It is not asserted to be necessary for the final
monodromy conclusion.

## 4. Critical values and ramification

Let \(\alpha\) be the root on the length-one edge. Then
\(v(\alpha)=h-s>0\) and

\[
 d_1\alpha=-d_0+\text{higher-valuation terms}.
\]

The term \(d_1\) uniquely dominates \(P_m''(\alpha)\), so \(\alpha\) is
simple. As \(2\) is a unit,

\[
 P_m(\alpha)=d_0\alpha+\frac{d_1}{2}\alpha^2+\cdots
 =\frac12d_0\alpha+\cdots,
\]

and \(v(P_m(\alpha))=h-2s\). The \(X^p\) coefficient is integral by the
preceding argument and evaluates to strictly higher valuation.

For each unit critical point, nonvanishing of the polar value gives value
valuation exactly \(-h\). This does not require the unit critical points
themselves to be simple.

On the outer edge the derivative initial form is
\(d_rX^r+mX^{m-1}\). The exponent gap \(p-1\) is prime to the residue
characteristic, so its \(p-1\) nonzero roots are simple. Using the critical
equation in the two leading terms of \(P_m\) gives

\[
 d_rX^{r+1}\left(\frac1{r+1}-\frac1m\right)
 =d_rX^{r+1}\frac{p-1}{m(r+1)}.
\]

Every displayed denominator and \(p-1\) is a unit. Since
\(v(X)=-h/(p-1)\), the value valuation is

\[
 -h-\frac{(r+1)h}{p-1}=-\frac{mh}{p-1}.
\]

Finally,

\[
 -\frac{mh}{p-1}<-h<h-2s
\]

because \(m>p-1\) and \(h>s\). Thus \(b=P_m(\alpha)\) cannot equal any
other critical value. A unique simple critical point over a branch value
has ramification index \(2\), so the geometric branch cycle is a
transposition. This is characteristic-zero geometric inertia at the branch
value, not a claim about wild inertia at the auxiliary \(p\)-adic place.

If \(P_m\) is indecomposable over \(\overline K\), its geometric polynomial
monodromy is primitive. A primitive subgroup of \(S_m\) containing a
transposition is \(S_m\). The arithmetic group contains the geometric
group and is therefore also \(S_m\).

For formal completeness, the global statement should identify the chosen
embedding of \(K\) into \(L=K_v\), or into a valued extension of \(K_v\).

## 5. Applications

### 5.1 Polylogarithmic traces

For \(f=\operatorname{Li}_\tau\), \(a_n=(n+1)^{-\tau}\). Over
\(\mathbf Q_p\), the coefficients through \(a_{p-2}\) are units,
\(a_{r-1}\) is a unit, \(a_{p-1}=p^{-\tau}\) has valuation \(-\tau\), and
the coefficients \(a_p,\ldots,a_{m-1}\) are units. Thus
\(h=\tau,s=0\). At \(r=2\), square-freeness is automatic, giving an
isolated transposition for every \(p\ge5\). The note correctly does not
claim full \(S_{p+2}\) here without indecomposability.

### 5.2 Entire hypergeometric-type traces

Here

\[
 a_n=\frac1{((n+1)!)^\sigma(n+1)^\tau}.
\]

The factorial has \(p\)-adic valuation \(0\) for \(n+1<p\), and valuation
\(1\) for \(p\le n+1<2p\). The extra \(n+1\) factor contributes \(\tau\)
only at \(n=p-1\). Hence over \(\mathbf Q_p\)

\[
 h=\sigma+\tau,\qquad s=\sigma.
\]

Since \(\tau\ge1\), \(h>s\). Again, the note correctly stops at a
transposition unless indecomposability is independently proved.

In a ramified extension normalized by \(v(\pi)=1\), these examples instead
have \(h=e\tau,s=0\) and
\(h=e(\sigma+\tau),s=e\sigma\), respectively. This is only a normalization
change.

### 5.3 The logarithmic--Stirling family

The standard generating function

\[
 \frac{(-\log(1-z))^k}{k!}
 =\sum_{m\ge k}|s(m,k)|\frac{z^m}{m!}
\]

inserted into (1.1) gives

\[
 [X^k]P_m^f=\frac{(k-1)!|s(m,k)|}{(m-1)!},
\]

so (6.3) is exact.

For indecomposability, put

\[
 B(z)=\frac z{-\log(1-z)}=\int_0^1(1-z)^t\,dt.
\]

For \(n\ge1\), \(\binom tn\) has sign \((-1)^{n-1}\) throughout
\(0<t<1\). Hence

\[
 B_n=(-1)^n\int_0^1\binom tn\,dt<0.
\]

Writing \(1/f=z^{-1}B(z)=z^{-1}+\sum_{b\ge0}d_bz^b\), the precise index
relation is

\[
 d_b=B_{b+1}<0\qquad(b\ge0).
\]

The normalized-Faber right-factor lemma says that a decomposition
\(P_m^f=G\circ H\) with inner degree \(b>1\) forces \(d_b=0\). Since no
\(d_b\) vanishes, \(P_m^f\) is indecomposable over \(\mathbf C\) for every
\(m\ge2\). Thus the global input is proved rather than assumed.

At \(m=p+2\), \(p\ge5\), the local theorem supplies a transposition and the
preceding paragraph supplies absolute indecomposability. Therefore

\[
 \operatorname{Gal}(P_{p+2}^f(X)-T/\mathbf C(T))
 =\operatorname{Gal}(P_{p+2}^f(X)-T/\mathbf Q(T))
 =S_{p+2}.
\]

This family is unconditional. The geometric group over \(\mathbf C(T)\)
equals that over \(\overline{\mathbf Q}(T)\) by invariance under extension
between algebraically closed characteristic-zero constant fields.

## 6. Required wording fixes before integration

The source can be integrated after these non-substantive clarifications:

1. Replace the global clause of Theorem 4.1 by: let \(K\) be a number field,
   let \(v\mid p\), take \(L=K_v\), or a valued extension, and assume
   (S1)--(S5) at \(v\).
2. In (3.1), define
   \(\bar A_{<p}(z)=\sum_{n=0}^{p-2}\bar a_nz^n\) and use it in \(C_j\).
3. In Section 6.2, insert
   \(d_b=[z^b](1/f)=[z^{b+1}](z/f)=B_{b+1}\), and state the exact Faber
   obstruction invoked.
4. Label the \(h,s\) values in Sections 6.1 and 6.3 as
   \(\mathbf Q_p\)-normalized values.

With these qualifications, every advertised conclusion survives hostile
review.

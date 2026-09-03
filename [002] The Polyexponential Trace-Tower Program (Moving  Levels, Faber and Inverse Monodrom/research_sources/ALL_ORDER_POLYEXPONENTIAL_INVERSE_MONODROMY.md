# All-order inverse monodromy for the polyexponential tower

**Research status (2026-09-01).**  This note records a new analytic deduction
from the polyexponential tower.  It has not been inserted in the Moving-Level
manuscript.  Uniform incomplete-gamma remainders, contraction boxes, and the
covering-space argument are included below so that the proof is logically
self-contained apart from the quoted standard large-variable remainder
theorem.  In particular, **global pairwise noncollision of all critical
values is neither assumed nor claimed**.

Put

\[
 F_q(z)=\operatorname{Ein}_q(z)
 =\sum_{n\geq1}\frac{(-1)^{n-1}z^n}{n!n^q},\qquad q\geq1,
\]

and put \(F_0(z)=1-e^{-z}\).  Then

\[
 zF_q'(z)=F_{q-1}(z).
\tag{0.1}
\]

The principal result is

> **Theorem A (all-order maximal inverse monodromy).**  For every fixed
> integer \(q\geq1\) and every regular value \(c_0\) (that is, \(c_0\) is
> not a critical value),
> \[
>  \operatorname{Mon}_{c_0}(F_q^{-1})
>  =\operatorname{FSym}(F_q^{-1}(c_0))
>  \cong\operatorname{FSym}(\mathbb N).
> \tag{0.2}
> \]

For \(q=1\), all critical points are simple and all critical values are
pairwise distinct.  For \(q\geq2\), those two global statements are not
needed: the proof shows that degeneracies and critical-value collisions, if
any, form only a finite exceptional set.  A finite-exception permutation
lemma then upgrades the tail transpositions to the full finitary symmetric
group.

## 1. Polynomial plus exponential decomposition

For small \(u\),

\[
 \begin{aligned}
 \Phi(u,z)
 &:=\sum_{q\geq1}F_q(z)u^{q-1}\\
 &=\frac{z^u\Gamma(1-u)-1}{u}+z^u\Gamma(-u,z).
 \end{aligned}
\tag{1.1}
\]

Write \(w=\Log z+\gamma\) on the principal sheet and define

\[
 Q_q(w)=[u^q]\exp\!\left(
 wu+\sum_{m\geq2}\frac{\zeta(m)}m u^m\right).
\tag{1.2}
\]

Thus

\[
 Q_0=1,\qquad Q_q'=Q_{q-1},\qquad
 Q_q(w)=\frac{w^q}{q!}+O_q(|w|^{q-2}),
\tag{1.3}
\]

with the obvious interpretation for \(q=1\), and

\[
 F_q(z)=Q_q(\Log z+\gamma)+R_q(z),\qquad
 R_q(z)=[u^{q-1}]z^u\Gamma(-u,z).
\tag{1.4}
\]

The upper-incomplete-gamma expansion, uniformly for \(|\arg z|\leq\pi\)
with upper and lower boundary values on the cut, gives

\[
 z^u\Gamma(-u,z)
 =\frac{e^{-z}}z\left(
 \sum_{k=0}^{N-1}\frac{(-1)^k(1+u)_k}{z^k}
 +O_N(|z|^{-N})\right).
\tag{1.5}
\]

Here and below the required uniformity has the following precise meaning.
Fix \(0<\eta<1\).  The standard large-variable remainder theorem for the
upper incomplete gamma function, applied with \(a=-u\) in the compact set
\(|u|\leq\eta\), says that for every \(N\geq1\)

\[
 z^u\Gamma(-u,z)=\frac{e^{-z}}z
 \left(\sum_{k=0}^{N-1}\frac{(-1)^k(1+u)_k}{z^k}
       +E_N(u,z)\right),
 \qquad
 \sup_{|u|\leq\eta}|E_N(u,z)|\leq C_{N,\eta}|z|^{-N}.
\tag{1.5a}
\]

This holds on \(|\arg z|\leq\pi\), with the corresponding boundary branch
on either side of the negative axis.  It is the compact-parameter form of
the usual fixed-parameter expansion (for example, NIST DLMF, \S8.11(i)); it
follows from the same contour-integral remainder after the parameter is
restricted to a compact set.  The remainder is holomorphic in \(u\).
Consequently Cauchy's formula on \(|u|=\eta\) gives, for every fixed \(j\),

\[
 |[u^j]E_N(u,z)|\leq C_{N,\eta}\eta^{-j}|z|^{-N}.
\tag{1.5b}
\]

On each closed subsector strictly inside \(|\arg z|<3\pi/2\), the same
remainder theorem may be differentiated in \(z\), and, after enlarging the
constant,

\[
 \sup_{|u|\leq\eta}|\partial_zE_N(u,z)|
 \leq C_{N,\eta}|z|^{-N-1}.
\tag{1.5c}
\]

For completeness, (1.5c) also follows from (1.5a) without a separate
differentiated theorem: put the chosen closed subsector inside a slightly
larger one and apply Cauchy's derivative estimate on a circle of radius
\(\varepsilon|z|\).  In particular it holds in the upper and lower sectors
about the imaginary axes used in Section 3.  Cauchy's formula in \(u\)
applies to (1.5c) as well.  These uniform statements justify both
coefficient extraction and the derivative estimate for the contraction maps
below.

Coefficient extraction yields

\[
 R_q(z)=(-1)^{q-1}\frac{e^{-z}}{z^q}
 \left(1-\frac{q(q+1)}{2z}+O_q(z^{-2})\right).
\tag{1.6}
\]

Indeed, \((1+u)_k\) has degree \(k\); its coefficient of \(u^{q-1}\) first
occurs at \(k=q-1\), where it equals \(1\), and at \(k=q\) that coefficient
is \(1+\cdots+q=q(q+1)/2\).  Taking \(N\geq q+1\) in (1.5a)--(1.5b) proves
(1.6), including its uniform error.  For later uniform notation set

\[
 Q_0=1,\qquad R_0(z)=-e^{-z},\qquad F_0=Q_0+R_0.
\tag{1.7}
\]

Formula (1.6), together with (1.7), is the analytic engine for everything
that follows.

## 2. No finite asymptotic values in any order

> **Lemma 2.1.**  For every \(q\geq1\) and \(M>0\), every connected
> component of
> \[
>  \{z:|F_q(z)|<M\}
> \]
> is bounded.  Consequently \(F_q\) has no finite asymptotic value.

Let \(z=x+iy\), \(r=|z|\), \(L=\log r\),
\(\theta=\arg z\in[-\pi,\pi]\), and put \(w=\Log z+\gamma\).  Uniformly
as \(r\to\infty\),

\[
 Q_q(w)=\frac{w^q}{q!}\left(1+O_q(L^{-2})\right),
 \qquad
 R_q(z)=(-1)^{q-1}e^{-z}z^{-q}\left(1+O_q(r^{-1})\right).
\tag{2.0}
\]

If \(|F_q(z)|\leq M\), then \(|Q_q(w)|\asymp_q L^q\), and (1.4) gives

\[
 \frac{R_q(z)}{Q_q(w)}=-1+O_{q,M}(L^{-q}).
\tag{2.0a}
\]

Taking logarithmic moduli in (2.0)--(2.0a), and using
\(\log|w|=\log L+O(L^{-1})\), gives the following estimate uniformly on
the bounded sublevel, not merely along a selected sequence:

\[
 x=-qL-q\log L+\log(q!)+O_{q,M}(L^{-1}).
\tag{2.1}
\]

Hence \(|y|\sim r\) and
\(\arg z=\operatorname{sgn}(y)\pi/2+O_q(L/r)\).  Taking arguments in the
same cancellation gives

\[
 (q-1)\pi-y-q\theta
 \equiv \pi+\arg Q_q(w)+O_{q,M}(L^{-q})\pmod{2\pi}.
\]

Since \(\arg Q_q(w)=q\arg w+O_q(L^{-2})\) and
\(\arg w=\theta/L+O(L^{-2})\), it follows, separately in the upper and
lower half-planes, that

\[
 \operatorname{dist}\!\left(
 y,2\pi\mathbb Z+\operatorname{sgn}(y)\frac{q\pi}{2}
 \right)\leq \frac{C_{q,M}}L.
\tag{2.2}
\]

To justify explicitly the word ``uniformly'', if either (2.1) or (2.2)
failed outside every disk, a sequence of counterexamples tending to infinity
would contradict (2.0)--(2.0a).  Choose \(R=R(q,M)\) so that outside
\(\overline{D(0,R)}\) the sublevel is contained in the horizontal strips of
half-width \(\pi/4\) centered at the lattices in (2.2).  These strips are
pairwise disjoint after coincident strips are identified (the upper and
lower lattices either agree or differ by \(\pi\)).

The intersection of the sublevel with any one fixed strip is bounded.
Indeed, otherwise it would contain a sequence with bounded \(y\) and
\(|x|\to\infty\), whereas (2.1) says that \(x\) has only logarithmic size in
\(|x|\), an impossibility.  Components of an open subset of \(\mathbb C\)
are path-connected.  A component avoiding \(\overline{D(0,R)}\) is therefore
contained in one strip and is bounded.  If a component meets the disk, then
every remote strip used by it meets \(\partial D(0,R)\): follow a path from
the disk to a point in that strip and take its last exit from the disk.  Only
finitely many of the strips meet that circle, and the sublevel part in each
of them is bounded.  The component is again bounded.

If \(F_q(\gamma(t))\to a\) along a curve \(\gamma(t)\to\infty\), then for
some \(M>|a|\) a tail of \(\gamma\) is a connected unbounded subset of
\(\{|F_q|<M\}\), hence lies in an unbounded component.  This contradiction
proves the last assertion of the lemma.

Also, every \(F_q\) is surjective.  Since \(F_0(x)\) has the sign of \(x\),
(0.1) and induction show that \(F_q'(x)>0\) for real \(x\).  The positive
and negative real-axis versions of (1.4)--(1.6) give respectively
\(F_q(x)\to+\infty\) as \(x\to+\infty\) and
\(F_q(x)\to-\infty\) as \(x\to-\infty\).  Thus no real value is omitted.
The function is transcendental entire and has real Taylor coefficients, so
a nonreal omitted value would force its distinct conjugate to be omitted as
well, contrary to Picard's theorem.

## 3. Large zeros and eventual separation of critical values

The following is the required Hardy-type zero lemma.  Recall that
\(F_p(z)=z e(-z,1\mid p+1)\) in Hardy's polyexponential notation, so its
leading zero distribution goes back to Hardy.  The derivative and
critical-value consequences below are what are needed for monodromy.

> **Lemma 3.1 (zero boxes).**  Fix \(p\geq1\).  Apart from finitely many
> zeros, the nonzero zeros of \(F_p\) are conjugate pairs
> \(\zeta_{p,n},\overline{\zeta_{p,n}}\), \(n\geq n_0(p)\), with exactly
> one upper zero in every corresponding large phase box.  There is a
> \(C^1\) (indeed real-analytic) parametrized fixed point
> \(\zeta_p(t)\), \(t\geq t_0\),
> whose integer samples are those zeros and for which
> \[
>  \begin{aligned}
>  \zeta_p(t)
>  &=2\pi it-p\log(2\pi t)-p\log\log(2\pi t)+O_p(1),\\
>  \zeta_p'(t)&=2\pi i+O_p(t^{-1}),\\
>  \Log\zeta_{p,n+1}-\Log\zeta_{p,n}
>  &=\frac1n+O_p\!\left(\frac{\log n}{n^2}\right).
>  \end{aligned}
> \tag{3.1}
> \]
> Every sufficiently large zero is simple.

Here is a direct proof with explicit boxes.  Put

\[
 \mathcal B_p(z)=(-1)^{p-1}e^z z^pR_p(z)
 =1-\frac{p(p+1)}{2z}+O_p(z^{-2}).
\]

Fix a large positive integer \(n\), put \(z_n^0=2\pi in\) and
\(L_n=\log(2\pi n)\), and initially work on a rough disk

\[
 E_{p,n}=\{z:|z-z_n^0|\leq C_p\log n\},
\tag{3.2a}
\]

where \(C_p\) is a sufficiently large fixed constant.  On this disk the
principal \(\Log z\) is defined and

\[
 w=\Log z+\gamma=L_n+\gamma+\frac{\pi i}{2}
    +O_p(\log n/n).
\]

Thus \(Q_p(w)\ne0\), and we choose its logarithm by

\[
 \log Q_p(w)=p\Log w-\log(p!)+O_p(w^{-2}).
\]

Also \(\mathcal B_p(z)\ne0\), and we choose
\(\log \mathcal B_p(z)\to0\).  The differentiated
uniform remainder in Section 1 gives

\[
 \mathcal B_p'(z)=O_p(n^{-2})\qquad (z\in E_{p,n}).
\tag{3.2b}
\]

At a zero of \(F_p\), exponentiation gives
\(e^zz^pQ_p(w)=(-1)^p\mathcal B_p(z)\).  With
\(\log((-1)^p)=i\pi p\), the corresponding fixed-point equation is

\[
 z=T_{p,n}(z):=2\pi in+i\pi p-p\Log z
 -\log Q_p(\Log z+\gamma)+\log \mathcal B_p(z).
\tag{3.2c}
\]

Using \(-i\pi p\) instead would merely replace \(n\) by \(n+p\); (3.2c)
fixes the phase index once and for all.  Define

\[
 c_{p,n}=T_{p,n}(z_n^0),\qquad
 D_{p,n}=\{z:|z-c_{p,n}|\leq1\}.
\tag{3.2d}
\]

The selected logarithms give

\[
 \begin{aligned}
 \Re c_{p,n}
 &=-pL_n-p\log L_n+\log(p!)+O_p(L_n^{-1}),\\
 \Im c_{p,n}
 &=2\pi n+\frac{p\pi}{2}
   -\frac{p\pi}{2L_n}+O_p(L_n^{-2}).
 \end{aligned}
\tag{3.2e}
\]

After increasing \(C_p\), the fixed-radius disk \(D_{p,n}\) lies in
\(E_{p,n}\) for every sufficiently large \(n\).  On the rough disk,

\[
 T_{p,n}'(z)=-\frac pz
 -\frac{Q_{p-1}(w)}{zQ_p(w)}
 +\frac{\mathcal B_p'(z)}{\mathcal B_p(z)}
 =O_p(n^{-1}).
\tag{3.2f}
\]

Consequently, for \(z\in D_{p,n}\), the line segment from \(z_n^0\) to
\(z\) lies in \(E_{p,n}\) and

\[
 |T_{p,n}(z)-c_{p,n}|
 \leq \frac{C_p}{n}|z-z_n^0|
 \leq \frac{C_p(1+\log n)}n<1,
\]

while \(\sup_{D_{p,n}}|T_{p,n}'|<1/2\).  Thus \(T_{p,n}\) has exactly one
fixed point in \(D_{p,n}\), and exponentiating (3.2c) shows that it is a
zero of \(F_p\).  The centers of consecutive disks differ by
\(2\pi i+o(1)\), so these disks are pairwise disjoint for large \(n\).

Conversely, (2.1)--(2.2), applied to the zeros with \(M=1\) and \(q=p\),
show that every
sufficiently large upper zero has a unique integer \(n\) for which

\[
 z=z_n^0+O_p(\log n),\qquad
 \Im z=2\pi n+\frac{p\pi}{2}+O_p(L_n^{-1}).
\]

With the logarithms selected above it satisfies precisely (3.2c), so (3.2f)
gives

\[
 |z-c_{p,n}|=|T_{p,n}(z)-T_{p,n}(z_n^0)|
 =O_p(\log n/n)<1.
\]

It is therefore the already constructed fixed point.  This proves both
existence in every large phase box and exhaustion of all large upper zeros;
conjugation gives the lower zeros.

For real \(t\) sufficiently large, replace \(n\) by \(t\) throughout the
same construction.  The estimates are locally uniform in \(t\), and
\(1-T_{p,t}'(\zeta_p(t))\ne0\).  The real implicit-function theorem gives a
local \(C^1\), indeed real-analytic, fixed point; uniqueness patches these
local functions into a single \(\zeta_p(t)\).  Differentiating (3.2c) yields

\[
 \zeta_p'(t)=\frac{2\pi i}{1-T_{p,t}'(\zeta_p(t))}
 =2\pi i+O_p(t^{-1}).
\]

Equation (3.2e) gives the first line of (3.1), and hence

\[
 \begin{aligned}
 \Log\zeta_p(n+1)-\Log\zeta_p(n)
 &=\int_n^{n+1}\frac{\zeta_p'(t)}{\zeta_p(t)}\,dt\\
 &=\int_n^{n+1}\left(\frac1t
    +O_p\left(\frac{\log t}{t^2}\right)\right)dt
 =\frac1n+O_p\left(\frac{\log n}{n^2}\right),
 \end{aligned}
\]

which completes (3.1).

Finally, consecutive-remainder division, with (1.7) when \(p=1\), gives

\[
 \frac{R_{p-1}(z)}{R_p(z)}
 =-z\left(1+\frac pz+O_p(z^{-2})\right).
\tag{3.2g}
\]

At a large zero of \(F_p\), \(R_p=-Q_p\), and therefore

\[
 \begin{aligned}
 F_{p-1}(z)
 &=Q_{p-1}(w)+R_{p-1}(z)\\
 &=zQ_p(w)\left(1+O_p(n^{-1})
   +O_p((n\log n)^{-1})\right)
 =zQ_p(w)(1+o(1)).
 \end{aligned}
\tag{3.3}
\]

Thus \(F_p'(z)=F_{p-1}(z)/z\ne0\) for every sufficiently large zero,
including \(p=1\).  Lemma 3.1 follows.

Now let \(q\geq2\), put \(p=q-1\), and define the upper critical values

\[
 b_{q,n}=F_q(\zeta_{p,n}).
\]

At a zero of \(F_p\), the quotient of two consecutive remainders in (1.6)
is

\[
 \frac{R_{p+1}(z)}{R_p(z)}
 =-\frac1z\left(1-\frac{p+1}{z}+O_p(z^{-2})\right).
\]

Since \(R_p=-Q_p\) there,

\[
 b_{q,n}=Q_{p+1}(w_n)+\frac{Q_p(w_n)}{\zeta_{p,n}}
 +O_p\!\left(\frac{(\log n)^p}{n^2}\right),
 \qquad w_n=\Log\zeta_{p,n}+\gamma.
\tag{3.4}
\]

Using \(Q_{p+1}'=Q_p\) and (3.1),

\[
 \delta w_n:=w_{n+1}-w_n
 =\frac1n+O_p\!\left(\frac{\log n}{n^2}\right).
\]

Taylor's formula, uniformly for \(w\) on the segment between \(w_n\) and
\(w_{n+1}\), gives

\[
 Q_{p+1}(w_{n+1})-Q_{p+1}(w_n)
 =Q_p(w_n)\delta w_n+O_p((\log n)^{p-1}n^{-2}).
\]

Moreover

\[
 \frac{Q_p(w_{n+1})}{\zeta_{p,n+1}}
 -\frac{Q_p(w_n)}{\zeta_{p,n}}
 =O_p((\log n)^p n^{-2}).
\]

The difference of the two remainders in (3.4) is bounded by the sum of
their absolute bounds.  Consequently

\[
 b_{q,n+1}-b_{q,n}
 =\frac{Q_p(w_n)}n
 +O_p\!\left(\frac{(\log n)^{p+1}}{n^2}\right).
\tag{3.5}
\]

Since

\[
 w_n=\log(2\pi n)+\gamma+\frac{\pi i}{2}
 +O_p\!\left(\frac{\log n}{n}\right),
\]

equation (3.5) gives

\[
 \begin{aligned}
 \Re(b_{q,n+1}-b_{q,n})
 &=\frac{(\log(2\pi n))^p}{p!\,n}(1+o(1))>0,\\
 \Im(b_{q,n+1}-b_{q,n})
 &=\frac{\pi(\log(2\pi n))^{p-1}}
 {2(p-1)!\,n}(1+o(1))>0.
 \end{aligned}
\tag{3.6}
\]

The same formulas also give the individual-value asymptotics

\[
 \begin{aligned}
 \Re b_{q,n}
 &=\frac{(\log(2\pi n))^{p+1}}{(p+1)!}(1+o(1)),\\
 \Im b_{q,n}
 &=\frac{\pi(\log(2\pi n))^p}{2p!}(1+o(1))>0.
 \end{aligned}
\tag{3.7}
\]

In particular, \(|b_{q,n}|\to\infty\), and the lower critical values are
their conjugates.  We now separate all possible tail collisions.  For two
upper indices \(m>n\), summing the eventually positive real increments in
(3.6) gives \(\Re b_{q,m}>\Re b_{q,n}\).  Upper and lower tail values cannot
coincide because (3.7) puts them in opposite half-planes.  Finally, the
critical points not belonging to the two tails form a finite set, whereas
the tail values tend to infinity; after increasing the tail threshold, no
tail value equals a value coming from that finite set.  We have proved:

> **Corollary 3.2.**  For every fixed \(q\geq2\), all but finitely many
> critical points of \(F_q\) are simple, all but finitely many critical
> values arise from exactly one critical point, and distinct such tail
> critical points have distinct critical values.  The complete critical
> value set is closed and discrete.  Every critical value has only finitely
> many critical points above it.

Indeed, the critical points of \(F_q\) are precisely the nonzero zeros of
\(F_{q-1}\).  Lemma 3.1 leaves only finitely many of them outside the two
tails.  Thus the full critical-value set is a finite set together with two
sequences escaping to infinity, which proves closedness and discreteness.
For any fixed critical value, (3.7) permits only finitely many tail
preimages, and there are only finitely many exceptional critical points.

For completeness, the order \(q=1\) calculation used below is global.  The
critical points are

\[
 \operatorname{Crit}(F_1)=\{2\pi ik:k\in\mathbb Z\setminus\{0\}\},
\]

and they are simple because
\(F_1''(2\pi ik)=F_0'(2\pi ik)/(2\pi ik)=1/(2\pi ik)\ne0\).  For \(k>0\),

\[
 F_1(2\pi ik)=\operatorname{Cin}(2\pi k)
              +i\operatorname{Si}(2\pi k).
\tag{3.8}
\]

The function \(\operatorname{Cin}(x)=\int_0^x(1-\cos t)t^{-1}\,dt\) is
strictly increasing at the points \(2\pi k\).  Also
\(\operatorname{Si}(2\pi k)>0\): pair the positive half-wave
\([2j\pi,(2j+1)\pi]\) with the following negative half-wave and use the
strict decrease of \(1/t\).  Hence the upper values in (3.8) are pairwise
distinct and nonreal, and conjugation separates them from all lower values.
Finally (1.4)--(1.6) on the positive imaginary axis give
\(\operatorname{Cin}(2\pi k)=\log(2\pi k)+\gamma+O(k^{-1})\), so this critical-value set
is closed and discrete, and every value has exactly one critical point above
it.

For \(q=2\), in fact every critical point is simple: a common nonzero zero
of \(F_1\) and \(F_1'\) would have to be \(2\pi ik\), but
\(F_1(2\pi ik)=\operatorname{Cin}(2\pi k)+i\operatorname{Si}(2\pi k)\ne0\).
Global noncollision for \(F_2\) remains a finite, numerically verified but
unproved problem.  It is not required in Theorem A.

## 4. The finite-exception permutation lemma

> **Lemma 4.1.**  Let \(\Omega\) be countably infinite and let
> \(G\leq\operatorname{FSym}(\Omega)\) be transitive.  Suppose \(G\) is
> generated by a family of transpositions together with finitely many
> additional finitary permutations.  Then \(G=\operatorname{FSym}(\Omega)\).

Let \(H\) be the group generated by the transpositions and let its orbits be
the connected components of the associated edge graph.  On each component,
\(H\) contains the full finitary symmetric group.  If \(H\) is transitive,
then already \(H=\operatorname{FSym}(\Omega)\) and there is nothing to
prove.  Assume henceforth that it is not transitive.  Every \(H\)-orbit must
meet the finite union of the supports of the exceptional generators;
otherwise that proper orbit is \(G\)-invariant.  Thus there are finitely many
\(H\)-orbits, and at least one is infinite.

Start from an infinite orbit \(U\), on which \(G\) contains
\(\operatorname{FSym}(U)\).  If an exceptional generator \(g\) sends
\(a\in U\) to \(b\notin U\), choose \(x\in U\) outside the finite support
of \(g\).  Then

\[
 g(a\ x)g^{-1}=(b\ x)\in G.
\]

This cross-transposition adjoins the whole \(H\)-orbit of \(b\) to \(U\).
More explicitly, form a finite incidence graph whose vertices are the
\(H\)-orbits and in which two vertices are joined when some exceptional
generator sends a point of one to a point of the other.  This graph is
connected: a union of its connected components would otherwise give a
nontrivial \(G\)-invariant union of \(H\)-orbits, contrary to transitivity.
Following a spanning tree from the infinite orbit and repeating the above
cross-transposition construction therefore absorbs every orbit.  Hence every
finitary transposition belongs to \(G\), proving the lemma.

## 5. Proof of Theorem A

Let \(B_q\) be the critical-value set.  Corollary 3.2 (and the explicit
\(q=1\) calculation) makes \(B_q\) closed and discrete.  Set

\[
 X_q=\mathbb C\setminus F_q^{-1}(B_q),\qquad
 Y_q=\mathbb C\setminus B_q.
\]

The preimage \(F_q^{-1}(B_q)\) is closed and discrete.  Indeed, near a point
whose image is not in \(B_q\) this follows from closedness of \(B_q\); near
a point mapping to \(b\in B_q\), choose a target disk containing no other
point of \(B_q\), so locally the preimage is the discrete zero set of
\(F_q-b\).  The complement of a closed discrete subset of the plane is
path-connected (perturb a polygonal path around the finitely many points it
meets), hence \(X_q\) is path-connected.

Let \(\Delta=D(a,r)\) be a disk with \(\overline\Delta\subset Y_q\), and
let \(U\) be a component of \(F_q^{-1}(\Delta)\).  For
\(M>|a|+r\), the connected set \(U\) lies in one component of
\(\{|F_q|<M\}\); Lemma 2.1 therefore makes \(U\) bounded.  The restriction
\(F_q:U\to\Delta\) is proper.  To see this without any boundary
assumption, let \(K\Subset\Delta\) and take a sequence
\(z_j\in U\cap F_q^{-1}(K)\).  Boundedness gives a convergent subsequence
\(z_j\to z\).  Then \(F_q(z)\in K\subset\Delta\); since
\(F_q^{-1}(\Delta)\) is open, a small connected neighborhood of \(z\) lies
in the same component \(U\), so \(z\in U\).

The map on \(U\) is unramified.  A proper local biholomorphism has finite
fibers and is a covering onto its image; that image is nonempty, open, and
closed in \(\Delta\), hence is all of \(\Delta\).  Since \(U\) is connected
and \(\Delta\) is simply connected, this covering has one sheet.  We have
therefore proved that

\[
 F_q:X_q\longrightarrow Y_q
\]

is a connected covering and its monodromy is transitive.

The regular fiber is countably infinite.  Indeed, if \(F_q-c\) had only
finitely many zeros, the order-one Hadamard factorization theorem (the order
is immediate from the Taylor coefficients) would give

\[
 F_q(z)-c=P(z)e^{az+b}
\]

with a polynomial \(P\).  If \(a\ne0\), a ray on which
\(\Re(az)\to-\infty\) makes the right side tend to zero and gives the finite
asymptotic value \(c\), contrary to Lemma 2.1.  If \(a=0\), then \(F_q\)
would be a polynomial.  Thus every regular fiber is infinite; being a
discrete subset of \(\mathbb C\), it is countably infinite.

The finitary nature of a meridian requires the bounded-component conclusion
of Lemma 2.1, not merely finiteness of the critical fiber.  We record the
precise local statement.

> **Lemma 5.1 (finitary meridians).**  Let \(f\) be entire and suppose every
> component of the inverse image of every bounded disk is bounded.  Let
> \(b\) be an isolated critical value with only finitely many critical
> points above it.  Then a meridian around \(b\) has finite support on a
> regular fiber.  If exactly one critical point lies above \(b\) and it is
> simple, the meridian is a single transposition.

Choose a disk \(\Delta_b\) whose closure contains no critical value of
\(f\) other than \(b\).  The compactness argument above,
which did not use absence of critical points, shows that the restriction of
\(f\) to every component \(U\) of \(f^{-1}(\Delta_b)\) is a proper finite
branched cover onto \(\Delta_b\).  If \(U\) contains no critical point, the
map is a connected unramified cover of a disk, hence has degree one, and its
sheet is fixed by the meridian.  Every critical point in such a component
maps to \(b\); hence only finitely many components contain critical points.
Each of those components has finite degree, so the meridian is supported on
the finite union of their finite fibers.  Its nontrivial cycles are exactly
the local ramification cycles.  A unique simple critical point therefore
gives one transposition.  Transporting the local meridian to the chosen base
point only conjugates this permutation and preserves its finite support and
cycle type.  This proves the lemma.

Lemma 5.1 applies to \(F_q\) by Lemma 2.1 and Corollary 3.2 (or (3.8) when
\(q=1\)).  Thus every meridian is finitary and all but finitely many
meridians are single transpositions.  Finally, every loop in \(Y_q\) is a
finite word in meridians: its compact image lies in a sufficiently large
disk whose boundary avoids \(B_q\), and that disk contains only finitely
many points of the closed discrete set \(B_q\).  It follows that the entire
monodromy group lies in \(\operatorname{FSym}\) and is generated by the
tail transpositions together with finitely many exceptional finitary
permutations.  It is transitive and acts on a countably infinite fiber, so
Lemma 4.1 gives (0.2).

## 6. Algebraic freedom of branches and first jets

> **Theorem B (all branches are ordinarily algebraically free).**  On an
> evenly covered simply connected disk, every finite family of distinct
> inverse branches of \(F_q\) is algebraically independent over
> \(\mathbb C(c)\).

Suppose a relation exists and clear its coefficients' denominators to obtain
a nonzero polynomial

\[
 P(c;X_1,\ldots,X_n)\in\mathbb C[c,X_1,\ldots,X_n]
\]

which vanishes on the given branches.  Choose \(c_*\) in the original disk
so that \(P(c_*;\mathbf X)\) is not the zero polynomial; only finitely many
values are excluded by its nonzero coefficient polynomials.  Clearing the
denominators has removed all coefficient poles; equivalently, meridian
representatives could be perturbed away from their finite pole set.  Analytic
continuation of the identity around loops based at \(c_*\), together with
the \(n\)-transitivity of \(\operatorname{FSym}\), makes
\(P(c_*;\mathbf X)\) vanish on every ordered distinct \(n\)-tuple in the
infinite fiber.  Those tuples are Zariski dense in \(\mathbb C^n\): fix all
but one coordinate, omit the finitely many previously used fiber points, and
induct.  This contradicts the choice of \(c_*\) and proves Theorem B.

There is a sharper jet statement.

> **Theorem C (all-order first-jet freedom).**  For every fixed \(q\geq1\),
> distinct inverse branches \(\rho_1,\ldots,\rho_n\) satisfy
> \[
>  \{\rho_i,\rho_i':1\leq i\leq n\}
>  \quad\text{algebraically independent over }\mathbb C(c).
> \tag{6.1}
> \]

Fix an arbitrary regular value \(c_*\).  We first write out the fiber version of the
contraction, rather than appeal to it implicitly.  On the rough disk
\(E_{q,n}\) from (3.2a), \(Q_q(w)-c_*\ne0\) for large \(n\), and we choose
the logarithm asymptotic to \(q\Log w-\log(q!)\).  The equation
\(F_q(z)=c_*\) is equivalent to

\[
 z=T^{c_*}_{q,n}(z):=2\pi in+i\pi q-q\Log z
 -\log(Q_q(\Log z+\gamma)-c_*)+\log\mathcal B_q(z).
\tag{6.2}
\]

Define \(c^{c_*}_{q,n}=T^{c_*}_{q,n}(2\pi in)\) and

\[
 D^{c_*}_{q,n}=\{z:|z-c^{c_*}_{q,n}|\leq1\}.
\]

The same direct expansion used in (3.2e), now with a fixed lower-order term
\(-c_*\), gives
\(|c^{c_*}_{q,n}-2\pi in|=O_{q,c_*}(\log n)\); hence this disk lies in
\(E_{q,n}\).  Moreover,

\[
 (T^{c_*}_{q,n})'(z)
 =-\frac qz-
 \frac{Q_{q-1}(w)}{z(Q_q(w)-c_*)}
 +\frac{\mathcal B_q'(z)}{\mathcal B_q(z)}
 =O_{q,c_*}(n^{-1}).
\tag{6.3}
\]

Thus, for all sufficiently large \(n\),
\[
 |T^{c_*}_{q,n}(z)-c^{c_*}_{q,n}|
 \leq \frac{C_{q,c_*}}n|z-2\pi in|
 \leq \frac{C_{q,c_*}(1+\log n)}n<1
 \qquad(z\in D^{c_*}_{q,n}),
\]

and \(\sup_{D^{c_*}_{q,n}}|(T^{c_*}_{q,n})'|<1/2\).  Thus
\(T^{c_*}_{q,n}(D^{c_*}_{q,n})\subset D^{c_*}_{q,n}\).
Exponentiating (6.2) identifies its unique
fixed point \(z_n(c_*)\) with a point of \(F_q^{-1}(c_*)\).  This supplies
an infinite sequence \(|z_n(c_*)|\to\infty\), since the consecutive centers
again differ by \(2\pi i+o(1)\).

At such a point \(R_q=c_*-Q_q\).  Consecutive-remainder division, including
\(q=1\) by (1.7), gives

\[
 \frac{R_{q-1}}{R_q}
 =-z\left(1+\frac qz+O_q(z^{-2})\right),
\]

and hence

\[
 F_{q-1}(z)=Q_{q-1}(w)
 +z(Q_q(w)-c_*)\left(1+\frac qz+O_q(z^{-2})\right).
\tag{6.4}
\]

Using (0.1) and
\(Q_{q-1}(w)/(z(Q_q(w)-c_*))=O_{q,c_*}((z\Log z)^{-1})\), we obtain

\[
 p(z):=\frac1{F_q'(z)}
 =\frac1{Q_q(\Log z+\gamma)-c_*}
  \left(1+O_{q,c_*}(z^{-1})\right)
 \sim\frac{q!}{(\Log z)^q}.
\tag{6.5}
\]

The jet set

\[
 J_{q,c_*}=\{(z,p(z)):F_q(z)=c_*\}
\]

is Zariski dense in \(\mathbb C^2\).  Indeed, for a nonzero polynomial
\(A(z,p)\), choose its largest \(z\)-degree \(d\), and within that degree
choose the smallest occurring \(p\)-degree \(j\).  Along the sequence above,
the term \(a_{d,j}z^dp^j\) dominates terms of the same \(z\)-degree and
larger \(p\)-degree because \(p\to0\).  If \(N\) is the largest difference
of \(p\)-degrees that occurs, it dominates every lower \(z\)-degree term
because

\[
 |z|^{-1}|p|^{-N}=O((\log|z|)^{qN}/|z|)\longrightarrow0.
\]

Thus \(A\) cannot vanish on all of \(J_{q,c_*}\).

We use the following elementary product fact.  If an infinite subset
\(S\subset\mathbb C^2\) is Zariski dense, then \(S\) with finitely many
points removed is still Zariski dense: otherwise the irreducible variety
\(\mathbb C^2\) would be the union of a proper closed set and finitely many
points.  It follows by induction that

\[
 S^{[n]}=\{(s_1,\ldots,s_n)\in S^n:s_i\ne s_j\ (i\ne j)\}
\]

is Zariski dense in \((\mathbb C^2)^n\).  Indeed, after fixing
\(s_1,\ldots,s_{n-1}\), a polynomial vanishing on \(S^{[n]}\) vanishes as a
polynomial in its last pair of variables on
\(S\setminus\{s_1,\ldots,s_{n-1}\}\); its coefficients then vanish on the
ordered distinct \((n-1)\)-fold product.

Since the construction and density proof apply to every regular \(c_*\), we
may now specialize a hypothetical relation at a convenient value.  Suppose
that the \(2n\) first-jet functions satisfy an algebraic
relation.  Clearing denominators gives a nonzero

\[
 P(c;Z_1,W_1,\ldots,Z_n,W_n)\in
 \mathbb C[c,Z_1,W_1,\ldots,Z_n,W_n].
\]

Choose \(c_*\) in the original regular disk so that its specialization in
the jet variables is nonzero.  Clearing denominators removes coefficient
poles (or, equivalently, the finitely many poles can be avoided by the loop
representatives).  Under continuation around a loop, a sheet
\(z\) and its derivative move together as
\((z,1/F_q'(z))\).  The \(n\)-transitivity from Theorem A therefore makes
the specialized polynomial vanish on the ordered distinct \(n\)-fold
product of \(J_{q,c_*}\), which is Zariski dense by the preceding paragraph.
This contradicts nonzero specialization and proves (6.1).

## 7. Ordinary freedom versus differential algebra

If \(\rho(c)\) is an inverse branch and

\[
 \mathcal L_\rho=\frac{\rho}{\rho'}\frac d{dc},
\]

then (0.1) gives

\[
 H_q:=\mathcal L_\rho^q(c)=1-e^{-\rho},\qquad
 H_q'=\rho'(1-H_q).
\tag{7.1}
\]

After clearing powers of \(\rho'\), (7.1) is a differential-polynomial
equation of order at most \(q+1\).  Hence every inverse branch is
differential-algebraic, while Theorems B--C show extreme ordinary algebraic
freedom.

For \(q=1\), (7.1) is exactly

\[
 \rho\rho''+(\rho')^3-(\rho+1)(\rho')^2=0.
\tag{7.2}
\]

Theorem C shows that no order-zero or order-one differential equation can
hold, so the differential order is exactly two.  Differentiating (7.2)
expresses every higher derivative rationally in \(\rho,\rho'\).  Therefore,
for any \(n\) distinct branches,

\[
 \operatorname{trdeg}_{\mathbb C(c)}
 \mathbb C(c)\langle\rho_1,\ldots,\rho_n\rangle=2n,
 \qquad
 \operatorname{dtrdeg}_{\mathbb C(c)}=0.
\tag{7.3}
\]

This is the sharpest ordinary/differential separation presently available.

## 8. Coupling to exact two-trace recovery

For a nonzero level \(c\), and the zero divisor of \(F_q(z)-c\), let

\[
 T_m^{(q)}(c)=\sum_{F_q(\rho)=c}\rho^{-m},\qquad m\geq2.
\]

The series is absolutely convergent because \(F_q-c\) has order one.  We
recall the trace calculation, with the same normalization as the companion
note [*Uniform monodromy of polyexponential trace
polynomials*](TRACE_MONODROMY_ALL_Q.md).  Hadamard factorization gives

\[
 F_q(z)-c=-c\,e^{\alpha z}
 \prod_{F_q(\rho)=c}\left(1-\frac z\rho\right)e^{z/\rho},
\]

with zeros repeated according to multiplicity.  Comparing the coefficient
of \(z^m\), \(m\geq2\), in the logarithm at \(z=0\) gives

\[
 T_m^{(q)}(c)=P_{q,m}(c^{-1}),\qquad
 P_{q,m}(X):=-m[z^m]\log(1-XF_q(z)).
\tag{8.0}
\]

Indeed,

\[
 P_{q,m}(X)=\sum_{k=1}^m\frac{m}{k}[z^m]F_q(z)^kX^k,
\]

so \(P_{q,m}\in\mathbb Q[X]\) is monic of degree \(m\).  Writing
\(X=c^{-1}\) and using the first four Taylor coefficients of \(F_q\) gives

\[
 \begin{aligned}
 T_2^{(q)}&=X^2-\frac{X}{2^q},\\
 T_4^{(q)}&=X^4-\frac{2X^3}{2^q}
 +\left(\frac2{3^{q+1}}+\frac1{2^{2q+1}}\right)X^2
 -\frac{X}{6\cdot4^q}.
 \end{aligned}
\tag{8.0a}
\]

In particular, if

\[
 A_q=\frac2{3^{q+1}}-\frac1{2^{2q+1}},
\]

and

\[
 C_q=-\frac1{6\cdot4^q}+\frac2{3\cdot6^q}
     -\frac1{2^{3q+1}}\ne0,
\]

(vanishing would give \(4^{q+1}=6^q+3^{q+1}\), impossible modulo \(3\)),

then (8.0a) gives

\[
 T_4^{(q)}-(T_2^{(q)})^2-A_qT_2^{(q)}=C_qX,
\]

and hence

\[
 c^{-1}=\frac{T_4^{(q)}-(T_2^{(q)})^2-A_qT_2^{(q)}}{C_q}.
\tag{8.1}
\]

Consequently

\[
 \mathbb C(c)=\mathbb C(T_2^{(q)},T_4^{(q)}).
\tag{8.2}
\]

Combining (8.2) with Theorems A--C produces the all-order
**local-freedom/global-collapse dichotomy**:

* every finite collection of local inverse branches, and even their first
  jets, is algebraically free;
* the monodromy of all local sheets is the maximal finitary symmetric group;
* nevertheless, all global reciprocal Newton traces of the infinite divisor
  are functions of two traces, and those two traces recover the level exactly.

This synthesis is substantially stronger than either the monodromy theorem or
the trace calculation in isolation.

## 9. Literature and novelty boundary

* NIST Digital Library of Mathematical Functions, \S8.11(i), equations
  8.11.2--8.11.3 (with the parameter restricted to a compact set), supplies
  the large-variable incomplete-gamma remainder used in (1.5a).  The
  contour-remainder proof gives compact-parameter uniformity, and Cauchy's
  estimates give (1.5b)--(1.5c).
* G. H. Hardy, *On the Zeroes of Certain Classes of Integral Taylor
  Series, Part II*, Proc. London Math. Soc. (2) **2** (1905), 401--431,
  DOI: `10.1112/plms/s2-2.1.401`, studied the zeros and asymptotics of
  \(e(x,a\mid s)\).  Since \(F_p(z)=z e(-z,1\mid p+1)\), the leading
  zero-box asymptotic must be credited to this line.
* K. N. Boyadzhiev, *Polyexponentials*, arXiv:0710.1332, surveys the
  defining identities and Hardy asymptotics.
* L. Zelenko, *Generic monodromy group of Riemann surfaces for inverses to
  entire functions of finite order*, arXiv:2105.14015, proves
  \(\operatorname{FSym}(\mathbb N)\) for a generic/``typical'' class with
  globally simple critical points and globally pairwise-distinct critical
  values.

Thus \(\operatorname{FSym}\) as an abstract phenomenon is not new.  The
potentially new content here is the **explicit all-order polyexponential
theorem**, the proof that only finitely many exceptional critical events can
occur, the finite-exception permutation upgrade (which avoids proving global
critical-value noncollision), and the all-order branch/first-jet algebraic
freedom.  A full submission still requires a systematic MathSciNet/zbMATH
priority search.

## 10. What remains open

1. Prove or disprove global pairwise noncollision of the critical values of
   \(F_q\), already open in the finite remainder for \(q=2\).
2. Determine whether the inverse differential equation in (7.1) has minimal
   order \(q+1\) for every \(q\geq2\).  Theorem C gives only the lower bound
   two.
3. Determine algebraic independence of higher inverse jets and the exact
   ordinary transcendence degree of the differential field generated by
   finitely many branches for \(q\geq2\).
4. Determine whether the local-freedom/global-collapse dichotomy has an
   analogue for other iterated-integral towers beyond the polyexponentials.

# 001 × Moving-Level Trace Towers: 추가 폐쇄·초월성 연구 노트

**판정일:** 2026-08-31  
**대상:** `[001] Exponential-Integral Periods ...`와 barriers 연구가 통합된 `KEIO Moving-Level Trace Towers v2.3`  
**기본체:**
\[
K=\overline{\mathbf Q}(e^\alpha:\alpha\in\overline{\mathbf Q}).
\]

## 0. 결론

두 원고를 결합하면 기존에 적혀 있지 않던 **무조건적 정리**가 실제로 여러 개 닫힌다. 가장 강한 세 결과는 다음이다.

1. 대수점에서의 signed polyexponential level
   \(a\Ein_q(\alpha)\)에 대한 \(\Ein\)-역상의 **대수점 완전분류**.
2. Gamma Laurent coefficient와 tail integral의 차를 level로 잡은 모든 \(\Ein\)-divisor에서 **모든 영점의 초월성**, 그리고 transversal inverse traces의 **공동 대수적 독립성**.
3. 모든 고정 양의 정수 \(r\)에 대해 lower incomplete Gamma의 매개변수 미분값
   \(\partial_s^k\Gamma_{<}(s,1)|_{s=r}\;(k\ge1)\)의 **가산 공동 대수적 독립성**.

추가로 order-axis Stieltjes–Hankel tower, 명시적인 spectral–classical 초월수, \(\gamma,\delta\)를 첨가한 뒤에도 결함이 최대 1이라는 상대 정리, trace relation ideal의 완전분류가 나온다.

반면 **현재 알려진 유명 고난도 추측을 통째로 해결한 것은 없다.** 특히 \(\gamma\), \(\delta\), 고정 \(p\)의 Euler factorial value의 무리성·초월성은 여전히 열려 있다. 이 구분은 논문에서 반드시 지켜야 한다.

## 1. 사용한 두 입력

### 입력 A — 001의 resonant polyexponential 독립성

\[
\Ein_q(z)=\sum_{n\ge1}\frac{(-1)^{n-1}z^n}{n^q n!}\qquad(q\ge1).
\]

001의 Theorem 1.4 / Theorem 8.3 / Corollary 8.4에 의해

\[
\bigl\{\Ein_q(\alpha):q\ge1,
\ \alpha\in\overline{\mathbf Q}^{\times}\bigr\}
\]

은 \(K\) 위에서 가산 공동 대수적 독립이다.

또 001 Corollary 8.8에서

\[
\Gamma(s)=\frac1s+\sum_{k\ge0}g_ks^k,
\qquad
T_k=\frac1{k!}\int_1^\infty e^{-u}(\log u)^k\frac{du}{u}
\]

라 하면

\[
c_k:=g_k-T_k=(-1)^{k+1}\Ein_{k+1}(1).
\]

### 입력 B — v2.3의 universal trace와 exact recovery

\(Z_c\)를 \(\Ein(z)-c\)의 영점 다중집합이라 하고 \(m\ge2\)일 때

\[
T_m(c):=\sum_{\rho\in Z_c}\rho^{-m}=P_m(c^{-1}),
\]

여기서 \(P_m\in\mathbf Q[X]\)는 차수 \(m\)의 monic polynomial이다. 특히

\[
c^{-1}=144T_4(c)-144T_2(c)^2-14T_2(c).
\]

따라서 한 level의 전체 trace ring은 이미 \(T_2,T_4\)로 생성되고,

\[
F[T_m(c):m\ge2]=F[T_2(c),T_4(c)]=F[c^{-1}].
\]

서로 대수적으로 독립인 level들에서 각각 trace 하나씩을 고르면 그 trace들도 공동 대수적 독립이다.

---

## 2. 새 정리 A — signed polyexponential 역상의 대수점 완전분류

### 정리 A

\(\alpha,\beta\in\overline{\mathbf Q}^{\times}\), \(q\ge1\),
\(a\in\overline{\mathbf Q}^{\times}\)라 하자. 그러면

\[
\boxed{
\Ein(\beta)=a\Ein_q(\alpha)
\iff
(q,\beta,a)=(1,\alpha,1).
}
\]

즉 자명한 동일좌표 경우를 제외하면 대수점끼리의 signed level collision은 전혀 없다.

### 증명

- \((q,\alpha)\ne(1,\beta)\)이면 서로 다른 두 resonant coordinate 사이의 비자명한 선형관계이므로 001의 공동 대수적 독립성과 모순이다.
- 같은 좌표이면 \((1-a)\Ein(\alpha)=0\)이다. \(\Ein(\alpha)\)는 \(K\) 위 초월적이므로 0이 아니고, 따라서 \(a=1\)이다.

### 역함수 초월성 귀결

\[
\Ein(z)=a\Ein_q(\alpha)
\]

의 모든 해는 위 한 예외를 제외하고 초월수이다. 특히 \(\alpha>0\)가 대수적이고 \(q\ge2\)이면 \(\Ein\)의 양의 실축 단조성으로

\[
x_{q,\alpha}:=\Ein^{-1}(\Ein_q(\alpha))>0
\]

가 유일하게 존재하며

\[
\boxed{x_{q,\alpha}\text{ 는 초월수이다}.}
\]

가장 작은 구체 예는

\[
\Ein(x)=\Ein_2(1),\qquad
x=1.154513907278168499650593428772329944\ldots,
\]

이고 이 수는 초월수이다.

**평가:** 완결도 A, 신규성 후보 A−. 기존의 일반 E-function common-zero 문제를 해결한 것이 아니라, 001의 매우 강한 값 독립성에서 나오는 이 특정 family의 완전분류다.

---

## 3. 새 정리 B — Gamma-jet spectral divisor의 모든 영점은 초월적

앞의

\[
c_k=g_k-T_k=(-1)^{k+1}\Ein_{k+1}(1)
\]

를 level로 잡고

\[
Z_k:=\{\rho\in\mathbf C:\Ein(\rho)=c_k\}
\]

라 하자.

### 정리 B

1. 모든 \(k\ge0\)와 모든 \(\rho\in Z_k\)에 대해 \(\rho\)는 초월수이다.
2. 모든 \(m\ge2\)에 대해
   \[
   \tau_{m,k}:=\sum_{\rho\in Z_k}\rho^{-m}
   =P_m(c_k^{-1})
   \]
   는 \(K\) 위 초월적이다.
3. 각 \(k\)마다 임의로 \(m_k\ge2\)를 하나 고르면
   \[
   \boxed{\{\tau_{m_k,k}:k\ge0\}\text{ 는 }K\text{ 위 공동 대수적 독립이다}.}
   \]

### 증명

- \(k=0\)에서는 level이 \(-\Ein(1)\)이므로 정리 A의 유일한 예외가 아니다.
- \(k\ge1\)에서는 order가 \(q=k+1\ge2\)이므로 정리 A가 모든 대수적 영점을 배제한다.
- \(c_k\)들은 001에 의해 공동 대수적 독립이다. 만약 \(P_m(c_k^{-1})\)가 \(K\) 위 대수적이면 \(c_k^{-1}\)는 \(P_m(X)-P_m(c_k^{-1})\)의 근이 되어 \(K\) 위 대수적이어야 하므로 모순이다.
- 마지막 공동 독립성은 v2.3의 transversal trace theorem을 적용하면 된다.

이 결과는 “Gamma jet의 명시적 조합 → entire divisor → 영점 전부 초월적 → inverse spectrum 공동 독립”을 한 번에 연결한다.

**평가:** 완결도 A, 논문 임팩트 A. 두 원고의 결합을 가장 잘 보여 주는 새 주정리 후보이다.

---

## 4. 새 정리 C — 양의 정수점 lower incomplete-Gamma 미분의 전차수 공동 독립

\[
\Gamma_{<}(s,1)=\int_0^1e^{-t}t^{s-1}\,dt
\]

이고, 고정된 \(r\in\mathbf Z_{\ge1}\)에 대해

\[
D_{r,k}:=\left.\frac{\partial^k}{\partial s^k}
\Gamma_{<}(s,1)\right|_{s=r}
=\int_0^1e^{-t}t^{r-1}(\log t)^k\,dt.
\]

### 정리 C

모든 고정 \(r\ge1\)에 대해

\[
\boxed{\{D_{r,k}:k\ge1\}\text{ 는 }K\text{ 위 가산 공동 대수적 독립이다}.}
\]

따라서 모든 \(D_{r,k}\;(k\ge1)\)는 각각 초월수이다.

특히 \(r=1\)에서는

\[
\boxed{D_{1,k}=(-1)^k k!\Ein_k(1)\qquad(k\ge1).}
\]

### 증명

\[
R(u):=u^{-1}-\Gamma_{<}(u,1)
=\sum_{j\ge0}R_ju^j,qquad
R_j=(-1)^j\Ein_{j+1}(1).
\]

lower incomplete Gamma의 recurrence

\[
\Gamma_{<}(s+1,1)=s\Gamma_{<}(s,1)-e^{-1}
\]

를 \(r\)번 전개하면 어떤 \(Q_r\in\mathbf Z[u]\)에 대해

\[
\Gamma_{<}(u+r,1)
=\frac{(u)_r}{u}-(u)_rR(u)-e^{-1}Q_r(u),
\]

여기서 \((u)_r=u(u+1)\cdots(u+r-1)\)이다. \(u^k\;(k\ge1)\)의 계수를 비교하면

\[
\frac{D_{r,k}}{k!}
=-(r-1)!R_{k-1}
+\text{a }K\text{-affine expression in }R_0,\ldots,R_{k-2}.
\]

이는 대각항 \(-(r-1)!\ne0\)인 affine lower-triangular 변환이다. 001에 의해 \(R_0,R_1,\ldots\)가 공동 대수적 독립이므로 \(D_{r,1},D_{r,2},\ldots\)도 공동 대수적 독립이다.

**주의:** 서로 다른 여러 \(r\)의 family를 합친 전체 family는 recurrence 때문에 독립이라고 주장하면 안 된다. 정리는 **각 고정 \(r\)**에 대한 것이다.

**평가:** 완결도 A, 외부 분야 확장성 A. 기존 v2.3의 \(s=0\) regularized Laurent jet을 모든 양의 정수 parameter point로 수송한다.

---

## 5. 새 정리 D — order-axis Stieltjes–Hankel–Gamma tower

양의 대수적 \(\alpha\)와 \(k\ge0\)에 대해

\[
\mu_{\alpha,k}:=k!\Ein_{k+1}(\alpha).
\]

Mellin 적분으로

\[
\boxed{
\mu_{\alpha,k}
=\int_0^1\frac{1-e^{-\alpha t}}{t}(-\log t)^k\,dt
=\int_0^\infty y^k(1-e^{-\alpha e^{-y}})\,dy.
}
\]

따라서 \((\mu_{\alpha,k})_{k\ge0}\)는 양의 밀도
\(1-e^{-\alpha e^{-y}}\)를 갖는 엄격한 Stieltjes moment sequence이다.

\[
H_{\alpha,d}:=det(\mu_{\alpha,i+j})_{0\le i,j<d},
\qquad d\ge1.
\]

### 정리 D

\[
\boxed{
\{H_{\alpha,d}:\alpha\in\overline{\mathbf Q}_{>0},\ d\ge1\}
\text{ 는 }K\text{ 위 공동 대수적 독립이다}.
}
\]

또한 모든 \(H_{\alpha,d}>0\). 특히 각 determinant는 초월적이며 0이 아니다.

\(\alpha=1\)에서는

\[
H_{1,d}
=\det\!\bigl((i+j)!R_{1,i+j}\bigr)_{0\le i,j<d}>0,
\]

즉 lower incomplete-Gamma Laurent jet이 factorial gauge 뒤 실제 양의 Hankel tower를 이룬다.

각 \((\alpha,d)\)마다 \(m_{\alpha,d}\ge2\)를 하나 고르면

\[
\{T_{m_{\alpha,d}}(H_{\alpha,d})\}_{\alpha,d}
\]

도 \(K\) 위 공동 대수적 독립이다.

### 증명 핵심

001에 의해 모든 \(\mu_{\alpha,k}\)가 공동 대수적 독립이다. 한 \(\alpha\)에서

\[
\frac{\partial H_{\alpha,d}}
{\partial\mu_{\alpha,2d-2}}=H_{\alpha,d-1}
\]

이므로 증가하는 \(d\)에 대한 Jacobian은 삼각형이고 대각항이 비영 다항식이다. 서로 다른 \(\alpha\)-block은 변수도 분리된다. 양성은 양의 측도의 Gram determinant 표현에서 나온다. 마지막 trace 주장은 v2.3의 transversal trace theorem이다.

**평가:** 완결도 A, 구조적 가치 A−. 001의 argument-direction finite-difference Hankel tower와 다른 **order-direction** tower다. 정확한 역사적 우선권은 “apparently new corollary”가 안전하다.

---

## 6. 새 정리 E — 실제로 쓸 수 있는 명시적 spectral–classical 초월수

Euler-level inverse trace를

\[
S_m:=T_m(\gamma)=P_m(\gamma^{-1})\qquad(m\ge2)
\]

라 하고

\[
X\in\{\delta,E_1(1),\Ei(1),\Ci(1),\Chi(1)\}
\]

를 택한다.

### 정리 E

모든 비실수 대수적 수 \(a\in\overline{\mathbf Q}\setminus\mathbf R\)에 대해

\[
\boxed{S_m+aX\text{ 는 }K\text{ 위 초월적이다}.}
\]

더 나아가

\[
\boxed{e\text{ 와 }S_m+aX\text{ 는 }\mathbf Q\text{ 위 대수적으로 독립이다}.}
\]

### 증명

\(K\)는 복소켤레에 안정하고 \(S_m,X\)는 실수이다. 만약
\(S_m+aX\)가 \(K\) 위 대수적이면 그 켤레도 그러므로

\[
X=\frac{(S_m+aX)-(S_m+\bar aX)}{a-\bar a}
\]

가 \(K\) 위 대수적이고, 따라서 \(S_m\)도 \(K\) 위 대수적이다. v2.3의 trace arithmetic에 의해 \(\gamma\)도 \(K\) 위 대수적이다. 그러나 v2.3의 five relative certificate theorem은 \(\gamma\)의 class와 \(X\)의 class가 동시에 대수적일 수 없다고 한다. 모순이다.

예를 들어

\[
\boxed{
S_2+i\delta
=2.135171980840\ldots+0.596347362323\ldots i
}
\]

는 \(K\) 위 초월수이고, \(e\)와 공동 대수적으로 독립이다.

**평가:** 완결도 A. \(\gamma\)나 \(\delta\) 개별 문제를 풀지 않고도 얻는 무조건적이고 명시적인 초월수 family다.

---

## 7. 상대적으로 더 강해지는 정리 — \(\gamma,\delta\)를 둘 다 붙여도 결함은 최대 1

\[
F=K(\gamma,\delta),\qquad
d=\operatorname{trdeg}_K F\in\{1,2\}.
\]

\(Y_{\alpha,q}=\Ein_q(\alpha)\)라 하고 anchor \((\alpha,q)=(1,1)\)은 제외한다. 모든 유한집합 \(S\)에 대해

\[
\boxed{
\operatorname{trdeg}_F F(Y_{\alpha,q}:(\alpha,q)\in S)
\ge |S|+1-d.
}
\]

따라서 \(F\) 위에서 전체 resonant family의 예외는 많아야 하나이다.

- \(d=1\)이면 anchor 이외의 전 family가 \(F\) 위 공동 대수적 독립이다.
- 어떤 한 나머지 coordinate가 \(F\) 위 대수적이면 반드시 \(d=2\), 즉 \(\gamma,\delta\)가 \(K\) 위 공동 대수적 독립이고, 그 coordinate를 제외한 나머지는 전부 \(F\) 위 공동 대수적 독립이다.

증명은

\[
|S|+1
=\operatorname{trdeg}_K K(Y_{1,1},Y_S)
\le d+\operatorname{trdeg}_F F(Y_S)
\]

한 줄이다. 여기서 \(Y_{1,1}=\gamma+\delta/e\in F\)이다.

이 정리는 \(R_{1,k}=(-1)^k\Ein_{k+1}(1)\;(k\ge1)\)와 그 transversal trace tower에도 그대로 적용된다.

**한계:** 이것은 \(d=1\)인지 \(2\)인지 결정하지 않으며, \(\gamma\) 또는 \(\delta\) 개별의 무리성·초월성을 증명하지 않는다.

---

## 8. barriers와 결합해 완전히 정리되는 구조적 문제

### 8.1 유한 trace tuple의 complete relation ideal

유한한 trace-order 집합 \(M\subset\{2,3,\ldots\}\)가 \(2,4\)를 포함하고, level index가 \(1\le i\le n\)일 때

\[
R_i=144X_{i,4}-144X_{i,2}^2-14X_{i,2}
\]

로 두면 complete relation ideal은

\[
I_M=left\langle
X_{i,2}-P_2(R_i),\quad
X_{i,m}-P_m(R_i):m\in M\setminus\{2,4\}
\right\rangle.
\]

그리고

\[
\mathbf F[X_{i,m}]/I_M\cong\mathbf F[Z_1,ldots,Z_n].
\]

따라서 이 ideal은 prime complete intersection이고 trace variety는 매끈한 \(\mathbf A^n\), normal, UFD이다. 001의 독립 level을 쓰면 서로 다른 level 사이의 hidden relation은 없다.

### 8.2 최소 두 moment의 inverse spectral rigidity

\((T_2,T_4)\)는 level \(c\), 따라서 전체 divisor \(Z_c\)를 정확히 결정한다. 한 trace \(T_m\)만으로는 일반적으로 \(m\)-to-1이므로 두 moment가 필요하다. 최대 order 4는 이 family에서 최적이다. \((T_2,T_3)\)에는 정확히

\[
\{6-2\sqrt3,6+2\sqrt3\}
\]

라는 유일한 충돌쌍이 있다.

### 8.3 spectral algebraic-matroid universality

v2.3 Appendix의 linear realization과 positive carrier를 결합하면 모든 유한 characteristic-zero algebraic matroid를 한 positive trace-class operator의 독립 eigenvalue들의 선형형으로 실현할 수 있다. 다시 order-2 trace로 보내도 모든 부분집합의 transcendence rank가 보존된다.

### 8.4 전 trace-order non-holonomy

고정 \(m\ge2\)에서 moving traces \((\tau_{m,N})\), 그 signed increments, 두 ordinary generating function은 모두 P-recursive / D-finite가 아니다. 단, increment positivity는 현재 \(m=2,4\)에서만 주장해야 한다.

또

\[
\mathcal R(u)=u^{-1}-\Gamma_{<}(u,1)
\]

은 \(-1,-2,\ldots\)에 무한히 많은 pole을 가지므로 \(\mathbf C(u)\) 위 D-finite가 아니다. 이는 그 계수의 대수적 독립성과 별개의 강한 analytic obstruction이다.

---

## 9. 유명 난제 감사: 어디까지 닿고, 어디서 멈추는가

| 문제 | 이번 결합의 실제 성과 | 판정 |
|---|---|---|
| Jossen의 E-function quotient/common-zero 추측 | signed \(\Ein_q\) family의 **대수적 입력** branch를 완전분류 | hard case는 초월적 common root라서 미해결 |
| Murty–Sumner / Schikhof의 고정-\(p\) Euler factorial 무리성 | \(p=13\)의 일부 unit residue disc에서 full convergence | 무리성은 미해결 |
| Kurepa left-factorial 추측 | \(p=13\) all-index denominator-unit lemma, \(Q_{p-1}(-1)\equiv !p\pmod p\) 접점 | 전 소수 명제는 미해결 |
| \(\gamma\), \(\delta\) 무리성·초월성 | exact trace equivalence, 상대 class exclusion, 새 complex transcendental combinations | 개별 문제는 미해결 |

Jossen 추측의 일반적인 대수적 common-root 경우는 이미 알려져 있고 진짜 난점은 초월적 common root이다. 따라서 정리 A를 “Jossen 해결”로 쓰면 안 된다. 관련 최신 1차 논문은 [Fischler–Rivoal, *On the values of E-functions*](https://arxiv.org/html/2503.20345v1)이다.

고정 \(p\)에서 \(E_p(\pm1)\)의 무리성은 여전히 열려 있다. [Ernvall-Hytönen–Matala-aho–Seppälä](https://arxiv.org/html/2111.13649v2)가 이 상태와 unit-boundary convergence의 어려움을 명시한다.

Kurepa 추측의 최신 계산 검증 범위는 \(p<2^{40}\)이다. [Andrejić–Bostan–Tatarević](https://arxiv.org/html/1904.09196v3). 따라서 \(2^{34}\)라고 쓰면 오래된 기록이다.

lower incomplete-Gamma의 special values에는 기존 연구가 있으므로 정리 C·D는 “apparently new consequence in the parameter-derivative/order-axis regime”로 쓰는 것이 안전하다. 비교 문헌: [Murty–Saha, *Transcendental values of the incomplete gamma function*](https://doi.org/10.1007/s00013-015-0800-3), [Boyadzhiev, *Polyexponentials*](https://arxiv.org/abs/0710.1332).

---

## 10. \(p\)-adic 쪽에서 닫히는 정확한 국소 결과와 장벽

\[
Q_n(t)=\sum_{h=0}^n h!\binom nh^2(-t)^h.
\]

\(p=13\)에서 \(t\bmod13\in\{6,9,11,12\}\)이면 모든 denominator가 unit이고 모든 Padé/continued-fraction convergent가 \(E_{13}(t)\)로 수렴한다. 특히 \(t=-1\)에서

\[
v_{13}\!\left(E_{13}(-1)-\frac{P_n(-1)}{Q_n(-1)}\right)
\ge2v_{13}(n!)=\frac{n-s_{13}(n)}6.
\]

이는 “apparently new explicit full-convergence case on the \(p\)-adic unit boundary”로는 가치가 있다. 그러나

\[
\log H_n=n\log n-n+2\sqrt n+O(\log n)
\]

인 데 비해 고정 \(p\)에서 얻는 valuation gain은 \(O(n)\)뿐이다. 근사지수 비율이 0으로 가므로 무리성 판정을 만들지 못한다.

편집상 한 가지 정정도 필요하다. v2.3의 “first odd primes” 표는 \(p=11\)을 빠뜨렸다. \(p=11\)의 good classes는

\[
t\equiv2,3,5,7\pmod{11}.
\]

따라서 이 행을 추가하거나 표 제목을 “sample primes”로 바꾸는 것이 맞다.

---

## 11. 권장 v2.4 통합 순서

1. **주정리로 승격:** 정리 A와 B를 연속 배치한다. “level arithmetic → zero arithmetic → trace arithmetic”의 새 축이 된다.
2. **special-functions subsection:** 정리 C와 D를 넣는다. lower incomplete Gamma의 positive-integer derivatives와 order-axis Hankel tower를 한 절로 묶는다.
3. **짧고 강한 corollary:** 정리 E의 \(S_m+iX\) family를 넣는다.
4. **relative algebra section:** \(K(\gamma,\delta)\) 위 defect-one 정리를 넣는다.
5. **barriers section:** 유명 난제는 해결하지 않았음을 명시하고, \(p\)-adic height/valuation mismatch를 정량적으로 남긴다.

### 최종 가치 판정

- **논문 내부의 새 정리 가치:** 높음. 특히 B·C·D는 서로 다른 분야를 실제 theorem으로 연결한다.
- **초월수론 자체의 깊이:** 중상. 깊은 새 외부 초월수 정리를 만든 것이라기보다 001의 강한 공동 독립성을 정확히 수송하여 예상 밖의 새 명시적 결과를 얻은 형태다.
- **유명 고난도 난제 해결:** 없음.
- **권장 표현:** “new unconditional consequences”, “complete classification for this family”, “apparently new order-axis/Gamma-jet corollary”.
- **피해야 할 표현:** “Jossen conjecture solved”, “Kurepa solved”, “\(\gamma\) or \(\delta\) transcendence proved”.

출판 전략상 가장 좋은 포장은 **새로운 독립 입력을 추가한 논문**이 아니라, 이미 확보한 001의 독립 입력과 v2.3의 exact spectral functor를 결합해 **영점·스펙트럼·Gamma derivatives·Hankel geometry를 동시에 닫는 transfer paper**라는 것이다.

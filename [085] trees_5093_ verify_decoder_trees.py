#!/usr/bin/env python3
"""Computational companion to "Decoder Trees and Kisielewicz's Identity:
Equations 5093 and 5107 Are Austin Laws".

For k >= 3 and theta in {'left', 'owner'} this implements the decoder-tree magma
T_k^theta(X) of the paper (Definitions 4.1 and 5.5) and checks the law
    theta = 'left' :  E_k : x = y*(y*( ... (y*(x*(z*y))) ... ))   (k leading y's)
    theta = 'owner':  G_k : x = y*(y*( ... (y*(z*(x*y))) ... ))   (k leading y's)
on large finite samples (E_3 is ETP Equation 5093 and G_3 is ETP Equation 5107).
It also checks every structural lemma of the paper on random and targeted
instances, and cross-checks the clause-based implementation against an
independent brute-force implementation of the semantic description (Lemma 5.6).
Usage:  python3 verify_decoder_trees.py [--quick]   (standard library only; each
family/k is checked in a separate process to bound memory use)
"""
import sys, random
from functools import lru_cache
sys.setrecursionlimit(1 << 20)

# ---------- hash-consed binary trees: node id -> None (leaf) or (left, right) ----------
NODES, IDX, SIZE = [], {}, []
def leaf(i):
    key = ('leaf', i)
    if key not in IDX:
        IDX[key] = len(NODES); NODES.append(None); SIZE.append(1)
    return IDX[key]
def pair(l, r):
    key = (l, r)
    if key not in IDX:
        IDX[key] = len(NODES); NODES.append(key); SIZE.append(SIZE[l] + SIZE[r] + 1)
    return IDX[key]
def ispair(t): return NODES[t] is not None
def L(t): return NODES[t][0]
def R(t): return NODES[t][1]
def tower(c, j, u):                      # c^[j] u = <c,<c,...<c,u>...>>
    for _ in range(j): u = pair(c, u)
    return u
def untower(c, p, j):                    # the t with p = c^[j] t, or None
    for _ in range(j):
        if not ispair(p) or L(p) != c: return None
        p = R(p)
    return p
def proper_subtrees(t):
    out, st = set(), [t]
    while st:
        s = st.pop()
        if ispair(s):
            for c in (L(s), R(s)):
                if c not in out: out.add(c); st.append(c)
    return out

class DecoderTree:
    """The decoder-tree magma T_k^theta (Definitions 4.1 and 5.5 of the paper)."""
    def __init__(self, k, theta):
        assert k >= 3 and theta in ('left', 'owner')
        self.k, self.theta = k, theta
        self.D = lru_cache(maxsize=None)(self._D)
        self.F = lru_cache(maxsize=None)(self._F)
        self.kappa = lru_cache(maxsize=None)(self._kappa)
        self.mul = lru_cache(maxsize=None)(self._mul)
        self.nonunique = []
    def _F(self, c, p):                  # F(c,p): p = c^[k-1] t with D(c,t) nonempty
        t = untower(c, p, self.k - 1)
        return t is not None and len(self.D(c, t)) > 0
    def _kappa(self, a):                 # special key set: D(a_L, t) if a = a_L^[k-1] t
        if not ispair(a): return frozenset()
        t = untower(L(a), a, self.k - 1)
        return self.D(L(a), t) if t is not None else frozenset()
    def generic_key(self, a, w):         # w = <c,a> with not F(c,a)
        return ispair(w) and R(w) == a and not self.F(L(w), a)
    def is_key(self, a, w):              # w in K(a)
        return self.generic_key(a, w) or w in self.kappa(a)
    def owner(self, a, w):               # o_a(w): c for w = <c,a> generic, a_L for the special key
        return L(w) if self.generic_key(a, w) else L(a)
    def out(self, a, x, w):              # theta_a(x, w)
        return x if self.theta == 'left' else self.owner(a, w)
    def _D(self, a, u):
        k, res = self.k, set()
        if ispair(u) and self.is_key(a, R(u)) and not self.F(L(u), R(u)):        # clause alpha
            res.add(self.out(a, L(u), R(u)))
        if ispair(a):                                                            # clause beta
            s = untower(L(a), a, k - 2)
            if s is not None and not self.F(L(a), a) and u in self.D(L(a), s):
                res.add(L(a))
        for v in self.kappa(a):                                                  # clause gamma
            if ispair(v):
                x = L(v); s = untower(x, v, k - 1)
                if s is not None and SIZE[x] + SIZE[s] < SIZE[a] + SIZE[u] and u in self.D(x, s):
                    res.add(self.out(a, x, v))
        if len(res) > 1: self.nonunique.append((a, u, res))
        return frozenset(res)
    def _mul(self, a, p):
        t = untower(a, p, self.k - 1)
        if t is not None:
            d = self.D(a, t)
            if d: return min(d)
        return pair(a, p)
    def Lpow(self, a, u, n):
        for _ in range(n): u = self.mul(a, u)
        return u
    def core(self, x, y, z):             # the term inside L_y^k
        return self.mul(x, self.mul(z, y)) if self.theta == 'left' else self.mul(z, self.mul(x, y))
    def law(self, x, y, z):
        return self.Lpow(y, self.core(x, y, z), self.k) == x

def trees_upto(gens, max_internal):
    by = {0: list(gens)}
    for n in range(1, max_internal + 1):
        by[n] = [pair(l, r) for i in range(n) for l in by[i] for r in by[n - 1 - i]]
    return [t for n in range(max_internal + 1) for t in by[n]]

def structured_pool(M, base, steps, rng):
    pool, k = list(base), M.k
    for _ in range(steps):
        a, b, c = rng.choice(pool), rng.choice(pool), rng.choice(pool)
        r = rng.random()
        if r < 0.3: pool.append(M.mul(a, b))
        elif r < 0.6: pool.append(M.Lpow(a, M.core(b, a, c), rng.randrange(k + 1)))
        else:
            y = M.mul(a, b); pool.append(y)
            pool.append(M.Lpow(y, M.core(a, y, a), rng.randrange(k)))
    return pool

# ---------- independent brute-force implementation of the semantics (nested tuples) ----------
def bf_model(k, theta):
    def isleaf(t): return t[0] == 'g'
    def psub(t):
        out, st = set(), [t]
        while st:
            s = st.pop()
            if not isleaf(s):
                for c in s:
                    if c not in out: out.add(c); st.append(c)
        return out
    def untower_t(c, p, j):
        for _ in range(j):
            if isleaf(p) or p[0] != c: return None
            p = p[1]
        return p
    @lru_cache(maxsize=None)
    def mul(a, p):                       # a*p = x iff p = a^[k-1]u and dec(a,u) = {x}
        u = untower_t(a, p, k - 1)
        if u is not None:
            d = dec(a, u)
            if d:
                assert len(d) == 1
                return next(iter(d))
        return (a, p)
    @lru_cache(maxsize=None)
    def dec(a, u):                       # E: {x : x*(c*a) = u};  G: {x : z*(x*a) = u}, by search
        cand = psub(a) | psub(u) | {a, u}
        if theta == 'left':
            return frozenset(x for x in cand for c in cand if mul(x, mul(c, a)) == u)
        return frozenset(x for x in cand for z in cand if mul(z, mul(x, a)) == u)
    return mul

def to_tuple(t, memo={}):
    if t not in memo:
        memo[t] = ('g', [kk for kk, v in IDX.items() if v == t][0][1]) if not ispair(t) else (to_tuple(L(t)), to_tuple(R(t)))
    return memo[t]

def check_family(theta, k, quick, rng):
    M, gens = DecoderTree(k, theta), [leaf(0), leaf(1)]
    small = trees_upto(gens, 2 if quick else 3)
    name = ('E' if theta == 'left' else 'G') + str(k)
    ok = True
    bad = sum(1 for x in small for y in small for z in small if not M.law(x, y, z))
    print(f"[{name}] exhaustive: {len(small)**3} triples, violations {bad}", flush=True); ok &= bad == 0
    pool = structured_pool(M, small, 300 if quick else 1500, rng)
    N = 3000 if quick else 20000
    bad = sum(1 for _ in range(N) if not M.law(rng.choice(pool), rng.choice(pool), rng.choice(pool)))
    print(f"[{name}] structured random: {N} triples, violations {bad}", flush=True); ok &= bad == 0
    # targeted instances making the core contract through clause beta or clause gamma
    bad = n = 0
    for _ in range(300 if quick else 2000):
        x, q, c1, c, c2, xx, zz = (rng.choice(pool) for _ in range(7))
        s = M.core(q, x, c1)                     # q is in D(x, s)
        y1 = tower(x, k - 2, s)                  # beta: x * <x,y1> contracts
        v = tower(x, k - 1, s)
        t = M.core(v, c, c2)                     # v is in D(c, t)
        y2 = tower(c, k - 1, t)                  # kappa(y2) = {v}: gamma
        assert M.kappa(y2) == frozenset([v])
        inst = ((x, y1, x), (xx, y1, zz), (x, y2, c), (xx, y2, c), (xx, y2, zz)) if theta == 'left' else \
               ((x, y1, x), (xx, y1, zz), (c, y2, x), (c, y2, zz), (xx, y2, zz))
        for (a, b, cc) in inst:
            n += 1; bad += not M.law(a, b, cc)
    print(f"[{name}] targeted beta/gamma instances: {n}, violations {bad}", flush=True); ok &= bad == 0
    # lemma checks
    viol = dict(Sub=0, U=0, V1=0, V2=0, Sem=0, Dec=0, Normal=0)
    memo = {}
    def normal(t):
        if t not in memo:
            memo[t] = (not ispair(t)) or (normal(L(t)) and normal(R(t)) and not M.F(L(t), R(t)))
        return memo[t]
    for _ in range(3000 if quick else 20000):
        a, x, c, p = (rng.choice(pool) for _ in range(4))
        w = M.mul(c, a)                          # a key of a, with owner c
        u = M.mul(x, w) if theta == 'left' else M.mul(x, M.mul(c, a))
        expected = x if theta == 'left' else c
        d = M.D(a, u)
        viol['Sem'] += (not M.is_key(a, w)) or M.owner(a, w) != c or (expected not in d)
        viol['U'] += len(d) > 1
        viol['Sub'] += not d <= (proper_subtrees(a) | proper_subtrees(u))
        t, early = u, False
        for _j in range(k - 1):
            t2 = M.mul(a, t); early |= (t2 != pair(a, t)); t = t2
        viol['Dec'] += early or M.mul(a, t) != expected
        viol['V1'] += len(M.D(a, a)) > 0
        viol['V2'] += len(M.D(a, w)) > 0
        if normal(a) and normal(p): viol['Normal'] += not normal(M.mul(a, p))
    print(f"[{name}] lemma checks (violations): {viol}; non-unique D: {len(M.nonunique)}", flush=True)
    ok &= sum(viol.values()) == 0 and not M.nonunique
    return ok

def cross_check(theta, quick, rng):
    k = 3; M, bf = DecoderTree(k, theta), bf_model(k, theta)
    small = trees_upto([leaf(0), leaf(1)], 2)
    T = lambda t: to_tuple(t)
    def bf_law(x, y, z):
        core = bf(T(x), bf(T(z), T(y))) if theta == 'left' else bf(T(z), bf(T(x), T(y)))
        for _ in range(k): core = bf(T(y), core)
        return core == T(x)
    bad = sum(1 for x in small for y in small for z in small if not bf_law(x, y, z))
    pool = [p for p in structured_pool(M, small, 200, rng) if SIZE[p] < 120]
    dis = fires = 0
    for _ in range(600 if quick else 3000):
        a = rng.choice(pool); r = rng.random()
        if r < 0.4: p = rng.choice(pool)
        elif r < 0.7: p = tower(a, k - 1, rng.choice(pool))
        else: p = tower(a, k - 1, M.core(rng.choice(pool), a, rng.choice(pool)))   # a firing product
        res = M.mul(a, p); fires += res != pair(a, p)
        dis += T(res) != bf(T(a), T(p))
    name = 'E3' if theta == 'left' else 'G3'
    print(f"[cross-check {name}] brute-force semantic model: law violations {bad} on {len(small)**3} triples; "
          f"product disagreements {dis} ({fires} firing products compared)", flush=True)
    return bad == 0 and dis == 0

def example_check():
    """Reproduces Example 5.8 of the paper (k = 3, type lambda)."""
    M, g, h, P = DecoderTree(3, 'left'), leaf(0), leaf(1), pair
    u = M.mul(g, M.mul(g, g))                                     # clause alpha
    assert u == P(g, P(g, g)) and M.D(g, u) == {g} and M.Lpow(g, u, 3) == g
    s = M.mul(h, M.mul(g, g)); y = P(g, s)                        # clause beta
    assert s == P(h, P(g, g)) and M.D(g, s) == {h}
    assert M.mul(g, y) == P(g, y) and M.mul(g, P(g, y)) == h and M.D(y, h) == {g}
    assert M.mul(y, h) == P(y, h) and M.mul(y, P(y, h)) == P(y, P(y, h)) and M.Lpow(y, h, 3) == g
    v = tower(g, 2, s); t = M.mul(v, M.mul(g, h)); y2 = tower(h, 2, t)   # clause gamma
    assert t == P(v, P(g, h)) and M.D(h, t) == {v} and M.kappa(y2) == {v}
    assert M.mul(h, y2) == v and M.mul(g, v) == h and M.D(y2, h) == {g} and M.Lpow(y2, h, 3) == g
    print("[example] Example 5.8 reproduced", flush=True)
    return True

def run_one(job, quick):
    theta, k = job[0], int(job[1])
    rng = random.Random(20261028 + 10 * k + (theta == 'owner'))
    if k == 0: return cross_check(theta, quick, rng)
    ok = example_check() if (theta, k) == ('left', 3) else True
    return check_family(theta, k, quick, rng) and ok

def main(quick):
    # each job runs in a fresh process, so that memory use stays bounded
    import subprocess
    ok = True
    for theta in ('left', 'owner'):
        for k in (3, 4, 5, 0):                     # k = 0 means: cross-check for k = 3
            cmd = [sys.executable, __file__, '--one', theta, str(k)] + (['--quick'] if quick else [])
            ok &= subprocess.run(cmd).returncode == 0
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
    return 0 if ok else 1

if __name__ == '__main__':
    quick = '--quick' in sys.argv
    if '--one' in sys.argv:
        i = sys.argv.index('--one')
        sys.exit(0 if run_one(sys.argv[i + 1:i + 3], quick) else 1)
    sys.exit(main(quick))

# The Polyexponential Trace-Tower Program, v3.1

This directory is the complete, offline-buildable source tree for the
integrated research monograph

> *The Polyexponential Trace-Tower Program: Moving Levels, Faber and
> Inverse Monodromy, Positive Spectra, and Arithmetic Barriers*.

The typeset authority is `main.tex` together with the reviewed files in
`parts/`.  Research notes and source-preparation material are retained for
provenance, but they do not override the statements or status assignments in
the monograph.

Version 3.1 adds the complete Maynard mean-square citation, the strict Kaluza
reciprocal-sign proof for every integer polylogarithmic order, all-degree
polylogarithmic Faber indecomposability, prime-degree and `m = p + 2`
symmetric monodromy, and exact fixed-order odd-degree window certificates
through degree 1001.  The factorially weighted `f_{sigma,tau}` family remains
outside this global closure.

## Build the PDF

From this directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

Equivalently:

```sh
make pdf
```

The result is `build/main.pdf`.  The build uses pdfLaTeX through `latexmk`;
LuaLaTeX and XeLaTeX are not required.  No network access is needed once the
dependencies listed in `BUILD_ENVIRONMENT.txt` are installed.

For a clean source-archive reproduction, the recommended sequence is:

```sh
sha256sum -c CHECKSUMS.sha256
make pdf
make check-quick
```

`CHECKSUMS.sha256` is supplied in the release archive.  During development,
before that manifest has been generated, begin with `make pdf`.

## Logical-status system

The letters below are part of the mathematical claim language, not editorial
ratings.  The detailed assignment of individual results is in the monograph's
status ledger.

| Code | Printed form | Exact meaning |
|---|---|---|
| U | `U-PASS` | Unconditional theorem, proved using only the displayed argument and standard cited results. |
| X | `X-PASS` | Unconditional **finite** theorem certified by exact integer or finite-field computation shipped here.  It is not extrapolated beyond its stated range. |
| R | `R-PASS` | Theorem relative to the explicitly cited algebraic-independence input from companion paper [001]. |
| C | `C-PASS` | Correct implication from an explicitly displayed hypothesis that remains open. |
| O | `OPEN` | Open, unproved, or deliberately excluded; it is never silently used in an unconditional conclusion. |

If a heading or historical source note is unbadged, the integrated status
ledger in `parts/09_status_ledger.tex` governs it.

## Reproduce the exact computations

All proof-relevant programs use exact rational, integer, or finite-field
arithmetic.  Floating-point output is not used to certify a Galois group,
separability statement, or valuation.

### Quick suite

```sh
make check-quick
```

This is a representative smoke test: it checks the fixed polylogarithmic
orders \(\tau=1,2,3,4\) through odd degree 1001, the Bertrand-prime route
through degree 1001 at order one, the original window selection through
degree 10,000, small exact Morse witnesses, and a compiled finite-field
derivative-separability audit.  It is intended to detect a broken Python,
SymPy, compiler, or source checkout quickly; it is not the full published
range.

### Extended suite

```sh
make check-extended
```

This reruns the frozen published ranges and compares the stable summaries
with the captured outputs in `computation/`:

- all-order rectangle through `m = 1001`, with ten candidate window primes;
- fixed polylogarithmic orders `tau = 1, 2, 3, 4` through odd degree `1001`;
- order-one Bertrand-prime certificates through `m = 100000`;
- original-tower window selection through `m = 1000000`;
- derivative and polar separability through degree `5000`;
- exact Morse witnesses through degree `55`;
- the independent `m = 27` character certificate; and
- the default mod-409 arithmetic certificates used in the degree-401 audit.

The extended suite can be substantially slower and more memory intensive
than the PDF build.  To rerun the additional all-odd degree-401 search, use:

```sh
make check-all-odd-401
```

Generated check logs and compiled helper binaries are written only under
`build/`.

## Directory map

- `main.tex` — master document, preamble, title matter, and inclusion order.
- `parts/` — frozen, reviewed LaTeX modules; these are the typeset authority.
- `computation/` — exact programs, mathematical audit notes, and captured
  outputs for finite certificates.
- `research_sources/` — retained Markdown research manuscripts and provenance
  material; these are not a second claim authority.
- `audits/` — selected independent referee/audit reports, retained as
  non-authoritative provenance.
- `source_snapshots/` — the v2.3 tower and v2.4 addendum predecessor sources;
  both are superseded by the curated Version 3.1 modules.
- `tools/prepare_sources.py` — one-time source-ingestion provenance utility.
- `build/` — generated PDF, LaTeX auxiliaries, test logs, and compiled helpers.
- `BUILD_ENVIRONMENT.txt` — reference toolchain and dependency inventory.

## Important source-freeze rule

Do **not** run `tools/prepare_sources.py` for an ordinary build.  It describes
the historical ingestion step and expects predecessor files outside this
standalone tree.  More importantly, it regenerates raw draft modules and can
overwrite the later hand-audited corrections in `parts/`.  The curated
`parts/` directory shipped here is frozen and sufficient to compile the PDF.

## Cleaning generated files

```sh
make clean
```

This asks `latexmk` to remove its auxiliary products and deletes only the
generated check directory and helper binary under `build/`.  Source files and
captured certificate outputs under `computation/` are left untouched.

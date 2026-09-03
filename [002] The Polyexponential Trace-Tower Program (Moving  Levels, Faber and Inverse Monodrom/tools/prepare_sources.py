#!/usr/bin/env python3
"""Prepare modular LaTeX inputs for the v3.0 master monograph.

This script is deliberately deterministic.  It extracts the audited bodies of
the two existing TeX manuscripts and converts selected Markdown research
manuscripts with Pandoc.  The generated files are then curated in-tree and are
shipped in the final source archive, so rebuilding the PDF itself does not
require access to the original workspace.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "master_v30"
PARTS = OUT / "parts"
RESEARCH = OUT / "research_sources"

V23 = ROOT / "work_v23" / "KEIO_Moving_Level_Trace_Towers_v2_3.tex"
ADDENDUM = ROOT / "output" / "source" / "KEIO_Trace_Barrier_Escape_Addendum_v2_4.tex"


def between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j].rstrip() + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def extract_existing_tex() -> None:
    v = V23.read_text(encoding="utf-8")
    write(
        PARTS / "01_tower_foundations.tex",
        between(v, r"\section{Introduction and exact scope}",
                r"\section{An explicit solution of a 2026 Euler recurrence}"),
    )
    write(
        PARTS / "06_ramanujan_gamma.tex",
        between(v, r"\section{An explicit solution of a 2026 Euler recurrence}",
                r"\section{The critical moving-point barrier}"),
    )
    write(
        PARTS / "08_arithmetic_barriers.tex",
        between(v, r"\section{The critical moving-point barrier}", r"\appendix"),
    )
    write(
        PARTS / "A_original_appendices.tex",
        between(v, r"\section{An \texorpdfstring{\(\Ein\)}{Ein}-linear realization of",
                r"\begin{thebibliography}{99}"),
    )
    write(
        PARTS / "Z_references.tex",
        between(v, r"\begin{thebibliography}{99}", r"\end{document}")
        .replace(r"\end{thebibliography}", r"\end{thebibliography}"),
    )

    a = ADDENDUM.read_text(encoding="utf-8")
    section_re = re.compile(r"(?=^\\section\{)", re.MULTILINE)
    chunks = section_re.split(a)
    wanted = {
        "Prime degree: a complete Morse theorem",
        "A moving-prime isolated transposition",
        "Exact finite rectangles",
        "Large order: complex regular polygons replace real critical points",
        "Local Faber transfer beyond the polyexponential tower",
        "Shifted discriminants, partial separability, and conditional density one",
        "Exact negative results that prevent a false proof",
        "The remaining theorem gate",
    }
    selected: list[str] = []
    for chunk in chunks:
        m = re.match(r"\\section\{([^}]*)\}", chunk)
        if m and m.group(1) in wanted:
            selected.append(chunk.rstrip())
    write(PARTS / "03_barrier_escape.tex", "\n\n".join(selected) + "\n")


MARKDOWN_PARTS = [
    ("TRACE_MONODROMY_ALL_Q.md", "02_uniform_faber_monodromy.tex"),
    ("ALL_ORDER_POLYEXPONENTIAL_INVERSE_MONODROMY.md", "05_inverse_monodromy.tex"),
    ("order_axis_stp_jacobi_audit.md", "07_order_axis_stp_jacobi.tex"),
    ("order_axis_double_scaling_complete.md", "07b_double_scaling.tex"),
    ("Gamma_Tail_DT_Zero_Density_Motive_Audit.md", "07c_gamma_tail.tex"),
    ("GAMMA_JET_SPECTRAL_SIEVE_ALL_Q.md", "07d_gamma_spectral_sieve.tex"),
    ("KEIO_001_v23_New_Closures_Research_Note.md", "07e_transfer_closures.tex"),
    ("Jossen_Multigenerator_Polyexponential_Audit.md", "07f_jossen_reductions.tex"),
]


def convert_markdown() -> None:
    source_dir = ROOT / "output" / "research"
    for source_name, target_name in MARKDOWN_PARTS:
        source = source_dir / source_name
        shutil.copy2(source, RESEARCH / source_name)
        target = PARTS / target_name
        subprocess.run(
            [
                "pandoc",
                "--from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex",
                "--to=latex",
                "--top-level-division=section",
                f"--id-prefix={Path(target_name).stem}-",
                "--wrap=preserve",
                str(source),
                "-o",
                str(target),
            ],
            check=True,
        )


def copy_computation() -> None:
    source_dir = ROOT / "output" / "research"
    names = [
        "trace_morse_certificates.py",
        "trace_allq_modp_audit.py",
        "trace_allq_modp_audit_1001.txt",
        "trace_galois_401.py",
        "odd_trace_padic_certify.py",
        "odd_trace_padic_certify_100000.txt",
        "odd_trace_modp_route.py",
        "window_prime_selection_audit.py",
        "window_prime_selection_audit_1000000.txt",
        "even_derivative_separability_audit.cpp",
        "even_derivative_separability_audit_1000.txt",
        "even_derivative_separability_audit_5000.txt",
        "TRACE_MORSE_EXACT_CERTIFICATES.md",
        "WINDOW_PRIME_SELECTION_AUDIT.md",
        "ODD_TRACE_MODP_ROUTE.md",
        "ODD_TRACE_PADIC_ROUTE.md",
        "EVEN_DERIVATIVE_SEPARABILITY.md",
    ]
    for name in names:
        src = source_dir / name
        if src.exists():
            shutil.copy2(src, OUT / "computation" / name)


def main() -> None:
    PARTS.mkdir(parents=True, exist_ok=True)
    RESEARCH.mkdir(parents=True, exist_ok=True)
    (OUT / "computation").mkdir(parents=True, exist_ok=True)
    extract_existing_tex()
    convert_markdown()
    copy_computation()


if __name__ == "__main__":
    main()

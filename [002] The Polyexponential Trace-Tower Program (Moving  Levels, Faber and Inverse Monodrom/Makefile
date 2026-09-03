SHELL := /bin/sh

PYTHON ?= python3
CXX ?= g++
CXXFLAGS ?= -O3 -std=c++17

BUILD_DIR := build
CHECK_DIR := $(BUILD_DIR)/checks
EVEN_AUDIT := $(BUILD_DIR)/even_derivative_separability_audit

export LC_ALL := C
export PYTHONHASHSEED := 0

.PHONY: all pdf verify-manifest check check-quick check-extended \
	check-all-odd-401 clean help

all: pdf

pdf:
	mkdir -p $(BUILD_DIR)
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex

verify-manifest:
	@test -f CHECKSUMS.sha256 || { echo "CHECKSUMS.sha256 is absent (development tree, not release archive)" >&2; exit 1; }
	sha256sum -c CHECKSUMS.sha256

$(EVEN_AUDIT): computation/even_derivative_separability_audit.cpp
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $< -o $@

check: check-quick

check-quick: $(EVEN_AUDIT)
	mkdir -p $(CHECK_DIR)
	$(PYTHON) computation/polylog_window_prime_audit.py --bound 1001 | tee $(CHECK_DIR)/polylog_window_prime_audit_1001.txt
	grep -Fqx 'POLYLOG_WINDOW_AUDIT=PASS' $(CHECK_DIR)/polylog_window_prime_audit_1001.txt
	$(PYTHON) computation/odd_trace_padic_certify.py --max-m 1001 --order 1 --prime-trials 12 | tee $(CHECK_DIR)/odd_trace_padic_1001.txt
	$(PYTHON) computation/window_prime_selection_audit.py --bound 10000 | tee $(CHECK_DIR)/window_prime_selection_10000.txt
	grep -Fqx 'SELECTION_AUDIT=PASS' $(CHECK_DIR)/window_prime_selection_10000.txt
	$(PYTHON) computation/trace_morse_certificates.py --max-m 12 --prime-bound 1000 | tee $(CHECK_DIR)/trace_morse_12.txt
	awk '$$2 == "None" { bad=1 } END { exit bad }' $(CHECK_DIR)/trace_morse_12.txt
	$(EVEN_AUDIT) --bound 500 | tee $(CHECK_DIR)/even_derivative_500.txt
	grep -Fqx 'DS_AUDIT=PASS' $(CHECK_DIR)/even_derivative_500.txt
	grep -Fqx 'POLAR_AUDIT=PASS' $(CHECK_DIR)/even_derivative_500.txt

check-extended: $(EVEN_AUDIT)
	mkdir -p $(CHECK_DIR)
	$(PYTHON) computation/polylog_window_prime_audit.py --bound 1001 > $(CHECK_DIR)/polylog_window_prime_audit_1001.txt
	diff -u computation/polylog_window_prime_audit_1001.txt $(CHECK_DIR)/polylog_window_prime_audit_1001.txt
	$(PYTHON) computation/trace_allq_modp_audit.py --bound 1001 --candidate-count 10 > $(CHECK_DIR)/trace_allq_modp_audit_1001.txt
	diff -u computation/trace_allq_modp_audit_1001.txt $(CHECK_DIR)/trace_allq_modp_audit_1001.txt
	$(PYTHON) computation/odd_trace_padic_certify.py --max-m 100000 --order 1 --prime-trials 12 > $(CHECK_DIR)/odd_trace_padic_certify_100000.txt
	diff -u computation/odd_trace_padic_certify_100000.txt $(CHECK_DIR)/odd_trace_padic_certify_100000.txt
	$(PYTHON) computation/window_prime_selection_audit.py --bound 1000000 > $(CHECK_DIR)/window_prime_selection_audit_1000000.txt
	diff -u computation/window_prime_selection_audit_1000000.txt $(CHECK_DIR)/window_prime_selection_audit_1000000.txt
	$(EVEN_AUDIT) --bound 5000 > $(CHECK_DIR)/even_derivative_separability_audit_5000.txt
	diff -u computation/even_derivative_separability_audit_5000.txt $(CHECK_DIR)/even_derivative_separability_audit_5000.txt
	$(PYTHON) computation/trace_morse_certificates.py --max-m 55 --prime-bound 3000 > $(CHECK_DIR)/trace_morse_55.txt
	awk '$$2 == "None" { bad=1 } END { exit bad }' $(CHECK_DIR)/trace_morse_55.txt
	$(PYTHON) computation/odd_trace_modp_route.py > $(CHECK_DIR)/odd_trace_modp_route.txt
	$(PYTHON) computation/trace_galois_401.py > $(CHECK_DIR)/trace_galois_401.txt

check-all-odd-401:
	mkdir -p $(CHECK_DIR)
	$(PYTHON) computation/trace_galois_401.py --all-odd > $(CHECK_DIR)/trace_galois_401_all_odd.txt

clean:
	latexmk -c -outdir=build main.tex
	rm -f $(EVEN_AUDIT)
	rm -rf $(CHECK_DIR)

help:
	@printf '%s\n' \
	  'make pdf                build build/main.pdf with pdfLaTeX/latexmk' \
	  'make verify-manifest    verify the release SHA-256 manifest' \
	  'make check-quick        run representative exact smoke checks' \
	  'make check-extended     reproduce frozen published ranges' \
	  'make check-all-odd-401  run the additional long mod-409 search' \
	  'make clean              remove generated build auxiliaries/checks'

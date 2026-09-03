#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

// Exact finite-field audit for the q=1 derivative-separability hypothesis.
//
// Put g(z)=-Ein(-z)=sum_{n>=1} z^n/(n n!).  Up to X -> -X and a
// nonzero scalar, P'_{1,r}(X) is
//
//   H_r(X)=sum_{k=1}^r [z^r]g(z)^k X^{k-1}.
//
// We compute all powers g^k truncated at --bound over F_MOD.  A constant
// gcd(H_r,H'_r) proves that the characteristic-zero polynomial is
// square-free.  MOD is prime and is larger than every supported bound, so
// all denominators n n! are units and every H_r keeps its full degree.

namespace {

constexpr std::int64_t MOD = 998244353;

std::int64_t mod_pow(std::int64_t base, std::int64_t exponent) {
  std::int64_t result = 1;
  while (exponent > 0) {
    if (exponent & 1) result = result * base % MOD;
    base = base * base % MOD;
    exponent >>= 1;
  }
  return result;
}

void trim(std::vector<std::int64_t>& polynomial) {
  while (polynomial.size() > 1 && polynomial.back() == 0)
    polynomial.pop_back();
}

std::vector<std::int64_t> remainder(
    std::vector<std::int64_t> left,
    const std::vector<std::int64_t>& right) {
  const std::int64_t inverse_lead = mod_pow(right.back(), MOD - 2);
  while (left.size() >= right.size() && !(left.size() == 1 && left[0] == 0)) {
    const std::int64_t factor = left.back() * inverse_lead % MOD;
    const std::size_t shift = left.size() - right.size();
    if (factor != 0) {
      for (std::size_t j = 0; j < right.size(); ++j) {
        left[shift + j] =
            (left[shift + j] - factor * right[j]) % MOD;
        if (left[shift + j] < 0) left[shift + j] += MOD;
      }
    }
    trim(left);
  }
  return left;
}

bool square_free(std::vector<std::int64_t> polynomial) {
  std::vector<std::int64_t> derivative(polynomial.size() - 1);
  for (std::size_t j = 1; j < polynomial.size(); ++j)
    derivative[j - 1] = static_cast<std::int64_t>(j) * polynomial[j] % MOD;
  trim(polynomial);
  trim(derivative);
  while (!(derivative.size() == 1 && derivative[0] == 0)) {
    polynomial = remainder(std::move(polynomial), derivative);
    std::swap(polynomial, derivative);
  }
  return polynomial.size() == 1;
}

int parse_bound(int argc, char** argv) {
  int bound = 1000;
  for (int index = 1; index < argc; ++index) {
    const std::string argument = argv[index];
    if (argument == "--bound" && index + 1 < argc) {
      bound = std::stoi(argv[++index]);
    } else {
      throw std::runtime_error("usage: audit [--bound N]");
    }
  }
  if (bound < 2 || bound >= MOD)
    throw std::runtime_error("bound must satisfy 2 <= bound < MOD");
  return bound;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    const int bound = parse_bound(argc, argv);

    std::vector<std::int64_t> inverse(bound + 1, 1);
    for (int n = 2; n <= bound; ++n)
      inverse[n] = MOD - (MOD / n) * inverse[MOD % n] % MOD;

    std::vector<std::int64_t> g(bound + 1, 0);
    std::int64_t inverse_factorial = 1;
    for (int n = 1; n <= bound; ++n) {
      inverse_factorial = inverse_factorial * inverse[n] % MOD;
      g[n] = inverse_factorial * inverse[n] % MOD;
    }

    // rows[n][k-1] is [z^n]g(z)^k.  Besides the even DS rows, retaining
    // odd rows lets us audit the polar B_n=2H_n+XH'_n used by the
    // fixed-offset theorem.
    std::vector<std::vector<std::int64_t>> rows(bound + 1);
    for (int n = 1; n <= bound; ++n) rows[n].assign(n, 0);

    std::vector<std::int64_t> power(bound + 1, 0);
    std::vector<std::int64_t> next(bound + 1, 0);
    power[0] = 1;
    for (int k = 1; k <= bound; ++k) {
      std::fill(next.begin(), next.end(), 0);
      for (int n = k; n <= bound; ++n) {
        std::uint64_t accumulator = 0;
        const int largest_part = n - k + 1;
        for (int j = 1; j <= largest_part; ++j) {
          accumulator +=
              static_cast<std::uint64_t>(g[j]) * power[n - j] % MOD;
          if (accumulator >= (static_cast<std::uint64_t>(MOD) << 32))
            accumulator %= MOD;
        }
        next[n] = static_cast<std::int64_t>(accumulator % MOD);
        rows[n][k - 1] = next[n];
      }
      power.swap(next);
    }

    std::vector<int> failures;
    for (int degree = 2; degree <= bound; degree += 2) {
      if (!square_free(rows[degree])) failures.push_back(degree);
    }

    std::vector<int> polar_failures;
    for (int degree = 3; degree <= bound; degree += 2) {
      std::vector<std::int64_t> polar = rows[degree];
      for (int j = 0; j < degree; ++j)
        polar[j] = static_cast<std::int64_t>(j + 2) * polar[j] % MOD;
      if (!square_free(std::move(polar))) polar_failures.push_back(degree);
    }

    std::cout << "BOUND=" << bound << '\n';
    std::cout << "MODULUS=" << MOD << '\n';
    std::cout << "EVEN_ROWS_TESTED=" << bound / 2 << '\n';
    std::cout << "FAILURES=[";
    for (std::size_t index = 0; index < failures.size(); ++index) {
      if (index) std::cout << ", ";
      std::cout << failures[index];
    }
    std::cout << "]\n";
    std::cout << "DS_AUDIT=" << (failures.empty() ? "PASS" : "FAIL") << '\n';
    std::cout << "NONCONSTANT_ODD_POLAR_ROWS_TESTED=" << (bound - 1) / 2
              << '\n';
    std::cout << "POLAR_FAILURES=[";
    for (std::size_t index = 0; index < polar_failures.size(); ++index) {
      if (index) std::cout << ", ";
      std::cout << polar_failures[index];
    }
    std::cout << "]\n";
    std::cout << "POLAR_AUDIT="
              << (polar_failures.empty() ? "PASS" : "FAIL") << '\n';
    return failures.empty() && polar_failures.empty() ? 0 : 1;
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 2;
  }
}

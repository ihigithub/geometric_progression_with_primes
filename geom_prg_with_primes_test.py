import pytest
from geom_prg_with_primes import geo_prg_primes


def test_geo_prg_primes():
    prime_numbers = 5

    expected_result = 3*5*7*11*13
    actual_result = geo_prg_primes(prime_numbers)
    assert expected_result == actual_result
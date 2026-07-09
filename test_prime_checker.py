
from prime_checker import is_prime


def test_number_less_than_2_is_not_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False


def test_2_is_prime():
    assert is_prime(2) is True


def test_prime_numbers():
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(17) is True


def test_non_prime_numbers():
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(9) is False
    assert is_prime(25) is False

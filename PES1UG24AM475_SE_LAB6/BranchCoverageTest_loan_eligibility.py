
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


# Credit score validation branches
def test_score_below_minimum():
    with pytest.raises(ValueError):
        credit_band(200)


def test_score_above_maximum():
    with pytest.raises(ValueError):
        credit_band(950)


def test_score_valid_boundaries():
    assert credit_band(300) == "poor"
    assert credit_band(550) == "fair"
    assert credit_band(650) == "good"
    assert credit_band(750) == "excellent"
    assert credit_band(900) == "excellent"


# Eligibility employment branches
def test_unknown_employment():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "freelancer", 800)


# Eligibility age branches
def test_age_below_minimum():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_maximum():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_age_within_range():
    assert is_eligible(30, 50000, "salaried", 800) is True


# Income branches for both employment types
def test_salaried_income_below_minimum():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_self_employed_income_below_minimum():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_self_employed_income_eligible():
    assert is_eligible(30, 50000, "self_employed", 800) is True


# Credit eligibility branches
def test_poor_credit_score_rejected():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_good_credit_score_accepted():
    assert is_eligible(30, 50000, "salaried", 700) is True


# Interest rate branches
def test_interest_excellent_salaried_no_collateral():
    assert interest_rate(800, "salaried", False) == 8


def test_interest_good_salaried_with_collateral():
    assert interest_rate(700, "salaried", True) == 8


def test_interest_fair_self_employed_no_collateral():
    assert interest_rate(600, "self_employed", False) == 14


def test_interest_poor_self_employed_with_collateral():
    assert interest_rate(400, "self_employed", True) == 12

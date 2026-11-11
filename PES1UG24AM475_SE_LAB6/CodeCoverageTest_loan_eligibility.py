
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate


def test_credit_band_categories():
    assert credit_band(800) == "excellent"
    assert credit_band(700) == "good"
    assert credit_band(600) == "fair"
    assert credit_band(400) == "poor"


def test_credit_band_invalid_score():
    with pytest.raises(ValueError, match="invalid score"):
        credit_band(200)


def test_eligibility_unknown_employment():
    with pytest.raises(ValueError, match="unknown employment"):
        is_eligible(30, 50000, "unemployed", 800)


def test_eligibility_age_rejection():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_eligibility_income_rejection():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_eligibility_poor_credit_rejection():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_eligibility_approved():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_interest_rate_excellent():
    assert interest_rate(800, "salaried", False) == 8


def test_interest_rate_good():
    assert interest_rate(700, "salaried", False) == 10


def test_interest_rate_fair_with_collateral():
    assert interest_rate(600, "self_employed", True) == 12

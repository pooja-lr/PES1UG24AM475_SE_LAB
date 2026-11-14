
from hypothesis import given, strategies as st
from loan_eligibility import parse_income, monthly_emi, pan_category
import math


# 1. Fuzz testing parse_income()
@given(st.text() | st.none())
def test_parse_income_no_crash(s):
    result = parse_income(s)
    assert result is None or (
        isinstance(result, int) and result >= 0
    )


def test_parse_income_valid():
    assert parse_income("50,000") == 50000
    assert parse_income("50000") == 50000


def test_parse_income_invalid():
    assert parse_income("abc") is None
    assert parse_income(None) is None
    assert parse_income("50,00") is None


# 2. Fuzz testing monthly_emi()
@given(st.text() | st.none())
def test_monthly_emi_no_crash(s):
    result = monthly_emi(s)
    assert result is None or (
        isinstance(result, (int, float))
        and math.isfinite(result)
        and result >= 0
    )


def test_monthly_emi_valid():
    assert monthly_emi("500000,10,5") == 10623.52
    assert monthly_emi("120000,0,1") == 10000.00


def test_monthly_emi_invalid():
    assert monthly_emi("abc") is None
    assert monthly_emi(None) is None
    assert monthly_emi("500000,10,0") is None


# 3. Fuzz testing pan_category()
@given(st.text() | st.none())
def test_pan_category_no_crash(s):
    result = pan_category(s)
    assert result is None or result in {
        "Individual", "Company", "HUF", "Firm"
    }


def test_pan_category_valid():
    assert pan_category("ABCPE1234F") == "Individual"
    assert pan_category("ABCCE1234F") == "Company"
def test_pan_category_invalid():
    assert pan_category("ABC") is None
    assert pan_category(None) is None
    assert pan_category("ABCDE1234!") is None

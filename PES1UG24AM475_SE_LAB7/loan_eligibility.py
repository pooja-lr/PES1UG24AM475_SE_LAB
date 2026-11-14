
import re

CATEGORIES = {
    "P": "Individual",
    "C": "Company",
    "H": "HUF",
    "F": "Firm"
}


def parse_income(income):
    """Parse monthly income safely."""
    if not isinstance(income, str):
        return None

    income = income.strip()

    # Accept plain digits or correctly grouped comma-separated digits
    if not re.fullmatch(r"(?:\d+|\d{1,3}(?:,\d{3})+)", income):
        return None

    try:
        value = int(income.replace(",", ""))
        return value if value >= 0 else None
    except (ValueError, OverflowError):
        return None


def monthly_emi(details):
    """Calculate monthly EMI safely."""
    if not isinstance(details, str):
        return None

    parts = details.split(",")

    if len(parts) != 3:
        return None

    try:
        principal, rate, years = [int(part.strip()) for part in parts]

        if principal <= 0 or rate < 0 or years <= 0:
            return None

        n = years * 12
        r = rate / 1200

        # Handle zero-interest loans separately
        if r == 0:
            return round(principal / n, 2)

        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

        return round(emi, 2)

    except (ValueError, TypeError, OverflowError, ZeroDivisionError):
        return None


def pan_category(pan):
    """Identify PAN category safely."""
    if not isinstance(pan, str):
        return None

    pan = pan.strip().upper()

    # Validate the complete PAN format
    if not re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan):
        return None

    return CATEGORIES.get(pan[3])


def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    result = parse_income(user_input)
    print("Income:", result)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    result = monthly_emi(user_input)
    print("Monthly EMI:", result)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    result = pan_category(user_input)
    print("PAN Category:", result)


if __name__ == "__main__":
    main()

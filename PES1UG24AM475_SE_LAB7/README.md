
# PES1UG24AM475 - Lab 7
## Fuzz Testing for Input Validation Bugs

### Objective
To identify and fix input validation bugs using property-based fuzz testing with the Hypothesis library.

### Technologies Used
- Python 3.13
- Hypothesis
- Pytest

### Files
| File | Description |
|---|---|
| loan_eligibility.py | Fixed loan eligibility application |
| test_loan_eligibility.py | Hypothesis fuzz tests and validation tests |
| Lab7_Report.pdf | Lab execution screenshots and observations |

### Functions Tested
1. parse_income() - Validates and parses monthly income.
2. monthly_emi() - Calculates monthly loan EMI safely.
3. pan_category() - Validates PAN input and identifies its category.

### Bugs Identified
- Invalid income formats and non-string inputs.
- Invalid EMI parameters, missing values and division by zero.
- Invalid PAN formats and unsupported category characters.

### Fixes Implemented
- Added defensive input validation.
- Added exception handling.
- Added support for zero-interest EMI calculations.
- Added PAN format validation.
- Invalid inputs return None instead of crashing.

### Testing
Hypothesis was used to generate unexpected inputs automatically.

Pytest was used to execute the test suite.

Command:
python -m pytest test_loan_eligibility.py -v

### Final Result
9 tests passed successfully.

All three functions were tested using fuzz testing and additional valid and invalid input test cases.

### Conclusion
Fuzz testing using Hypothesis helped identify input validation weaknesses and improve the robustness of the loan eligibility application.

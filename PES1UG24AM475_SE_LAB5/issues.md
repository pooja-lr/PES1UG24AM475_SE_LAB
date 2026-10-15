\# Lab 5: Static Code Analysis — Issues Log



\*\*Repository:\*\* `L5\_52\_course\_enrollment\_system`  

\*\*Python file:\*\* `course\_enrollment\_system.py`  

\*\*Tools used:\*\* Pylint, Bandit, Flake8



\## 1. Issues Identified and Fixes



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---:|---|---|

| Unsafe `eval()` usage | Security — Medium | 47 | Evaluates a discount expression using `eval()`, which can execute arbitrary Python code. | Replace `eval()` with a safe calculation approach, such as validated numeric inputs and explicit arithmetic. |

| Weak MD5 hashing | Security — High | 52 | Uses MD5 to generate student hashes. MD5 is unsuitable for security-sensitive hashing. | Use SHA-256 for a non-security identifier, or a suitable password-hashing algorithm if storing passwords. |

| Insecure random OTP generation | Security — Low | 56 | Uses `random.randint()` to generate enrollment OTPs. The standard random generator is not designed for security-sensitive tokens. | Use `secrets.randbelow()` or `secrets.randbelow(9000) + 1000` to generate a four-digit OTP. |

| Shell command execution | Security — High | 63 | Uses `os.system()` to execute a command containing a filename, potentially allowing command injection. | Remove the shell command and use `print()` to display the export location. |

| Hardcoded registrar token | Security — Low | 75 | Stores the registrar authentication token directly in the source code. | Remove the hardcoded token and retrieve it through a secure configuration mechanism or environment variable. |

| Exception silently ignored | Reliability / Security | 31–32 | Uses a bare `except` followed by `pass`, hiding failures when dropping a course. | Catch the specific expected exception and handle or report the error appropriately. |

| Mutable default argument | Code quality / Bug risk | 15 | Uses a list as a default function argument, which can be shared across calls and retain state. | Change the default to `None` and initialize a new list inside the function. |

| Global variable modification | Code quality | 16 | Uses the `global` statement to modify `total\_tuition`, creating unnecessary global-state dependence. | Return the updated tuition value or encapsulate the state in an appropriate data structure. |

| Unused import | Code quality | 4 | Imports `math` but does not use it. | Remove the unused import. |

| Unused variable `lab\_fee` | Code quality | 36 | Assigns a value to `lab\_fee` without using it. | Remove the variable or use it if it is required for course-status logic. |

| Unused variable `base\_fee` | Code quality | 46 | Assigns a course fee to `base\_fee` but does not use it. | Use the value in the tuition calculation or remove the unnecessary assignment. |

| Unused variable `cid` | Code quality | 68 | Defines a loop variable that is not used in the loop body. | Replace it with `\_` if the value is intentionally unused, or use it in the logic. |

| Non-standard function names | Maintainability | 15, 27, 35, 45, 51, 55, 59, 66 | Several function names use camelCase rather than the recommended Python snake\_case convention. | Rename functions to `enroll\_student`, `drop\_course`, `check\_course\_status`, `calculate\_scholarship\_tuition`, `generate\_student\_hash`, `generate\_enrollment\_otp`, `export\_course\_roster`, and `get\_open\_courses\_summary`. Update all call sites. |

| Missing module docstring | Documentation | 1 | The Python module does not contain a module-level docstring. | Add a short docstring describing the course enrollment system. |

| Missing function docstrings | Documentation | 15, 27, 35, 45, 51, 55, 59, 66 | Functions lack docstrings explaining their purpose. | Add concise docstrings describing each function's purpose, parameters, and return value where appropriate. |

| Line too long | Formatting | 7–9, 15, 23, 79 | Several lines exceed Flake8's 79-character limit. Line 23 is also flagged by Pylint for exceeding its 100-character limit. | Break long statements across multiple lines while preserving their behavior. |

| Missing final newline | Formatting | End of file (line 87 in Pylint; line 87 in Flake8) | The file does not end with a newline character. | Add a newline at the end of the Python file. |

| String formatting could use an f-string | Maintainability | 23 | Pylint reports that a regular string-formatting expression could use an f-string. | Replace the expression with an f-string where appropriate. |

| Comparison with `None` | Code quality | 37 | Compares `courses.get(course\_id)` with `None` using `==`. | Use `is None` for the comparison. |

| Unnecessary conditional return | Code quality | 39 | A conditional expression returns Boolean values that can be simplified. | Return the Boolean condition directly if it preserves the original logic. |

| Unnecessary `else` after `return` | Code quality | 39 | Contains an `else` branch after a preceding `return`. | Remove the unnecessary `else` and de-indent the remaining code. |

| File opened without encoding | Reliability | 60 | Opens a file without explicitly specifying its encoding. | Specify an appropriate encoding, such as `encoding="utf-8"`. |

| File resource not managed with a context manager | Reliability | 60–63 | Opens a file and closes it manually, which may leave the file open if an error occurs. | Use a `with open(...) as file:` block to manage the file resource safely. |

| Parameter shadows an outer-scope name | Maintainability | 66 | The `courses` parameter in `getOpenCoursesSummary()` reuses the name of an outer-scope variable. | Rename the parameter to avoid ambiguity, or refactor the function to make its data dependencies clear. |



\## 2. Before-Fix Analysis Summary



| Tool | Findings from the report |

|---|---|

| Pylint | Score: \*\*4.00/10\*\* |

| Bandit | \*\*6 potential issues:\*\* 2 High, 1 Medium, 3 Low |

| Flake8 | \*\*12 reported violations\*\* |



\## 3. Planned Fixes



1\. \*\*Bandit:\*\* Address all reported security findings, including unsafe evaluation, MD5 hashing, insecure OTP generation, shell execution, the hardcoded token, and silent exception handling.

2\. \*\*Pylint:\*\* Improve naming conventions, documentation, exception handling, variable usage, function design, and other code-quality issues. Aim for a score above 9.5/10.

3\. \*\*Flake8:\*\* Fix all reported formatting and style violations, including long lines, unused imports and variables, bare exception handling, comparisons with `None`, and the missing final newline.



\## 4. Verification After Fixes



After making the changes, rerun Pylint, Bandit, and Flake8 and save the reports as:



\- `pylint\_after.txt`

\- `bandit\_after.txt`

\- `flake8\_after.txt`



Compare the before-and-after reports to verify that the identified findings have been resolved. Test the course enrollment program to ensure that its functionality remains correct.



\## 5. Git Commit Record



| Commit | Purpose | Commit message |

|---|---|---|

| 1 | Security fixes | `Fix security issues identified by Bandit` |

| 2 | Code-quality fixes | `Fix code quality issues identified by Pylint` |

| 3 | Formatting fixes | `Fix formatting issues identified by Flake8` |



\*\*Note:\*\* This document records the findings from the original reports. The fixes and post-fix results must be verified after implementation. Some findings overlap across tools, so the total number of messages is not the same as the number of unique underlying issues.




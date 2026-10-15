\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis, and why is it important?



Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, and coding standard violations. It helps improve software quality, security, readability, and maintainability. In this lab, Pylint, Bandit, and Flake8 were used to analyze the course enrollment system and identify issues before deployment.



\## 2. What issues did you identify and fix using Pylint, Bandit, and Flake8?



Pylint identified code-quality issues such as missing docstrings, inconsistent function naming, a mutable default argument, unused variables, and unnecessary global-state usage. Bandit identified security concerns involving unsafe `eval()`, weak MD5 hashing, insecure random OTP generation, shell-command execution, and a hardcoded registrar token. Flake8 identified formatting violations, including excessive or missing blank lines, whitespace on blank lines, and line-length issues. These findings were addressed through safer implementations, improved naming and documentation, and formatting corrections.



\## 3. How did the static analysis tools improve the course enrollment system?



The tools helped make the code safer, cleaner, and easier to maintain. The scholarship calculation was changed to use a validated numeric discount rate instead of `eval()`. SHA-256 replaced MD5 for generating student identifier hashes, and the OTP generator was changed to use Python's `secrets` module. Shell-command execution and the hardcoded registrar token were removed. The mutable default argument and unnecessary global-state modification were also addressed. Finally, formatting and documentation were improved.



\## 4. What did you learn from this lab?



I learned that different static analysis tools detect different categories of problems. Pylint focuses on code quality and programming practices, Bandit focuses on security vulnerabilities, and Flake8 checks Python style and formatting. Using all three tools provides broader coverage than relying on only one. I also learned that fixing reported issues must be followed by rerunning the tools and testing the program to verify that the changes are effective and that the original functionality remains intact.




![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/Python-3.13%2B-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Testing workflow](https://github.com/CSC510-Software-Engineering-Fall-2024/HW-1/actions/workflows/test.yml/badge.svg) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint) ![Radon](https://img.shields.io/github/workflow/status/your-repo/radon?label=radon&logo=radon) ![Bandit](https://img.shields.io/github/workflow/status/your-repo/bandit?label=bandit&logo=bandit) ![Pyflakes](https://img.shields.io/github/workflow/status/your-repo/pyflakes?label=pyflakes&logo=pyflakes) ![Pyright](https://img.shields.io/github/workflow/status/your-repo/pyright?label=pyright&logo=pyright)








# CSC 510 - Homework 2

## Overview

This repository contains the solution to **Homework 2**, which focuses on debugging, static analysis, and test-driven development.

The main objectives are:
1. Executing static analysis tools and auto-formatting on the provided code.
2. Debugging and fixing the `mergeSort` implementation in `hw2_debugging.py`.
3. Writing and running test cases using `pytest`.
4. Automating static analysis and tests with continuous integration.

## Instructions

### 1. Download and Unzip the Assignment Files
- Download `hw2.zip` and unzip it to access the code files.

### 2. Static Analysis and Auto-Formatting
- Run **AutoPep8** to auto-format the Python code.
- Use two static analysis tools (e.g., **pylint**, **pyflake**, **pyright**, **Autopep8**, **Bandit**, **Radon**)

### 3. Debugging the Code
- The file `hw2_debugging.py` contains an implementation of the **mergeSort** algorithm, which relies on helper methods located in `rand.py`.
- The current implementation is failing. Analyze the code, fix any issues based on the static analysis recommendations, and ensure the `mergeSort` function works as expected.

### 4. Re-run Static Analysis
- After making code changes, re-run the static analysis tools to confirm no issues remain.
- Save the output (trace files) from the static analysis tools in a folder called `post_traces`.

### 5. Commit Changes
- Once the `mergeSort` implementation is fixed and the code passes all checks:
  - Commit your fixed version of `hw2_debugging.py` to your repository.
  - You can choose to commit it to your existing **HW1** repository or create a separate **HW2** repository.

### 6. Write Test Cases
- Write **three test cases** to verify the correctness of your `mergeSort` implementation.
- The tests should be executable using **pytest**.

### 7. Configure Continuous Integration
- Configure **AutoPep8** and the two static analysis tools to run on every commit in your HW2 repository.
- Add badges to your repository for each of the static analysis tools.

### 8. Continuous Testing
- Configure your new `merge_sort` tests to run on every commit, ensuring that no regression can occur without a test failing.

### 9. Submission
- Submit a PDF document containing the static analysis traces and a link to your HW2 repository to Moodle.

## Repository Structure
```bash
HW2/
│
├── hw2_debugging.py           # The main file containing the mergeSort implementation
├── rand.py                    # Helper methods used in mergeSort
├── post_traces/               # Folder containing the traces after re-running the static analysis tools
│   ├── pylint_trace.txt
│   ├── Radon_trace.txt
│   └── ...
├── tests/                     # Folder containing test cases for mergeSort
│   ├── test_merge_sort.py
│   └── ...
└── README.md
└── LICENSE.txt
```
## Contact

For any questions or issues regarding this assignment, feel free to reach out:

- **Email**: [pemacnic@ncsu.edu](oemacnic@ncsu.edu)


# 📘 Assignment: Python Unit Testing & Quality Assurance

## 🎯 Objective

Learn to write robust, maintainable code by mastering unit testing with pytest. You'll write tests first, implement code to pass them, and measure code quality through coverage reports.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests with pytest

#### Description
Create a test file using pytest that validates a simple Python module. Learn test structure, assertions, and running test suites. Implement the module code to pass all tests.

#### Requirements
Completed program should:

- Create a `test_calculator.py` file with pytest test cases
- Write tests for basic arithmetic operations (add, subtract, multiply, divide)
- Use assertions to validate expected vs actual results
- Handle edge cases like division by zero
- Implement a `calculator.py` module that passes all tests
- Run tests successfully with `pytest` and view detailed output

### 🛠️ Implement Fixtures, Mocking, and Test-Driven Development

#### Description
Apply advanced testing patterns: use fixtures for test setup, mock external dependencies, and practice Test-Driven Development (TDD) by writing tests before implementation.

#### Requirements
Completed program should:

- Create reusable fixtures for common test data
- Mock external API calls or file I/O operations
- Follow TDD: write failing tests first, then implement code
- Test both success and failure scenarios
- Use parameterized tests to reduce code duplication
- Ensure clean, organized test structure

### 🛠️ Measure and Report Code Coverage (Stretch Goal)

#### Description
Use pytest-cov to measure code coverage and generate coverage reports. Achieve high coverage while maintaining meaningful tests.

#### Requirements
Completed program should:

- Install and configure pytest-cov
- Generate HTML coverage reports
- Achieve at least 90% code coverage
- Identify untested code paths
- Write additional tests to improve coverage
- Understand coverage limitations (coverage ≠ quality)

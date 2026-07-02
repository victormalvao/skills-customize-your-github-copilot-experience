"""
test_calculator.py - Unit tests for calculator module
Run with: pytest test_calculator.py -v
"""

import pytest
from calculator import add, subtract, multiply, divide, factorial, is_prime

class TestBasicOperations:
    """Test basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_subtract(self):
        assert subtract(10, 3) == 7
        assert subtract(5, 5) == 0
        assert subtract(0, 5) == -5
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-3, 4) == -12
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Divide by zero should raise ValueError."""
        with pytest.raises(ValueError):
            divide(10, 0)

class TestFactorial:
    """Test factorial function."""
    
    def test_factorial_base_cases(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
    
    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(6) == 720
    
    def test_factorial_negative(self):
        """Factorial of negative should raise ValueError."""
        with pytest.raises(ValueError):
            factorial(-1)

class TestPrime:
    """Test prime number checker."""
    
    def test_prime_numbers(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
    
    def test_non_prime(self):
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(6) == False
    
    def test_large_primes(self):
        assert is_prime(97) == True
        assert is_prime(100) == False

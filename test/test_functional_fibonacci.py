from test_fibonacci import BaseFibonacciTests
from src.functional_fibonacci import functional_fibonacci

class FunctionalFibonacciTests(BaseFibonacciTests):
    def get_fibonacci_function(self):
        return functional_fibonacci

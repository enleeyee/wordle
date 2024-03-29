from test_fibonacci import BaseFibonacciTests
from src.imperative_fibonacci import imperative_fibonacci

class ImperativeFibonacciTests(BaseFibonacciTests):
    def get_fibonacci_function(self):
        return imperative_fibonacci

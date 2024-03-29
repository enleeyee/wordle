from itertools import islice
from .fibonacci import validate_non_negative

def fibonacci_generator(position):
    previous_number, current_number = 1, 1
    
    for i in range(position):
        yield previous_number
        previous_number, current_number = current_number, previous_number + current_number

def functional_fibonacci(position):
    
    validate_non_negative(position)

    return next(islice(fibonacci_generator(position + 1), position, None))

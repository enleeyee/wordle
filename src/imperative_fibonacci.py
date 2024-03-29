from .fibonacci import validate_non_negative

def imperative_fibonacci(position):

    validate_non_negative(position)

    previous_number, current_number = 1, 1

    for i in range(0, position):
        previous_number, current_number = current_number, previous_number + current_number

    return previous_number

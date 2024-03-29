def validate_non_negative(position):
    if position < 0:
        raise ValueError("The number should be non-negative")
    
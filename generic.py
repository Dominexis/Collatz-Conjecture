def product(factors: list[int]) -> int:
    """Takes the product of all the provided factors."""
    output = 1
    for factor in factors:
        output *= factor
    return output
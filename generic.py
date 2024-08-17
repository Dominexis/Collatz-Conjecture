def product(factors: list[int]) -> int:
    """Takes the product of all the provided factors."""
    output = 1
    for factor in factors:
        output *= factor
    return output



def prime_factors(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    factor = 2

    def add_factor():
        if factor in factors:
            factors[factor] += 1
        else:
            factors[factor] = 1

    while factor*factor <= value:
        while value%factor == 0:
            add_factor()
            value //= factor
        factor += 1
    if value > 1:
        factor = value
        add_factor()
    
    return factors
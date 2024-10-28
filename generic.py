from pathlib import Path



PROGRAM_PATH = Path(__file__).parent



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



def sort_dict(dictionary: dict) -> dict:
    """
    Sorts the keys of the provided dictionary object.
    """

    keys = list(dictionary.keys())
    keys.sort()
    output = {}
    for key in keys:
        output[key] = dictionary[key]
    return output



def is_int(value: str) -> bool:
    return value[1 if value.startswith("-") else 0:].isnumeric()
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



def convert_steps_to_powers(steps: str) -> list[int]:
    """
    Converts a steps string consisting of up and down steps (denoted by "u" and "d") to a sequence of powers of 2.
    """

    powers: list[int] = []
    for step in steps:
        if step in ["u", "U"]:
            powers.append(2)
        if step in ["d", "D"]:
            if len(powers) > 0:
                powers[-1] *= 2
            else:
                # This case shouldn't happen with naturally-occurring sequences, but is here to prevent errors
                powers.append(2)

    return powers



def convert_powers_to_steps(powers: list[int]) -> str:
    """
    Converts a sequence of powers of 2 to a steps string consisting of up and down steps (denoted by "u" and "d").
    """

    steps = ""
    for power in powers:
        steps += "u"
        while True:
            power //= 2
            if power <= 1:
                break
            steps += "d"
    
    return steps



def convert_sequence_to_powers(sequence: list[int]) -> list[int]:
    powers: list[int] = []

    for value in sequence:
        if value%2:
            powers.append(1)
        else:
            if len(powers) > 0:
                powers[-1] *= 2
            else:
                powers.append(2)

    if powers[-1] == 1:
        powers.pop()

    return powers



def extract_sequence_from_prompt(sequence_prompt: str) -> list[int]:
    sequence_prompt = sequence_prompt.strip()

    if sequence_prompt.startswith("["):
        sequence_prompt = sequence_prompt[1:-1]
        sequence: list[int] = []
        for value in sequence_prompt.split(","):
            value = value.strip()
            if not value.isnumeric():
                print(f"ERROR: {value} is not numeric!")
                raise Exception
            sequence.append(int(value))

    else:
        sequence = convert_steps_to_powers(sequence_prompt)

    return sequence
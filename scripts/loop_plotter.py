from typing import TypedDict, cast
import powers
import generic
import loop_formula
import math



class LoopInfo(TypedDict):
    denominator: int
    denominators: list[int]
    denominator_factors: dict[int, int]
    numerator_gcds: dict[int, int]
    numerators: dict[int, int]

class PlotInclusions(TypedDict):
    denominator: bool
    denominators: bool
    denominator_factors: bool
    numerator_gcds: bool
    numerators: bool



def get_loop_info(length: int, weight: int, include: PlotInclusions) -> LoopInfo | None:
    """
    Compiles various pieces of information about all the loops
    with `length` steps and `weight` powers of 2 distributed throughout the list.

    `weight` must be equal to or greater than `length` to produce a defined value.

    The include parameter can be used to customize the output data.
    """

    if length > weight:
        return
    
    # Print current status
    print(f"W {weight}, L {length}                          ", end="\r")
    
    # Compute denominator
    denominator = powers.POWERS_OF_2[weight] - powers.POWERS_OF_3[length]
    denominator_factors = generic.prime_factors(abs(denominator)) if include["denominator_factors"] else {}

    # Compute numerators
    numerators: dict[int, int] = {}
    if include["numerators"] or include["numerator_gcds"] or include["denominators"]:
        get_numerators(numerators, denominator, [], length, weight, 1, 0)

    # Compute numerator GCDs
    numerator_gcds: dict[int, int] = {}
    if include["numerator_gcds"]:
        for numerator in numerators:
            gcd = numerators[numerator]
            if gcd in numerator_gcds:
                numerator_gcds[gcd] += 1
            else:
                numerator_gcds[gcd] = 1

    # Compute denominator list
    denominators: list[int] = []
    if include["denominators"]:
        for numerator in numerators:
            gcd = numerators[numerator]
            simplified_denominator = abs(denominator // gcd)
            if simplified_denominator not in denominators:
                denominators.append(simplified_denominator)
        denominators.sort()

    # Return output
    output = cast(LoopInfo, {})
    if include["denominator"]:
        output["denominator"] = denominator
    if include["denominators"]:
        output["denominators"] = denominators
    if include["denominator_factors"]:
        output["denominator_factors"] = denominator_factors
    if include["numerators"]:
        output["numerators"] = numerators
    if include["numerator_gcds"]:
        output["numerator_gcds"] = generic.sort_dict(numerator_gcds)

    return output



def get_numerators(numerators: dict[int, int], denominator: int, sequence: list[int], length: int, weight: int, current_length: int, current_weight: int):
    """
    Iterates through all possible sequences given the length and weight. Repeating sequences are ignored.
    The base numerators of the loops are logged, as well as their greatest common divisor with the base denominator.
    """

    sequence.append(1)
    if length == current_length:
        sequence[-1] = weight - current_weight
        if not does_sequence_repeat(sequence):
            numerator = loop_formula.get_loop_numerator([powers.POWERS_OF_2[power] for power in sequence])
            numerators[numerator] = math.gcd(numerator, denominator)

    else:
        for power in range(1, (weight - current_weight) - (length - current_length) + 1):
            sequence[-1] = power
            get_numerators(numerators, denominator, sequence.copy(), length, weight, current_length + 1, current_weight + power)



def does_sequence_repeat(sequence: list[int]) -> bool:
    """
    Determines whether the given sequence repeats itself.
    """

    length = len(sequence)
    for section in range(1, length//2 + 1):
        if length%section != 0:
            continue
        for i in range(length):
            if sequence[i] != sequence[i%section]:
                break
        else:
            return True
    return False



def plot_loops(max_length: int, max_weight: int, include: PlotInclusions) -> dict[tuple[int, int], LoopInfo]:
    """
    Compiles the data of loops of many lengths and weights in a grid.

    The include parameter can be used to customize the output data.
    """

    plot: dict[tuple[int, int], LoopInfo] = {}

    for weight in range(1, max_weight + 1):
        for length in range(1, max_length + 1):
            loop = get_loop_info(length, weight, include)
            if loop:
                plot[(length, weight)] = loop

    return plot
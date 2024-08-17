from typing import TypedDict
import powers
import generic



class LoopInfo(TypedDict):
    denominator: int
    denominator_factors: dict[int, int]



def get_loop_info(length: int, weight: int) -> LoopInfo | None:
    """
    Compiles various pieces of information about all the loops
    with `length` steps and `weight` powers of 2 distributed throughout the list.

    `weight` must be equal to or greater than `length` to produce a defined value.
    """

    if length > weight:
        return
    
    denominator = powers.POWERS_OF_2[weight] - powers.POWERS_OF_3[length]
    denominator_factors = generic.prime_factors(abs(denominator))

    return {
        "denominator": denominator,
        "denominator_factors": denominator_factors,
    }



def plot_loops(max_length: int, max_weight: int) -> dict[tuple[int, int], LoopInfo]:
    """
    Compiles the data of loops of many lengths and weights in a grid.
    """

    plot: dict[tuple[int, int], LoopInfo] = {}

    for weight in range(1, max_weight + 1):
        for length in range(1, max_length + 1):
            loop = get_loop_info(length, weight)
            if loop:
                plot[(length, weight)] = loop

    return plot



def print_plot(plot: dict[tuple[int, int], LoopInfo]) -> str:
    entries: list[str] = []

    for key in plot:
        loop = plot[key]
        entries.append(f"    {key}: {str(loop).replace("'", '"')}")
    
    return f"{{\n{",\n".join(entries)}\n}}"
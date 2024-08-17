import generic
import powers



def get_loop(sequence: list[int]) -> tuple[int, int]:
    """
    Computes the Collatz Loop Formula on the provided sequence.

    The sequence represents the powers of 2 of the division step of the Collatz sequence, uniquely encoding the loop.

    The result is the number encoded as a numerator/denominator pair such that if you take the Collatz sequence of it,
    the division steps will follow the provided sequence, and it will return to itself after the sequence completes.
    """
    return (get_loop_numerator(sequence), get_loop_denominator(sequence))



def get_loop_numerator(sequence: list[int]) -> int:
    """
    Computes the numerator of the Collatz Loop Formula.

    It is the sum of terms where each term is the product of some power of 2 and some power of 3.

    The first term is always a power of 3, and the last term is always a power of 2,
    thus it will never be divisible by 2 or 3.
    """
    length = len(sequence)
    return sum([
        powers.POWERS_OF_3[length - i - 1] *
        generic.product(sequence[:i])
        for i in range(length)
    ])



def get_loop_denominator(sequence: list[int]) -> int:
    """
    Computes the denominator of the Collatz Loop Formula.

    It is the product of the sequence minus 3 to the power of the length of the sequence.

    Because it is always a power of 2 minus a power of 3, it will never be divisible by 2 or 3.
    """
    return generic.product(sequence) - powers.POWERS_OF_3[len(sequence)]
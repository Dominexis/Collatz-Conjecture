import powers



def invert_numerator(numerator: int, length: int) -> list[int] | None:
    """
    Computes the sequence of powers of 2 that produces the given numerator in the loop formula.

    It works by iterating through the powers of 3, starting from the given length and working down, subtracting them from the numerator, then dividing it by 2 as many times as it can.

    The final term in the sequence does not affect the output, and so is omitted from the return value.
    """

    if numerator%2 == 0 or numerator%3 == 0:
        return None

    sequence: list[int] = []
    
    for i in range(length-1, -1, -1):
        numerator -= powers.POWERS_OF_3[i]
        if i == 0:
            break
        if numerator <= 0:
            return None
        step = 0
        while True:
            if numerator%2 == 0:
                numerator //= 2
                step += 1
            else:
                break
        sequence.append(powers.POWERS_OF_2[step])
        
    if numerator == 0:
        return sequence
    return None



def invert_numerators(numerator: int) -> dict[int, list[int]]:
    """
    Computes all possible sequences of powers of 2 that produce the given numerator in the loop formula.

    Because the numerator only uses addition, there is a minimum possible numerator which can be produced by a given length. Thus, only lengths which can produce numbers the size of the given numerator need to be checked.

    The minimum length is produced with a sequence of only 2's. Such a sequence returns -1 in the loop formula. The minimum length can thus be computed with the negative denominator, which is only two terms.
    """

    sequences: dict[int, list[int]] = {}
    length = 1
    while True:
        sequence = invert_numerator(numerator, length)
        if sequence is not None:
            sequences[length] = sequence
        length += 1
        if powers.POWERS_OF_3[length] - powers.POWERS_OF_2[length] > numerator:
            break
    return sequences



def prompt():
    while True:
        numerator = input("Numerator (leave blank to exit): ")
        if not numerator:
            return
        if not numerator.isnumeric():
            continue

        sequences = invert_numerators(int(numerator))
        print(f"Sequences: {sequences}\nNumber of sequences: {len(sequences)}\n")



if __name__ == "__main__":
    prompt()
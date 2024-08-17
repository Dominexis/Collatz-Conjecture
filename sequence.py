def collatz_sequence(value: int, denominator: int = 1, steps: int = 0) -> list[int]:
    """
    Runs the Collatz sequence for the provided number of steps (default is until a loop is reached)
    starting from `value`.

    A denominator may be specified to iterate over rational numbers. Make sure `value` and `denominator` are coprime.
    """
    sequence: list[int] = [value]
    while True:
        # Multiply by 3 and add denominator if odd
        if value%2:
            value = value*3 + denominator
        # Divide by 2 if even
        else:
            value //= 2

        # Add value to list if not in it already
        if value not in sequence:
            sequence.append(value)
        else:
            break

        # Break if steps expire (go forever if 0 or negative).
        steps -= 1
        if steps == 0:
            break

    return sequence
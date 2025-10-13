import generic
import random



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



def prompt():
    while True:
        value = input("Starting value (leave blank to exit): ")
        if not value:
            return
        if value.startswith("l"):
            new_value = ""
            for i in range(int(value[1:])):
                new_value += str(random.randint(0, 9))
            value = new_value
        if not generic.is_int(value):
            print(f"ERROR: {value} is not numeric!")
            continue

        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not generic.is_int(denominator):
            print(f"ERROR: {denominator} is not numeric!")
            continue

        sequence = collatz_sequence(int(value), int(denominator))
        print(f"Sequence: {sequence}\nSteps: {generic.convert_sequence_to_powers(sequence)}\nExponents: {generic.convert_powers_to_exponents(generic.convert_sequence_to_powers(sequence))}\nSequence length: {len(sequence)}\n")



if __name__ == "__main__":
    prompt()
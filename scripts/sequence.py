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
        random_number = None
        if value.startswith("l"):
            random_number = 0
            place = 1
            for i in range(int(value[1:])):
                random_number += random.randint(0, 9)*place
                place *= 10
        elif not generic.is_int(value):
            print(f"ERROR: {value} is not numeric!")
            continue
        if random_number is not None:
            value = random_number
        else:
            value = int(value)

        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not generic.is_int(denominator):
            print(f"ERROR: {denominator} is not numeric!")
            continue

        sequence = collatz_sequence(value, int(denominator))
        print(f"Sequence: {sequence}\nSteps: {generic.convert_sequence_to_powers(sequence)}\nExponents: {generic.convert_powers_to_exponents(generic.convert_sequence_to_powers(sequence))}\nSequence length: {len(sequence)}\nStarting value: {value}\nEnding value: {sequence[-1]}\n")



if __name__ == "__main__":
    prompt()
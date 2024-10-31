import math
import generic
import powers
import loop_formula



def invert_sequence(sequence: list[int] | str, ending: tuple[int, int] = (1, 1)) -> tuple[int, int]:
    """
    Computes the Collatz sequence inverter formula on the provided sequence.

    The sequence represents the powers of 2 of the division step of the Collatz sequence, uniquely encoding the loop.
    It may alternatively be a string of u's and d's representing up steps and down steps.

    The result is the number encoded as a numerator/denominator pair such that if you take the Collatz sequence of it,
    the division steps will follow the provided sequence,
    and it will land on `ending`, which is also a numerator/denominator pair, at the end of the sequence.
    """

    if isinstance(sequence, str):
        sequence = generic.convert_steps_to_powers(sequence)

    numerator = ending[0]*math.prod(sequence) - ending[1]*loop_formula.get_loop_numerator(sequence)
    denominator = ending[1]*powers.POWERS_OF_3[len(sequence)]

    return (numerator, denominator)



def prompt():
    while True:
        sequence_prompt = input("Sequence (leave blank to exit): ")
        if not sequence_prompt:
            return
        
        sequence_prompt = sequence_prompt.strip()

        if sequence_prompt.startswith("["):
            sequence_prompt = sequence_prompt[1:-1]
            sequence: list[int] = []
            for value in sequence_prompt.split(","):
                value = value.strip()
                if not value.isnumeric():
                    print(f"ERROR: {value} is not numeric!")
                    continue
                sequence.append(int(value))

        else:
            sequence = generic.convert_steps_to_powers(sequence_prompt)

        ending_prompt = input("Ending (leave blank to exit): ")
        if not ending_prompt:
            return
        
        ending_parts = ending_prompt.split("/")
        ending_parts = ending_parts[:min(2, len(ending_parts))]
        invalid_ending = False
        for i in range(len(ending_parts)):
            ending_parts[i] = ending_parts[i].strip()
            if not generic.is_int(ending_parts[i]):
                print(f"ERROR: {ending_parts[i]} is not numeric!")
                invalid_ending = True
                break
        if invalid_ending:
            continue
        
        ending = (int(ending_parts[0]), int(ending_parts[1]) if len(ending_parts) > 1 else 1)
        if ending[1] < 0:
            ending = (-ending[0], -ending[1])

        output = invert_sequence(sequence, ending)
        gcd = math.gcd(output[0], output[1])
        output = (output[0]//gcd, output[1]//gcd)
        print(f"Numerator: {output[0]}\nDenominator: {output[1]}\n")



if __name__ == "__main__":
    prompt()
import powers
import loop_formula
import trailing_bit_generator



NORMAL_SEQUENCE: list[int] = []
for i in range(4096):
    for bit in format(i, "b"):
        NORMAL_SEQUENCE.extend([2] if bit == "0" else [4])



def large_division(ratio: tuple[int, int], digits: int) -> str:
    quotient = str(ratio[0]*powers.POWERS_OF_10[digits] // ratio[1])
    quotient = "0"*(digits - len(quotient)) + quotient
    quotient = quotient[:-digits] + "." + quotient[-digits:]
    for i in range(len(quotient)):
        if quotient.endswith("0"):
            quotient = quotient[:-1]
        else:
            break
    return quotient



def expanding_powers():
    for i in range(100):
        result = loop_formula.get_loop(powers.POWERS_OF_2[1:i+2])
        # print(f"[2 ... {powers.POWERS_OF_2[i+1]}]: {large_division(result, 100)}, {result[0]}/{result[1]}")
        print(f"[2 ... {powers.POWERS_OF_2[i+1]}]: {large_division(result, 100)}")



def normal_of_2_and_4_trailing_bits():
    sequence = NORMAL_SEQUENCE[:32]
    values: list[tuple[int, int]] = []
    binary_strings: list[str] = []
    max_string_length = 0

    for i in range(len(sequence)):
        value = trailing_bit_generator.generate_trailing_bits(sequence[:i+1], 1)
        values.append(value)
        binary_string = trailing_bit_generator.format_to_binary(value)
        binary_strings.append(binary_string)
        max_string_length = max(max_string_length, len(binary_string))

     
    for i in range(len(sequence)):
        binary_string = binary_strings[i]
        print(f"{" "*(max_string_length - len(binary_string))}{binary_string}")



def normal_of_2_and_4_loop():
    for i in range(0, len(NORMAL_SEQUENCE), 250):
        sequence = NORMAL_SEQUENCE[:i+1]
        result = loop_formula.get_loop(sequence)
        print(f"{len(sequence)}: {large_division(result, 100)}")



if __name__ == "__main__":
    normal_of_2_and_4_loop()
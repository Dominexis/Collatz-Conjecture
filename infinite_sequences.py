import powers
import loop_formula
import sequence_inverter
import trailing_bit_generator
import p_adics



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



def sequence_7_loop():
    sequence = [2,2,4,8,16]
    while True:
        sequence.append(4)
        result = loop_formula.get_loop(sequence)
        print(f"{len(sequence)}: {large_division(result, 100)}")



def test_sequence_inverter_on_loop():
    # sequence: list[int] = [2,2,8,4]
    sequence: list[int] = [2,2,4,8,16]
    while True:
        # sequence.append(2)
        sequence.append(4)
        result = sequence_inverter.invert_sequence(sequence, (0,1))
        print(f"{len(sequence)}: {large_division(result, 100)}")



def test_sequence_inverter_on_normal():
    for i in range(0, len(NORMAL_SEQUENCE), 250):
        sequence = NORMAL_SEQUENCE[:i+1]
        result = sequence_inverter.invert_sequence(sequence)
        print(f"{len(sequence)}: {large_division(result, 100)}")



def sequence_7_trailing_bits():
    sequence = [2,2,4,8,16]
    values: list[tuple[int, int]] = []
    binary_strings: list[str] = []
    max_string_length = 0

    for i in range(500):
        sequence.append(4)
        value = trailing_bit_generator.generate_trailing_bits(sequence, 1)
        values.append(value)
        binary_string = trailing_bit_generator.format_to_binary(value)
        binary_strings.append(binary_string)
        max_string_length = max(max_string_length, len(binary_string))

    for i in range(len(sequence)):
        binary_string = binary_strings[i]
        print(f"{" "*(max_string_length - len(binary_string))}{binary_string}")



def sequence_5_looped_2_adic():
    sequence = [16]

    for i in range(50):
        sequence.append(4)
        loop_result = loop_formula.get_loop(sequence)
        division_result = p_adics.division(loop_result[0], loop_result[1])
        print(f"{p_adics.convert_bits_to_string(division_result[0])}")



def doubling_sequence_loop():
    sequence = [2]
    numeral = 4
    while True:
        increase = len(sequence)
        for j in range(increase):
            sequence.append(numeral)
        result = loop_formula.get_loop(sequence)
        print(f"{len(sequence)}: {large_division(result, 100)}")
        numeral = 4 if numeral == 2 else 2



def fours_and_twos_loop():
    for length in range(1, 1000, 10):
        sequence: list[int] = []
        for i in range(length):
            sequence.append(4)
        for i in range(length):
            sequence.append(2)
        result = loop_formula.get_loop(sequence)
        print(f"{len(sequence)}: {large_division(result, 100)}")




if __name__ == "__main__":
    fours_and_twos_loop()
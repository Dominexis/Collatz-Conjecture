import generic
import powers
import json



def generate_trailing_bits(sequence: list[int] | str, denominator: int = 1, display: bool = False, details: bool = False) -> tuple[int, int]:
    """
    Because information flows from the least significant bits to the most significant in a Collatz sequence,
    the least significant bits dictate the steps in the sequence itself.

    This function takes a sequence of steps and reverses it over the least significant bits to compute
    the pattern of least significant bits which produce the given sequence of steps.

    A denominator must be provided in order for the addition step to be reversed.
    """

    if isinstance(sequence, str):
        sequence = generic.convert_steps_to_powers(sequence)

    value = 1
    modulo = 2

    if display:
        print("")

    for i in range(len(sequence)-1, -1, -1):
        power = sequence[i]

        # Reverse division step
        new_value = value*power
        modulo *= power
        if details:
            print("DIVIDE")
            print(f"{format(new_value, "b")} / {power} = {format(value, "b")}\n")
        value = new_value

        # Reverse adding denominator step
        new_value = (value - denominator)%modulo
        if details:
            print("ADD")
            show_sum(("denom", denominator), ("out", new_value), ("in", value))
        value = new_value

        # Reverse multiplication step
        for k in range(1, 4):
            if (modulo*k + value)%3 == 0:
                new_value = (modulo*k + value)//3%modulo
                break
        if details:
            print("MULTIPLY")
            show_sum(("out", new_value), ("outx2", new_value*2), ("in", value))
        value = new_value

    if display:
        print(f"Trailing bits using denominator {denominator}: {modulo}k + {value}, {format_to_binary((value, modulo))}\n")
    return value, modulo



def show_sum(addend_1: tuple[str, int], addend_2: tuple[str, int], total: tuple[str, int]):
    true_sum = addend_1[1] + addend_2[1]
    true_title = "true"
    
    addend_1_bin = format(addend_1[1], "b")
    addend_2_bin = format(addend_2[1], "b")
    total_bin = format(total[1], "b")
    true_sum_bin = format(true_sum, "b")

    max_title_length = max(len(addend_1[0]), len(addend_2[0]), len(total[0]), len(true_title))
    max_bin_length = max(len(addend_1_bin), len(addend_2_bin), len(total_bin), len(true_sum_bin))

    print(f"{addend_1[0]}:{" "*(max_title_length-len(addend_1[0]))}   {" "*(max_bin_length-len(addend_1_bin))}{addend_1_bin}")
    print(f"{addend_2[0]}:{" "*(max_title_length-len(addend_2[0]))} + {" "*(max_bin_length-len(addend_2_bin))}{addend_2_bin}")
    print(f"{total[0]}:{" "*(max_title_length-len(total[0]))} = {" "*(max_bin_length-len(total_bin))}{total_bin}")
    print(f"{true_title}:{" "*(max_title_length-len(true_title))}   {" "*(max_bin_length-len(true_sum_bin))}{true_sum_bin}")
    print("")



def format_to_binary(value: tuple[int, int]) -> str:
    return format(value[0] + value[1], "b")[1:]



def prompt_single():
    while True:
        sequence_prompt = input("Sequence (leave blank to exit): ")
        if not sequence_prompt:
            return
        
        try:
            sequence = generic.extract_sequence_from_prompt(sequence_prompt)
        except:
            continue


        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not denominator.isnumeric():
            print(f"ERROR: {denominator} is not numeric!")
            continue

        generate_trailing_bits(sequence, int(denominator), True, True)



def prompt_set():
    while True:
        sequence_prompt = input("Sequence (leave blank to exit): ")
        if not sequence_prompt:
            return
        
        try:
            sequence = generic.extract_sequence_from_prompt(sequence_prompt)
        except:
            continue

        sequence_steps = generic.convert_powers_to_steps(sequence)


        for denominator in range(1, 101, 2):
            value = generate_trailing_bits(sequence, int(denominator))
            binary_string = format_to_binary(value)
            print(f"{" "*(4-len(str(denominator)))}{denominator}: {" "*(1+len(sequence_steps)-len(binary_string))}{binary_string.replace("0", "-")}")



def prompt_construction():
    while True:
        sequence_prompt = input("Sequence (leave blank to exit): ")
        if not sequence_prompt:
            return

        try:
            sequence = generic.extract_sequence_from_prompt(sequence_prompt)
        except:
            continue


        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not denominator.isnumeric():
            print(f"ERROR: {denominator} is not numeric!")
            continue


        values: list[tuple[int, int]] = []
        binary_strings: list[str] = []
        max_string_length = 0

        for i in range(len(sequence)):
            value = generate_trailing_bits(sequence[:i+1], int(denominator))
            values.append(value)
            binary_string = format_to_binary(value)
            binary_strings.append(binary_string)
            max_string_length = max(max_string_length, len(binary_string))

        
        for i in range(len(sequence)):
            progress = sequence[:i+1]
            binary_string = binary_strings[i]
            print(f"{" "*(max_string_length - len(binary_string))}{binary_string} : {progress}")


        lines: list[str] = []
        for i in range(len(sequence)):
            value = values[i]
            parts: list[str] = []
            while True:
                binary_string = format_to_binary(value)
                parts.append(f"{" "*(max_string_length - len(binary_string))}{binary_string}")
                if value[1] <= 2:
                    break
                new_value = (value[0]*3 + 1)%value[1]
                modulo = value[1]
                while new_value%2 == 0:
                    new_value //= 2
                    modulo //= 2
                value = (new_value, modulo)
            lines.append(" ".join(parts))
        
        with (generic.PROGRAM_PATH / "trailing_bits.txt").open("w", encoding="utf-8") as file:
            file.write("\n".join(lines))




# These will print out all the trailing bits up to a certain power limit within a certain depth
def prompt_exhaustive(compact: bool):
    while True:
        depth_prompt = input("Depth (leave blank to exit): ")
        if not depth_prompt:
            return
        if not depth_prompt.isnumeric():
            print(f"ERROR: {depth_prompt} is not numeric!")
            continue
        depth = int(depth_prompt)

        power_limit_prompt = input("Power limit (leave blank to exit): ")
        if not power_limit_prompt:
            return
        if not power_limit_prompt.isnumeric():
            print(f"ERROR: {power_limit_prompt} is not numeric!")
            continue
        power_limit = int(power_limit_prompt)

        print("")
        exhaustive_layer([], depth, power_limit, compact)

def exhaustive_layer(sequence: list[int], depth: int, power_limit: int, compact: bool):
    sequence.append(1)
    if compact and len(sequence) == depth:
        sequence[-1] = powers.POWERS_OF_2[4*power_limit]
        value = generate_trailing_bits(sequence, 1)
        binary_string = format_to_binary(value)

        print(f"{binary_string[1:4*power_limit].replace("0", "-")}: {sequence}")

    else:
        for i in range(1, power_limit+1):
            sequence[-1] = powers.POWERS_OF_2[i]
            value = generate_trailing_bits(sequence, 1)
            binary_string = format_to_binary(value)

            if not compact:
                print(f"{(depth*power_limit+1 - len(binary_string))*" "}{binary_string}: {sequence}")
            if len(sequence) < depth:
                exhaustive_layer(sequence.copy(), depth, power_limit, compact)



def prompt_offset_finder():
    while True:
        depth_prompt = input("Depth (leave blank to exit): ")
        if not depth_prompt:
            return
        if not depth_prompt.isnumeric():
            print(f"ERROR: {depth_prompt} is not numeric!")
            continue
        depth = int(depth_prompt)

        power_limit_prompt = input("Power limit (leave blank to exit): ")
        if not power_limit_prompt:
            return
        if not power_limit_prompt.isnumeric():
            print(f"ERROR: {power_limit_prompt} is not numeric!")
            continue
        power_limit = int(power_limit_prompt)

        cycles = cycle_finder()

        print("")
        offset_finder_layer([], depth, power_limit, 1, cycles)


def offset_finder_layer(sequence: list[int], depth: int, power_limit: int, length: int, cycles: list[str]):
    sequence.append(1)
    if len(sequence) == depth:
        sequence[-1] = powers.POWERS_OF_2[32]
        value = generate_trailing_bits(sequence, 1)
        binary_string = format_to_binary(value)

        cycle = cycles[depth]
        segment = binary_string[32 - min(31, len(cycle)):32]
        offset = (len(cycle)*2 - ((cycle*2).find(segment) + len(segment))) % len(cycle)

        print(f"Anc: {length}, Rel: {offset}, Abs: {length + offset}: {sequence}, {segment}")

    else:
        for i in range(1, power_limit+1):
            sequence[-1] = powers.POWERS_OF_2[i]
            length += 1
            value = generate_trailing_bits(sequence, 1)
            binary_string = format_to_binary(value)

            if len(sequence) < depth:
                offset_finder_layer(sequence.copy(), depth, power_limit, length, cycles)



def prompt_exhaustive_offset_finder():
    while True:
        depth_prompt = input("Depth (leave blank to exit): ")
        if not depth_prompt:
            return
        if not depth_prompt.isnumeric():
            print(f"ERROR: {depth_prompt} is not numeric!")
            continue
        depth = int(depth_prompt)

        cycles = cycle_finder()
        cycle = cycles[depth]
        sequence = [2 for i in range(depth - 1)]
        sequence[0] = 4
        offsets = [[] for i in range(depth - 1)]

        base_offset = get_offset(sequence, cycle)

        for i in range(depth - 2, -1, -1):
            while True:
                offset = (get_offset(sequence, cycle) - base_offset) % len(cycle)
                # print(f"{offset}: {sequence}")

                if i != depth - 2:
                    for j in range(depth - 2, i, -1):
                        offset_array = offsets[j]
                        offset = (len(offset_array) - offset_array.index(offset)) % len(offset_array)

                if offset not in offsets[i]:
                    offsets[i].append(offset)
                else:
                    break

                sequence[i] *= 2
            sequence[i] = 2
            print(f"\n{i}: {offsets[i]}")




# This function will compute the cycles of bits for a set number of depths
def cycle_finder(display: bool = False) -> list[str]:
    cycles: list[str] = ["0"]
    power_of_4 = 1
    for power_of_3 in range(1, 10):
        while True:
            if (powers.POWERS_OF_2[power_of_4*2] - 1) % powers.POWERS_OF_3[power_of_3] == 0:
                value = (powers.POWERS_OF_2[power_of_4*2] - 1) // powers.POWERS_OF_3[power_of_3]
                binary_string = format(value, "b")
                binary_string = "0"*(power_of_4*2 - len(binary_string)) + binary_string
                cycles.append(binary_string)
                if display:
                    print(f"\n{power_of_3}, {power_of_4}: {binary_string.replace("0", "-")}")
                break
            power_of_4 += 1
    return cycles

# This function will get the phase of the segment within the given cycle
def get_offset(sequence: list[int], cycle: str) -> int:
    sequence = sequence.copy()
    sequence.append(powers.POWERS_OF_2[32])
    value = generate_trailing_bits(sequence, 1)
    binary_string = format_to_binary(value)
    segment = binary_string[32 - min(31, len(cycle)):32]
    offset = (len(cycle)*2 - ((cycle*2).find(segment) + len(segment))) % len(cycle)
    # print(f"{sequence}, {offset}, {binary_string}, segment: {segment}, cycle: {cycle}")
    return offset

# Computes a multidimensional array of every possible offset up to a certain depth limit
def compute_offset_array(depth_limit: int) -> list[dict[tuple, list[int]]]:
    offset_array: list[dict[tuple, list[int]]] = [{} for i in range(depth_limit + 1)]
    offset_array[0] = {(): [0, 0]}
    cycles = cycle_finder()
    compute_offset_array_layer(offset_array, [], depth_limit, 1, cycles)
    return offset_array

def compute_offset_array_layer(offset_array: list[dict[tuple, list[int]]], sequence: list[int], depth_limit: int, depth: int, cycles: list[str]):
    sequence.append(1)

    for i in range(1, 2*powers.POWERS_OF_3[depth - 1] + 1):
        sequence[-1] = powers.POWERS_OF_2[i]
        offset = get_offset(sequence, cycles[depth + 1])
        offset_array[depth][tuple(sequence)] = [offset, (offset_array[depth - 1][tuple(sequence[:-1])][0] + i)%(2*powers.POWERS_OF_3[depth - 1])]

        if depth < depth_limit:
            compute_offset_array_layer(offset_array, sequence.copy(), depth_limit, depth + 1, cycles)

def export_offset_array(depth_limit: int):
    offset_array = compute_offset_array(depth_limit)
    converted_offset_array: list[dict[str, str]] = []
    for entry in offset_array:
        converted_offset_array.append({})
        for key in entry:
            converted_offset_array[-1][str(key)] = f"_ARRAY{entry[key]}ARRAY_"
    with (generic.PROGRAM_PATH / "offset_array.json").open("w", encoding="utf-8") as file:
        file.write(
            json.dumps(converted_offset_array, indent=4).replace('"_ARRAY', "").replace('ARRAY_"', "")
        )



def constructive_trailing_bit_generator_test(depth: int, offset: int):
    cycle_period = 2*powers.POWERS_OF_3[depth - 1]
    previous_cycle_period = 2*powers.POWERS_OF_3[depth - 2]

    # This is the amount that the number is shifted by the left by to encode the offset of the previous section
    offset_size = previous_cycle_period*3 + offset + (1 if depth <= 2 else 0)
    offset_factor = powers.POWERS_OF_2[offset_size - 1]
    # This is the power of 3 associated with the previous section
    depth_power = powers.POWERS_OF_3[depth - 1]

    power_of_4 = cycle_period + 1
    while True:
        # This is the initial offset test
        offset_test = powers.POWERS_OF_2[power_of_4*2]
        numerator = (offset_test - 1)//3 * offset_factor - 1
        if numerator % depth_power == 0:
            value = numerator // depth_power
            binary_string = format_to_binary((value, offset_test*offset_factor))
            print(f"Depth: {depth}, previous offset: {offset}, offset: {(cycle_period - power_of_4*2 + 1)%cycle_period}, {binary_string[:-offset_size]} {binary_string[-offset_size:]}")
            # print(f"({offset}, {(cycle_period - power_of_4*2 + 1)%cycle_period}), ", end="")
            break

        power_of_4 += 1

def trigger_constructive_test():
    for depth in range(2, 6):
        # print("\n[", end="")
        print("")
        for offset in range(0, 2*powers.POWERS_OF_3[depth - 2]):
            constructive_trailing_bit_generator_test(depth, offset)
        # print("]")



def constructive_trailing_bit_generator(sequence: list[int] | str) -> str:
    
    if isinstance(sequence, str):
        sequence = generic.convert_steps_to_powers(sequence)

    # Handle edge case of the first step in the sequence
    power_index = powers.POWERS_OF_2.index(sequence[0])
    output = "01" * (power_index//2 + 1)
    if power_index%2 == 0:
        output = "0" + output[2:]
    else:
        output = "1" + output[1:]
    offset = power_index%2
    depth = 1


    for step in sequence[1:]:
        depth += 1
        power_index = powers.POWERS_OF_2.index(step)

        cycle_period = 2*powers.POWERS_OF_3[depth - 1]
        previous_cycle_period = 2*powers.POWERS_OF_3[depth - 2]

        # This is the amount that the number is shifted by the left by to encode the offset of the previous section
        offset_size = (offset + (1 if depth <= 2 else 0) - 1)%previous_cycle_period + 1
        offset_factor = powers.POWERS_OF_2[offset_size - 1]
        # This is the power of 3 associated with the previous section
        depth_power = powers.POWERS_OF_3[depth - 1]

        power_of_4 = power_index//2 + 1
        while True:
            # This is the initial offset test
            offset_test = powers.POWERS_OF_2[power_of_4*2]
            numerator = (offset_test - 1)//3 * offset_factor - 1 # This number has the form 0101010101001111111 in binary
            if numerator % depth_power == 0:
                value = numerator // depth_power
                offset = (cycle_period - power_of_4*2 + 1 + power_index)%cycle_period
                binary_string = format_to_binary((value, offset_test*offset_factor))
                output = binary_string[-offset_size-power_index: -offset_size] + output
                if output.startswith("0"):
                    output = "1" + output[1:]
                else:
                    output = "0" + output[1:]
                break

            power_of_4 += 1

    return output



def prompt_constructive_trailing_bit_generator():
    while True:
        sequence_prompt = input("Sequence (leave blank to exit): ")
        if not sequence_prompt:
            return
        
        try:
            sequence = generic.extract_sequence_from_prompt(sequence_prompt)
        except:
            continue
        
        old = format_to_binary(generate_trailing_bits(sequence))
        new = constructive_trailing_bit_generator(sequence)
        print(f"Old: {old}")
        print(f"New: {new}")
        if old == new:
            print("Match!")
        else:
            print("ERROR")



def prompt_exhaustive_constructive_test():
    while True:
        depth_prompt = input("Depth (leave blank to exit): ")
        if not depth_prompt:
            return
        if not depth_prompt.isnumeric():
            print(f"ERROR: {depth_prompt} is not numeric!")
            continue
        depth = int(depth_prompt)

        power_limit_prompt = input("Power limit (leave blank to exit): ")
        if not power_limit_prompt:
            return
        if not power_limit_prompt.isnumeric():
            print(f"ERROR: {power_limit_prompt} is not numeric!")
            continue
        power_limit = int(power_limit_prompt)

        print("")
        exhaustive_constructive_test_layer([], depth, power_limit, 1)


def exhaustive_constructive_test_layer(sequence: list[int], depth: int, power_limit: int, length: int):
    sequence.append(1)
    for i in range(1, power_limit+1):
        sequence[-1] = powers.POWERS_OF_2[i]
        length += 1
        old = format_to_binary(generate_trailing_bits(sequence))
        new = constructive_trailing_bit_generator(sequence)
        if old != new:
            print(f"{sequence}\n{old}\n{new}\n")

        if len(sequence) < depth:
            exhaustive_constructive_test_layer(sequence.copy(), depth, power_limit, length)




def prompt():
    while True:
        print("1) Single")
        print("2) Set")
        print("3) Construction")
        print("4) Exhaustive")
        print("5) Exhaustive (compact)")
        print("6) Cycle finder")
        print("7) Offset finder")
        print("8) Exhaustive offset finder")
        print("9) Export offset array")
        print("10) Constructive test")
        print("11) Constructive trailing bit generator")
        print("12) Exhaustive constructive test")
        select = input("Select (leave blank to exit): ")

        if not select:
            return
        
        if select == "1":
            prompt_single()
        if select == "2":
            prompt_set()
        if select == "3":
            prompt_construction()
        if select == "4":
            prompt_exhaustive(False)
        if select == "5":
            prompt_exhaustive(True)
        if select == "6":
            cycle_finder(True)
        if select == "7":
            prompt_offset_finder()
        if select == "8":
            prompt_exhaustive_offset_finder()
        if select == "9":
            export_offset_array(3)
        if select == "10":
            trigger_constructive_test()
        if select == "11":
            prompt_constructive_trailing_bit_generator()
        if select == "12":
            prompt_exhaustive_constructive_test()



if __name__ == "__main__":
    prompt()
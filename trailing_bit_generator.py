import generic
import powers



def generate_trailing_bits(sequence: list[int] | str, denominator: int, display: bool = False, details: bool = False) -> tuple[int, int]:
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





def prompt():
    while True:
        print("1) Single")
        print("2) Set")
        print("3) Construction")
        print("4) Exhaustive")
        print("5) Exhaustive (compact)")
        print("6) Cycle finder")
        print("7) Offset finder")
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



if __name__ == "__main__":
    prompt()
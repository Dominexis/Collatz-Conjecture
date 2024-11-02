import generic



def generate_trailing_bits(sequence: list[int] | str, denominator: int, display: bool = False, details: bool = False) -> int:
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
        print(f"Trailing bits using denominator {denominator}: {modulo}k + {value}, {format(value, "b")}\n")
    return value



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
            print(f"{" "*(4-len(str(denominator)))}{denominator}: {" "*(1+len(sequence_steps)-len(format(value, "b")))}{format(value, "b").replace("0", "-")}")



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


        binary_strings: list[str] = []
        max_string_length = 0

        for i in range(len(sequence)):
            value = generate_trailing_bits(sequence[:i+1], int(denominator))
            binary_string = format(value, "b")
            binary_strings.append(binary_string)
            max_string_length = max(max_string_length, len(binary_string))

        
        for i in range(len(sequence)):
            progress = sequence[:i+1]
            binary_string = binary_strings[i]
            print(f"{" "*(max_string_length - len(binary_string))}{binary_string} : {progress}")



def prompt():
    while True:
        print("1) Single")
        print("2) Set")
        print("3) Construction")
        select = input("Select (leave blank to exit): ")

        if not select:
            return
        
        if select == "1":
            prompt_single()
        if select == "2":
            prompt_set()
        if select == "3":
            prompt_construction()



if __name__ == "__main__":
    prompt()
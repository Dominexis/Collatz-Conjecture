def get_rational_cycle(denominator: int, display: bool = False) -> list[int]:

    if denominator%2 == 0:
        raise ValueError("Denominator must be odd")
    
    binary_string = format(denominator, "b")
    if display:
        print(f"Binary: {binary_string}")

    bits: list[int] = [1]
    
    # Least significant bit is not included in the offset list
    offsets: list[int] = []
    for i in range(len(binary_string)-2, -1, -1):
        if binary_string[i] == "1":
            offsets.append(len(binary_string) - i - 1)
    if display:
        print(f"Offsets: {offsets}")

    cycle_snapshot: list[int] = []
    cycle_start = 0
    carry = 0
    i = 1
    while True:
        addends: list[int] = []
        for offset in offsets:
            if i - offset >= 0:
                addends.append(bits[i - offset])
        addends.append(carry)
        total = sum(addends)

        if total%2:
            total += 1
            bits.append(1)
        else:
            bits.append(0)
        carry = total//2
        future_bits = bits[i - offsets[-1] + 1:]
        if display:
            print(f"Bits: {convert_bits_to_string(bits)}, Addends: {convert_bits_to_string(addends)}, Future bits: {convert_bits_to_string(future_bits)}")


        if i == offsets[-1] + 1:
            cycle_snapshot = addends + future_bits
            cycle_start = i + 1
            if display:
                print(f"Snapshot generated: {convert_bits_to_string(cycle_snapshot)}")
        if i > offsets[-1] + 1 and addends + future_bits == cycle_snapshot:
            if display:
                print("Match")
            break

        i += 1

    return bits[cycle_start:]



def convert_bits_to_string(bits: list[int]) -> str:
    chars: list[str] = []
    for bit in bits:
        chars.append(str(bit))
    return "".join(chars)



def prompt_single():
    while True:
        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not denominator.isnumeric():
            print(f"ERROR: {denominator} is not numeric!")
            continue

        cycle = get_rational_cycle(int(denominator), True)
        print(f"Cycle: {convert_bits_to_string(cycle)}\nLength: {len(cycle)}\n")


    
def prompt_set():
    for denominator in range(3, 500, 2):
        cycle = get_rational_cycle(int(denominator))
        print(f"Denominator: {denominator}, Length: {len(cycle)}")

    for power in range(2, 65):
        denominator = int(2**power) - 1
        cycle = get_rational_cycle(denominator)
        print(f"Denominator: {denominator}, Length: {len(cycle)}")



def prompt():
    while True:
        print("1) Single")
        print("2) Set")
        select = input("Select (leave blank to exit): ")

        if not select:
            return
        
        if select == "1":
            prompt_single()
        if select == "2":
            prompt_set()



if __name__ == "__main__":
    prompt()
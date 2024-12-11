import powers



def division(numerator: int, denominator: int, display: bool = False) -> tuple[list[int], int]:
    
    if numerator%2 == 0:
        raise ValueError("Numerator must be odd")
    if denominator%2 == 0:
        raise ValueError("Denominator must be odd")
    
    is_negative = numerator*denominator < 0
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    numerator_bits = convert_int_to_bits(numerator)
    numerator_length = len(numerator_bits)
    if display:
        print(f"Numerator: {format(numerator, "b")}")

    if denominator == 1:
        return numerator_bits, 1
    
    denominator_bits = convert_int_to_bits(denominator)
    if display:
        print(f"Denominator: {format(denominator, "b")}")

    bits: list[int] = [1]
    
    # Least significant bit is not included in the offset list
    offsets: list[int] = []
    for i in range(len(denominator_bits)-2, -1, -1):
        if denominator_bits[i] == 1:
            offsets.append(len(denominator_bits) - i - 1)
    if display:
        print(f"Offsets: {offsets}")

    snapshot_generated = False
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

        # Logic for determining the next bit
        if total%2 != (numerator_bits[i] if i < numerator_length else 0):
            total += 1
            bits.append(1)
        else:
            bits.append(0)
        carry = total//2
        future_bits = bits[i - offsets[-1] + 1:]
        if display:
            print(f"Bits: {convert_bits_to_string(bits)}, Addends: {convert_bits_to_string(addends)}, Future bits: {convert_bits_to_string(future_bits)}")


        # Logic for detecting repetitions
        if snapshot_generated and addends + future_bits == cycle_snapshot:
            if display:
                print("Match")
            break
        if i >= offsets[-1] + 1 and i >= numerator_length + 1 and not snapshot_generated:
            snapshot_generated = True
            cycle_snapshot = addends + future_bits
            cycle_start = i + 1
            if display:
                print(f"Snapshot generated: {convert_bits_to_string(cycle_snapshot)}")

        i += 1


    # Logic for negation
    if is_negative:
        number = powers.POWERS_OF_2[len(bits)] - convert_bits_to_int(bits)
        bits = convert_int_to_bits(number, len(bits))

    return bits, cycle_start



def convert_bits_to_string(bits: list[int]) -> str:
    chars: list[str] = []
    for bit in bits:
        chars.append(str(bit))
    return "".join(chars)

def convert_int_to_bits(number: int, length: int = 0) -> list[int]:
    binary_string = format(number, "b")
    binary_string += "0"*(length - len(binary_string))
    bits: list[int] = []
    for i in range(len(binary_string)-1, -1, -1):
        bits.append(int(binary_string[i]))
    return bits

def convert_bits_to_int(bits: list[int]) -> int:
    number = 0
    for i in range(len(bits)-1, -1, -1):
        number *= 2
        number += bits[i]
    return number



def prompt_division():
    while True:
        numerator = input("Numerator (leave blank to exit): ")
        if not numerator:
            return
        try:
            int(numerator)
        except:
            print(f"ERROR: {numerator} is not numeric!")
            continue

        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        try:
            int(denominator)
        except:
            print(f"ERROR: {denominator} is not numeric!")
            continue

        bits, cycle_start = division(int(numerator), int(denominator), True)
        binary_string = convert_bits_to_string(bits)
        print(f"Bits: {binary_string}\nCycle: {binary_string[cycle_start:]}, Length: {len(binary_string[cycle_start:])}\n")



if __name__ == "__main__":
    prompt_division()
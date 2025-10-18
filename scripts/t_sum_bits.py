from pathlib import Path
import random
import powers



PROGRAM_PATH = Path(__file__).parent



def convert_to_bits(number: int) -> str:
    chars = [char for char in format(number, "b")]
    chars.reverse()
    return "".join(chars)



def generate_bits():
    contents = ""
    number = 1
    power_of_2 = 2
    substring_number = 0
    for i in range(100):
        while True:
            substring = convert_to_bits(substring_number)
            if substring not in contents:
                break
            substring_number += 1

        line = convert_to_bits(number)
        contents = contents + line + "\n"
        print(line)
        number *= 3
        # number += power_of_2
        power_of_2 *= random.choice([2,4,8,16])

    print(f'Biggest substring: {convert_to_bits(substring_number)}')
    
    with (PROGRAM_PATH / "t_sum_bits.txt").open("w") as file:
        file.write(contents)


def compare_bits():
    contents = ""
    modulo = powers.POWERS_OF_2[1000]
    t_sum = 1
    power_of_2 = 0

    preamble = [1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 4, 3, 1, 1, 5, 4]
    loop = [2]
    right_side = (modulo - 27)*3 % modulo
    # preamble = [1, 2, 6, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 4, 1, 2, 1, 3, 1, 3, 1, 3, 3, 1, 1, 1, 1, 2, 7, 1, 2, 2, 3, 1, 1, 1, 1, 4, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 4, 3, 1, 1, 5, 4]
    # loop = [2]
    # right_side = (modulo - 418379)*3 % modulo
    # preamble = [4, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 3, 1, 6, 1, 2, 3, 1, 2, 3, 1, 1, 4, 3, 1, 3, 1, 4, 1, 1, 2, 1, 1, 3, 2, 1, 2, 1, 2, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 2, 4, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 5, 2, 1, 1, 7, 2, 1, 4, 1, 3, 1, 2, 3, 4]
    # loop = [2]
    # right_side = (modulo - 48295013)*3 % modulo
    # preamble = [1, 1, 1, 4, 2, 1, 4, 1, 3, 2, 2, 3, 5, 3]
    # loop = [1, 1, 2, 1, 1, 4, 1]
    # right_side = (modulo - -45169)*3 % modulo

    # 579/5
    # preamble = [1, 1, 2, 1, 2, 2, 3, 4, 1, 1, 1, 1, 1, 3, 2, 5, 2, 1, 1, 1]
    # loop = [3, 1, 1]
    # fifth = 3
    # for i in range(300):
    #     fifth = fifth*16 + 3
    # right_side = fifth*579*3 % modulo
    for i in range(1000):
        t_sum_line = convert_to_bits(t_sum)
        right_side_line = convert_to_bits(right_side)

        if i < len(preamble):
            power_of_2 += preamble[i]
        else:
            power_of_2 += loop[(i - len(preamble)) % len(loop)]

        line = ""
        if i == len(preamble):
            line += "LOOP\n"
        line = line + right_side_line + "\n" + t_sum_line + "\n"
        if powers.POWERS_OF_2[power_of_2] < modulo:
            line += " "*power_of_2 + "1\n"
        print(line)
        contents += line + "\n"

        t_sum = (t_sum*3 + powers.POWERS_OF_2[power_of_2]) % modulo
        
        right_side = right_side*3 % modulo

    with (PROGRAM_PATH / "t_sum_bits.txt").open("w") as file:
        file.write(contents)



if __name__ == "__main__":
    # generate_bits()
    compare_bits()
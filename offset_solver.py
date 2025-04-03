import math
import powers



def offset_solver_iterator(power_limit: int, offset_limit: int, reverse: bool):
    if not reverse:
        for power in range(1, power_limit+1):
            for offset in range(offset_limit + 1):
                offset_solver(power, offset)
    else:
        for offset in range(offset_limit + 1):
            for power in range(1, power_limit+1):
                offset_solver(power, offset)

def offset_solver(power: int, offset: int):
    modulo = powers.POWERS_OF_3[power]
    if offset >= math.floor(modulo*2/3):
        return

    congruent_target = (powers.POWERS_OF_2[offset] + 3) % modulo
    for offset_test in range(math.floor(modulo*2/3)):
        value = powers.POWERS_OF_2[offset_test] % modulo
        if value == congruent_target:
            print(f"({power}, {offset}): {offset_test}")
            break
    else:
        print(f"({power}, {offset}): N/A")



if __name__ == "__main__":
    offset_solver_iterator(9, 100, True)

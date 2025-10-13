import math
import powers



def offset_solver_sequence(sequence: list[int]):
    power = 2
    offset = 0
    modulo = 6
    for step in sequence:
        # print(f"Offset: {offset}")
        result = offset_solver(power, (step - offset) % modulo)
        if result is None:
            print("ERROR: Result is None")
            return
        offset = (result - step + offset) % modulo
        power += 1
        modulo *= 3

def offset_solver_iterator(power_limit: int, offset_limit: int, reverse: bool):
    if not reverse:
        for power in range(1, power_limit+1):
            for offset in range(offset_limit + 1):
                offset_solver(power, offset)
    else:
        for offset in range(offset_limit + 1):
            for power in range(1, power_limit+1):
                offset_solver(power, offset)

def offset_solver(power: int, offset: int) -> int | None:
    modulo = powers.POWERS_OF_3[power]
    if offset >= math.floor(modulo*2/3):
        return
    
    congruent_target = 1
    for i in range(offset):
        congruent_target = congruent_target*2 % modulo
    congruent_target = (congruent_target + 3) % modulo

    value = 1
    for offset_test in range(math.floor(modulo*2/3)):
        # value = powers.POWERS_OF_2[offset_test] % modulo
        if value == congruent_target:
            print(f"({power}, {offset}): {offset_test}")
            return offset_test
        value = value*2 % modulo
    else:
        print(f"({power}, {offset}): N/A")



if __name__ == "__main__":
    # offset_solver_iterator(10, 100, True)
    offset_solver_sequence([2,2,2,2,2,2,2,2,2,2])
    # offset_solver_sequence([1,1,1,1,1,1,1,1,1,1])
    # offset_solver_sequence([1,2,1,2,1,2,1,2,1,2])
    # offset_solver_sequence([2,1,1,3,4,1,2,1,2,1])
    # offset_solver_sequence([2, 1, 1, 1, 3, 4, 1, 3, 1, 2, 3, 4, 2,2,2,2,2,2,2,2,2])
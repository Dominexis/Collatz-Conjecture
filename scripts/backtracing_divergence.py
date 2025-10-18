def backtrace(ending: int, density: float, display: bool):
    value = ending*4 + 1
    length = 1
    weight = 2
    power_of_3 = 3

    for i in range(10000):
        if weight/length >= density:
            weight += 1
            value *= 2
        else:
            weight += 3
            value *= 8
        value -= power_of_3
        power_of_3 *= 3
        if display:
            print(f"{length}: {value}")
        length += 1
        if value < 0:
            return True

    return False



def test_ending(ending: int):
    density = 1.75
    step = 0.25
    for i in range(20):
        if backtrace(ending, density, False):
            density += step
        else:
            density -= step
        step *= 0.5
    print(f"Ending: {ending}, Density: {density}")



def prompt_backtrace():
    while True:
        ending = input("Ending: ")
        if not ending:
            break

        test_ending(int(ending))
        continue

        density = input("Density: ")
        if not density:
            break

        backtrace(int(ending), float(density), True)



if __name__ == "__main__":
    prompt_backtrace()
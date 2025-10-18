def backtrace(value: int, iterations: int):
    sequence: list[int] = []
    for i in range(iterations):
        match value%9:
            case 0:
                break
            case 1:
                sequence.append(2)
                value *= 4
            case 2:
                sequence.append(1)
                value *= 2
            case 3:
                break
            case 4:
                sequence.append(2)
                value *= 4
            case 5:
                sequence.append(3)
                value *= 8
            case 6:
                break
            case 7:
                sequence.append(4)
                value *= 16
            case 8:
                sequence.append(1)
                value *= 2

        if i == 3:
            value *= 64
            sequence[-1] += 6

        value -= 1
        value //= 3

    density = 0
    for entry in sequence:
        density += entry
    density /= len(sequence)

    print(f"Value: {value}\nSequence: {sequence}\nDensity: {density}\n")



def prompt_backtrace():
    while True:
        value = input("Value: ")
        if not value:
            break

        value = int(value)
        modified = False
        while value % 3 == 0:
            value //= 3
            modified = True
        if modified:
            print(f"Previous value was a multiple of 3, divided it to: {value}")

        backtrace(value, 1000)



if __name__ == "__main__":
    prompt_backtrace()
import powers



def get_next_source_bit(source: dict[str, list[int]]):
    bit = len(source["output"])

    source["output"].append((
        1 - sum([
            source["output"][m]*source["factor"][bit-m]
            for m in range(max(bit - len(source["factor"]) + 1, 0), bit)
        ])
        + source["carry"][bit - 1]//2
    ) % 2)

    source["carry"].append(
        1 - sum([
            source["output"][m]*source["factor"][bit-m]
            for m in range(max(bit - len(source["factor"]) + 1, 0), bit + 1)
        ])
        + source["carry"][bit - 1]//2
    )



def get_factor(power: int) -> list[int]:
    binary = format(powers.POWERS_OF_3[power], "b")
    return [int(binary[i]) for i in range(len(binary)-1, -1, -1)]



def zero_solver(power: int, offset: int, iterations: int):
    # Inject first source
    sources: list[dict[str, list[int]]] = [
        {
            "output": [1],
            "carry": [0],
            "factor": get_factor(power),
        }
    ]

    for i in range(offset):
        get_next_source_bit(sources[0])

    power += 1
    sources.append(
        {
            "output": [1],
            "carry": [0],
            "factor": get_factor(power),
        }
    )

    carry = 0
    step = 0
    steps: list[int] = []
    consecutive_twos = 0

    # for i in range(iterations):
    first = True
    while True:
        total = compute_sum(sources, carry)
        if not first and total%2 == 1:
            power += 1
            sources.append(
                {
                    "output": [1],
                    "carry": [0],
                    "factor": get_factor(power),
                }
            )
            total = compute_sum(sources, carry)
            if step == 2:
                consecutive_twos += 1
            else:
                consecutive_twos = 0
            steps.append(step)
            step = 0

        print(f"{total%2} = {"".join([str(source["output"][-1]) for source in sources])}")
        carry = total//2
        step += 1
        first = False

        for source in sources:
            get_next_source_bit(source)

        if consecutive_twos > 30:
            break

    print(f"Steps: {",".join([str(step) for step in steps])}")



def compute_sum(sources: list[dict[str, list[int]]], carry: int) -> int:
    return sum([source["output"][-1] for source in sources]) + carry



def prompt_zero_solver():
    power = int(input("Power: "))
    offset = int(input("Offset: "))
    iterations = int(input("Iterations: "))

    zero_solver(power, offset, iterations)



if __name__ == "__main__":
    while True:
        prompt_zero_solver()
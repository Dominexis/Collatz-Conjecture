import math



def divide_by_3(product: list[int]) -> list[int]:
    output: list[int] = [1]
    carry: list[int] = [0]

    for bit in product[1:]:
        output.append((bit - output[-1] + math.floor(carry[-1]*0.5))%2)
        carry.append(bit - output[-1] - output[-2] + math.floor(carry[-1]*0.5))

    return output



def repeated_division(value: list[int], iterations: int):
    print_bits(value)

    for i in range(iterations):
        value = divide_by_3(value)
        print_bits(value)



def print_bits(value: list[int]):
    bits: list[str] = []
    for bit in value:
        bits.append(str(bit))
    print("".join(bits))



if __name__ == "__main__":
    repeated_division([1 for i in range(50)], 50)
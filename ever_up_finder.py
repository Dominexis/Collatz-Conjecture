def show_number(value: int, length: int) -> str:
    string = format(value, "b")
    return " "*(length - len(string)) + string

def show_addition(addend_1: int, addend_2: int, sum: int, length: int) -> str:
    return f" {show_number(addend_1, length)}\n+{show_number(addend_2, length)}\n={show_number(sum, length)}\n"



def find_pattern(denominator: int, iterations: int, display: bool = False) -> int:
    """
    In order for a starting number to grow a certain number of times,
    the least bits of that number must follow a certain pattern.
    This pattern depends on the denominator group which the number is acting within.

    This function reverses 3n+1 /2 over several iterations to determine what that pattern is with some denominator.
    """

    value = 1
    modulo = 2
    length = 20
    for i in range(iterations):
        # Reverse division by 2 step
        value *= 2
        modulo *= 2

        # Reverse adding denominator step
        new_value = (value - denominator)%modulo
        if display:
            print("ADD")
            print(show_addition(denominator, new_value, value, length))
        value = new_value

        # Reverse multiplication step
        for k in range(1, 4):
            if (modulo*k + value)%3 == 0:
                new_value = (modulo*k + value)//3%modulo
                break
        if display:
            print("MULTIPLY")
            print(show_addition(new_value, new_value*2, value, length))
        value = new_value

    if display:
        print(f"Denominator {denominator} after {iterations} iterations: {modulo}k + {value}, {format(value, "b")}\n")
    return value



def prompt():
    while True:
        denominator = input("Denominator (leave blank to exit): ")
        if not denominator:
            return
        if not denominator.isnumeric():
            print(f"ERROR: {denominator} is not numeric!")
            continue

        iterations = 10
        find_pattern(int(denominator), iterations, True)



def display():
    for denominator in range(1, 1001, 2):
        value = find_pattern(int(denominator), 20)
        print(f"{" "*(4-len(str(denominator)))}{denominator}: {format(value, "b").replace("1", "-")}")
    return



if __name__ == "__main__":
    prompt()
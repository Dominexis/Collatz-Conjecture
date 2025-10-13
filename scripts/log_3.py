def compute_log_3(bits: str):
    # 1s place is always 1, 4s place is always 0

    # This is the power that 3 must be raised to to have the provided bits as the first bits in the result
    exponent_of_3 = int(bits[1])
    # This is the power of 3 associated with the above exponent, used to test against the test value
    power_of_3 = int(3**exponent_of_3)

    # This is the target, constructed bit by bit from the input
    test_value = exponent_of_3*2 + 1
    # This is the modulo of the test value to restrict the number of bits being tested at once
    modulo = 8

    # These encode 3^2^n, for performing the binary search on the exponent of 3
    super_exponent_of_3 = 1
    super_power_of_3 = 3

    for i in range(3, len(bits)):
        print(f"Processing bit: {i}")

        bit = bits[i]
        if bit == "1":
            test_value += modulo
        modulo *= 2
        super_exponent_of_3 *= 2
        super_power_of_3 *= super_power_of_3

        if power_of_3%modulo != test_value:
            exponent_of_3 += super_exponent_of_3
            power_of_3 *= super_power_of_3

        print(format(exponent_of_3, "b"))



if __name__ == "__main__":
    # compute_log_3("110100010001") # 3^7 = 2187
    compute_log_3("110011111111111111111111111")
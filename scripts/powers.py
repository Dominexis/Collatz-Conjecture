MAX_POWERS = 16384
"""Determines the length of the powers lists."""

POWERS_OF_2: list[int] = [1]
"""List of powers baked into an array to save on performance."""
POWERS_OF_3: list[int] = [1]
"""List of powers baked into an array to save on performance."""
POWERS_OF_10: list[int] = [1]
"""List of powers baked into an array to save on performance."""

for i in range(MAX_POWERS):
    POWERS_OF_2.append(POWERS_OF_2[i]*2)
    POWERS_OF_3.append(POWERS_OF_3[i]*3)
    POWERS_OF_10.append(POWERS_OF_10[i]*10)
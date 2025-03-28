# Collatz Conjecture

A collection of scripts and tools for studying the Collatz conjecture.

Start with some number `n`. If `n` is odd, multiply it by 3 and add 1. Conversely, if `n` is even, divide it by 2. Repeat this arbitrarily many times.

The Collatz conjecture states that all natural numbers, when applying the above rule, will eventually reach 1.

A more general version of the Collatz conjecture exists to account for 3 loops in the negatives, 0, and the positive loop containing 1.

## Collatz Loop Formula

A central part of the study is the Collatz loop formula. It takes a sequence of powers of 2, which represent the division steps of the Collatz sequence, and returns the value that will return to itself after said Collatz sequence.

![Collatz Loop Formula](images/loop_formula.png "Collatz Loop Formula")

Note, the above formula is designed with index-1 arrays in mind.

## Derivation of the Loop Formula

Start with some number `x`, then multiply it by 3 and add 1, then divide it by the first power of 2 in the sequence. This is the first iteration. Repeat this as many times as there are entries in the sequence, creating a nested fraction tower. Set it equal to `x` to make the sequence return to where it started.

![Collatz Loop Formula Derivation](images/loop_formula_tower.png "Collatz Loop Formula Derivation")

This equation is linear, so there is exactly one solution for `x`. Solving for `x` reveals a pattern which is generalizable for sequences of arbitrary length.

![Collatz Loop Formula Derivation](images/loop_formula_pattern.png "Collatz Loop Formula Derivation")

Abstracting these patterns results in the Collatz loop formula.

## Applying to Rationals

Both the original definition of the Collatz sequence and the loop formula apply to rational values.

To apply the sequence, simply consider the numerator of the fraction when it is in its simplest form.

The loop formula will return rational values for most inputs.

## Known Attributes of the Loop Formula

- Given the linearity of the loop formula and its derivation, a given sequence will produce exactly one loop. All loops have a unique identity, and no two loops share the same steps.

- With the exception of 0 (which has no `3n+1` step), all possible loops can be produced by the formula. This includes -1/2, which has no division step, and is represented by a sequence containing only 1. A sequence is not permitted to contain 1 and non-1 values, as this will not produce a valid Collatz sequence (a 1 represents multiple consecutive `3n+1` steps, which is impossible except for numbers with an even denominator, which never divide by 2).

- If your starting value has a denominator divisible by 3, it will be quickly reduced until no factors of 3 remain due to the `3n+1` step. Thus, no loops exist with a denominator divisible by 3.

- If your starting value has an even denominator, the `3n+1` step will only ever produce another odd number, thus no divisions by 2 will occur. Save for -1/2, all starting values with even denominators will diverge.

- For simplicity's sake, numbers with denominators divisible by 2 or 3 are not considered canon, and are not considered in most cases.

- With the exception of numbers with denominators divisible by 3, applying an iteration of the Collatz sequence will never change the denominator of the number.

    - Because the fraction is simple, the numerator and denominator are coprime.
    - If `a` and `b` are coprime, then `a + b` is coprime to both `a` and `b`.
    - When applying the `3n+1` step, the denominator is not divisible by 3 by definition, so the multiplication by 3 preserves the sides being coprime. Adding 1 to a fraction is equivalent to adding the denominator to the numerator, i.e. `a + b`, which also preserves the sides being coprime.
    - When applying the division by 2 step, the numerator must be even, and thus contains a factor of 2. Dividing the number by 2 reduces the numerator, but preserves the denominator.
    - Therefore, all values within a Collatz loop share a denominator in their simplest form.

- The unsimplified numerator and denominator from the loop formula will be known as the "base numerator" and "base denominator" respectively.

    - Because the base denominator is computed only from the length of the sequence and its weight (total powers of 2), the distribution of factors of 2 within the sequence does not change the value. e.g. `[2,4,8]` and `[4,4,4]` both produce a base denominator of 37.
    - This means that odd numbers within the same loop (which translate the sequence left or right) share a base denominator. e.g. `[2,4,8]` and `[4,8,2]` are two values within the same 3-step loop.
    - Because they also share a simplified denominator, it means that every base numerator within a loop has the same greatest common divisor with the base denominator.

## Loop Plotter

The loop plotter function is a 2-dimensional function to plot out all possible loops that can exist, save for non-canon loops such as 0 or -1/2.

The x axis plots the length of the sequence. The y axis plots the weight of the sequence, that is, the sum of the exponents of the powers of 2 in the sequence. e.g. the weight of `[2,2,4,2,8]` is `1+1+2+1+3`, or 8.

Sequences which repeat themselves are omitted e.g. `[2,4,2,4,2,4]`.

The output data is sorted into the following fields:

- `denominator`: The base denominator computed from that input.

- `denominators`: The list of all possible simplified denominators derived from the base denominator and the base numerators.

- `denominator_factors`: The prime factors of the base denominator. The keys of the array are the factors. The values of the array are the number of times that factor appears.

- `numerators`: The numerators which are computed from all possible loops from that input. The keys of the array are the numerators. The values of the array are the greatest common divisors between the base numerators and the base denominators.

- `numerator_gcds`: The greatest common divisors between the base numerators and the base denominator. The keys of the array are the greatest common divisors. The values of the array are the number of times each greatest common divisor appears.

A sample of the output was generated and written into `loop_plot.json`.

## Known Attributes of the Loop Plotter

- The space below the diagonal is undefined given that every entry in the list must be at least 2, hence, the weight must be at least equal to the length.

- Any given input has exactly one base denominator, because the base denominator is computed only from the length of the sequence and its weight.

- The base denominators are the difference between some power of 2 and some power of 3.

    - The gaps between these powers seem to become arbitrarily large, and rarely appear close to each other with larger values.
    - The vast majority of numbers are likely impossible to express as a difference between a power of 2 and a power of 3. This would suggest that the possible base denominators is a very restricted set.

- The base numerators are the sum of some terms, where each term is the product of some power of 2 and some power of 3.

    - Given the additive nature, any given list length has a minimum base numerator which can be returned. This means that we can search for possible base numerators exhaustively. The same is not true for the base denominators because those use subtraction.
    - The possible base numerators are more common than the possible base denominators, but they become very spread out for larger and larger values.

- For any given loop, all the base numerators share a greatest common divisor with the base denominator.

    - The base denominators tend to have few prime factors. Statistically, base numerators are most likely to be coprime to the base denominator rather than sharing a factor.
    - When common factors do appear, they tend to be small. Large greatest common divisors are generally uncommon.
    - There are four known cases where a greatest common divisor is equal to the base denominator (or its negative). These represent integer solutions to the loop formula. If a fifth case can be found, then the Collatz conjecture is false.
    - Given the ever-increasing base denominators, and the relative smallness of the greatest common divisors, it is unlikely that a fifth case will be found.
    - Trying to find such a case is a problem very adjacent to the distribution of primes. This suggests the Collatz conjecture is intimately connected to the mystery of the primes.

## Visual Plotter

The visual plotter will take the output of the loop plotter and generate a file containing a grid array where loop length is plotted horizontally and loop weight is plotted vertically. Each grid cell contains a single number. At the moment, that is the smallest simplified denominator which can be generated with those loop parameters. It is expected that the further out you go, the larger the numbers will generally get, but this is not proven.

## Numerator Inverter

The numerator inverter will take a proposed numerator and return all possible sequences of powers of 2 which will return said numerator in the loop formula. Because the final term of the sequence is not used in the numerator, it is omitted from the return value.

It works by first taking some length and subtracting the largest power of 3 present in a numerator of that length. From there, all remaining terms have a common factor of the first power of 2 in the sequence. Divide by 2 as many times as is possible. The number of divisions is the power of 2 of that term in the sequence. Repeat this process using the next smaller power of 3 until you run out. If at the very end you land on 0, that is a valid sequence and a valid numerator.

A given numerator can be produced with multiple sequences, so the numerator inverter will iterate through all possible lengths to find all possible sequences. There is a strict upper limit for what lengths can produce the given numerator because a given length has a minimum possible numerator that it can produce. If said minimum numerator is greater than the given numerator, it may be skipped.

## Sequence Inverter Formula

The sequence inverter formula takes a sequence of powers of 2, which represent the division steps of the Collatz sequence, and returns the value that will land on the provided ending value after said Collatz sequence.

![Collatz Sequence Inverter Formula](images/sequence_inverter_formula.png "Collatz Sequence Inverter Formula")

The formula is very similar to the loop formula. The power of 2 term from the denominator is multiplied by the ending and moved to the numerator, which subtracts off the existing numerator.

## Derivation of the Sequence Inverter Formula

The derivation is exactly like the loop formula, except instead of setting the tower to `x`, you set it to the ending `E`.

![Collatz Sequence Inverter Formula Derivation](images/sequence_inverter_formula_tower.png "Collatz Sequence Inverter Formula Derivation")

The simplification procedure is the same.

![Collatz Sequence Inverter Formula Derivation](images/sequence_inverter_formula_pattern.png "Collatz Sequence Inverter Formula Derivation")

Abstracting these patterns results in the Collatz sequence inverter formula.

## Trailing Bit Generator

When a number is iterated through the Collatz function, the least significant bits affect the most significant bits. The multiplication and addition steps strictly move information from right to left. For the division step, only divisions by 2 occur, which in binary, is a simple bitshift to the right.

For instance, the first step, whether up or down, is determined by the parity of the least significant bit. The immediate division by 2 causes a bitshift to the right, so then the parity of the second bit now determines the step. So the first two steps were determined by the first two bits (step here referring to an up or down step ending in a division by 2). Generally, the first `n` steps are determined by the first `n` bits. Because of the multiplication and addition steps, they must be taken as a set; so you cannot, for instance, take the third bit on its own to determine the third step.

The trailing bit generator reverses this process and takes a sequence of steps and computes the trailing bits which will produce that sequence of steps when iterated through the Collatz function. It requires assigning the denominator in advance as that will change how the reversal process goes.

## Known Attributes of the Trailing Bit Generator

- A given sequence of steps has infinitely many instances as the sequence appearing in a larger sequence depends only on the least significant bits, allowing the most significant bits to be assigned arbitrarily without changing the immediate steps.

- If the sequence is infinite in length, the trailing bits will become a 2-adic number representing the actual value. If the sequence repeats itself, the result will be the number from the loop encoded by said sequence.

- Because of the above point, all repeating sequences must belong to loops, meaning that if there exists a divergent sequence, the steps must be unrepeating.

- It is an unsolved problem whether unrepeating sequences will always generate unrepeating 2-adics, or whether they can generate repeating 2-adics in some cases. Solving this problem is closely related to solving the problem of loop distribution.
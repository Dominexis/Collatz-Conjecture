# Proof of the Collatz Inverter

## Abstract

The Collatz inverter algorithm takes a sequence of natural numbers, which represent the number of consecutive even steps between the odd steps, and returns the rightmost bits of the number which will follow the specified steps. If the sequence is infinite, then infinite bits are generated, which is a 2-adic representation of the number.

This document seeks to prove that this algorithm exists, and how it works on a deeper level.

## 1. Proof of the Existence of the Inverter

> Definition 1.1, the Collatz function:
>
> $`\mathrm{Collatz}\left(n\right) = \begin{cases} n/2 & \text{if}\ n \equiv 0 \left(\mathrm{mod}\ 2\right) \\ 3n+1 & \text{if}\ n \equiv 1 \left(\mathrm{mod}\ 2\right) \end{cases}`$

If $`n`$ is odd, then $`3n`$ is odd, then $`3n+1`$ is even. Therefore, odd steps will be followed by even steps.

To simplify, the even steps will be condensed into a single division. We will consider only odd numbers, making the iteration $`\frac{3n+1}{2^k}`$, where $`k`$ is the number of consecutive even steps.

We wish to find all numbers which will have exactly $`k`$ consecutive even steps after the first odd step. We can find these numbers by starting at the resulting value and working our way backwards. With $`n`$ being the number we wish to find, $`\frac{3n+1}{2^k}`$ will be an odd number, as after the $`k`$ even steps, we want another odd step.

Since the resulting number is odd, we start with $`1 \left(\mathrm{mod}\ 2\right)`$.

$`\frac{3n+1}{2^k} \equiv 1 \left(\mathrm{mod}\ 2\right)`$

We are looking for the value such that, after dividing by $`2^k`$, it is odd. Such a number is congruent to $`2^k \left(\mathrm{mod}\ 2^{k+1}\right)`$. Thus, in addition to multiplying both sides by $`2^k`$, we must also multiply the modulus by $`2^k`$.

$`3n+1 \equiv 2^k \left(\mathrm{mod}\ 2^{k+1}\right) \\ 3n \equiv 2^k - 1 \left(\mathrm{mod}\ 2^{k+1}\right) \\ n \equiv \frac{2^k - 1}{3} \left(\mathrm{mod}\ 2^{k+1}\right)`$

When we divide both sides by 3, we will have to perform modular division on the right hand side. To reliably perform modular division, we will express the numbers in binary and use an algorithm which will leverage this fact.

<details open>
<summary> 2-adic division </summary>

> Proof 1.2, 2-adic Division:
>
> Given a product $`P`$ and a factor $`F`$, we wish to compute output $`O`$ such that $`OF = P`$, and that they are all natural numbers.
>
> $`OF = P \\ O, F, P \in \N`$
>
> We will convert these values into a sum of powers of 2, representing the bits in the binary representation of these values.
>
> $`O_n, F_n, P_n \in \left\{0, 1\right\} \\ O_n, F_n, P_n = 0 \ \mathrm{where}\ n < 0`$
>
> $`\left( \sum_{i=0}^{\infty} O_i 2^i \right) \left( \sum_{j=0}^{\infty} F_j 2^j \right) = \sum_{k=0}^{\infty} P_k 2^k \\ \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} O_i F_j 2^{i+j} = \sum_{k=0}^{\infty} P_k 2^k`$
>
> To solve for a given bit, we will work in $`\mathrm{mod}\ 2^{b+1}`$, where $`b`$ is the index of the bit that we wish to solve for. All terms with a power of 2 greater than $`2^b`$ will be canceled to 0.
>
> $`\sum_{n=0}^{b} \sum_{m=0}^{n} O_m F_{n-m} 2^n \equiv \sum_{n=0}^{b} P_n 2^n \left(\mathrm{mod}\ 2^{b+1}\right) \\ 0 \equiv \sum_{n=0}^{b} P_n 2^n - \sum_{n=0}^{b} \sum_{m=0}^{n} O_m F_{n-m} 2^n \left(\mathrm{mod}\ 2^{b+1}\right) \\ 0 \equiv \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^n \left(\mathrm{mod}\ 2^{b+1}\right)`$
>
> We will divide both sides by $`2^b`$. To preserve congruency, we will also divide the modulus.
>
> $`0 \equiv \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b} \left(\mathrm{mod}\ 2\right)`$
>
> We will define $`C_b`$ to equal the right hand side of this expression.
>
> $`C_b = \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b} \\ 0 \equiv C_b \left(\mathrm{mod}\ 2\right)`$
>
> Then, we will extract out the term such that $`n = b`$.
>
> $`C_b = P_b - \sum_{m=0}^{b} O_m F_{b-m} + \sum_{n=0}^{b-1} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b}`$
>
> We will extract a factor of $`2^{-1}`$ from the rightmost term.
>
> $`C_b = P_b - \sum_{m=0}^{b} O_m F_{b-m} + \sum_{n=0}^{b-1} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-\left(b-1\right)} 2^{-1}`$
>
> Part of the rightmost term is equivalent to $`C_{b-1}`$. We will substitute.
>
> $`C_b = P_b - \sum_{m=0}^{b} O_m F_{b-m} + C_{b-1} 2^{-1}`$
>
> To solve for $`O_b`$, we will extract it out of the second term.
>
> $`0 \equiv P_b - O_b F_0 - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} \left(\mathrm{mod}\ 2\right) \\ O_b F_0 \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} \left(\mathrm{mod}\ 2\right)`$
>
> We will consider only odd values of $`F`$, such that $`F_0 = 1`$.
>
> $`O_b \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} \left(\mathrm{mod}\ 2\right)`$

</details>

We will use a special case for division by 3.

<details open>
<summary> 2-adic division by 3 </summary>

> Proof 1.3, 2-adic Division by 3:
>
> Take the expressions from Proof 1.2 and set $`F = 3`$.
>
> $`O_b \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} \left(\mathrm{mod}\ 2\right) \\ C_b = P_b - \sum_{m=0}^{b} O_m F_{b-m} + C_{b-1} 2^{-1}`$
>
> $`F_0, F_1 = 1 \\ F_n = 0 \ \mathrm{where}\ n > 1`$
>
> $`O_b \equiv P_b - O_{b-1} + C_{b-1} 2^{-1} \left(\mathrm{mod}\ 2\right) \\ C_b = P_b - O_b - O_{b-1} + C_{b-1} 2^{-1}`$

</details>

## 2. 
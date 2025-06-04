# Proof of the Collatz Inverter

## Abstract

The Collatz inverter algorithm takes a sequence of natural numbers, which represent the number of consecutive even steps between the odd steps, and returns the rightmost bits of the number which will follow the specified steps. If the sequence is infinite, then infinite bits are generated, which is a 2-adic representation of the number.

This document seeks to prove that this algorithm exists, and how it works on a deeper level.

## 1. Definition of the Inverter

> Definition 1.1, the Collatz function:
>
> $`\begin{align} \mathrm{Collatz}\left(n\right) = \begin{cases} n/2 & \text{if}\ n \equiv 0 \left(\mathrm{mod}\ 2\right) \\ 3n+1 & \text{if}\ n \equiv 1 \left(\mathrm{mod}\ 2\right) \end{cases} \notag \end{align}`$

If $`n`$ is odd, then $`3n`$ is odd, then $`3n+1`$ is even. Therefore, odd steps will be followed by even steps.

To simplify, the even steps will be condensed into a single division. We will consider only odd numbers, making the iteration $`\left(3n+1\right)/2^p`$, where $`p`$ is the number of consecutive even steps.

We will define the inverse of the Collatz function, which will undo $`p`$ even steps, and one odd step.

> Definition 1.2, the inverse Collatz function:
>
> $`\begin{align} \mathrm{Collatz}^{-1}\left(n,p\right) = \left(2^pn - 1\right)/3 \notag \end{align}`$

To define the inverter, we will apply the inverse Collatz function to a sequence of numbers representing the consecutive even steps between each odd step.

> Definition 1.3, the Collatz inverter function:
>
> Let $`s^n`$ be a sequence of length $`n`$, where $`s_n`$ is the $`n\text{th}`$ term in the sequence, indexed at $`0`$.
>
> In the trivial case where the sequence is empty and there are no steps to invert, we will return an odd number $`2k+1`$, where $`k \in \mathbb{Z}`$.
>
> Otherwise, when inverting the sequence, we undo the steps from last to first. We will do this by recursively nesting the function, with the last step being handled by the deepest nested layer:
>
> $`\begin{align} \mathrm{Inverter}\left(s^L\right) = & \begin{cases} 2k+1 & \text{if}\ L = 0 \\ \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_1 \ldots s_{L-1}\right]\right), s_0\right) & \text{else} \end{cases} \notag \end{align}`$

We will expand out the definition to produce a reduced expression.

> Proof 1.4, reduced Collatz inverter formula:
>
> Expanding out the general case of the Collatz inverter function, we get:
>
> $`\begin{align} \mathrm{Inverter}\left(s^L\right) & = \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_1, s_2, s_3 \ldots\right]\right), s_0\right) \notag \\ & = \left(2^{s_0} \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_2, s_3 \ldots\right]\right), s_1\right) - 1\right)/3 \notag \\ & = \left(2^{s_0}\left(2^{s_1}\left(2^{s_2}\left(2^{s_3}\left(\ldots\right)/3 - 1\right)/3 - 1\right)/3 - 1\right)/3 - 1\right)/3 \notag \\ & = 2^{s_0}\left(2^{s_1}\left(2^{s_2}\left(2^{s_3}\left(\ldots\right)\frac{1}{3^4} - \frac{1}{3^4}\right) - \frac{1}{3^3}\right) - \frac{1}{3^2}\right) - \frac{1}{3} \notag \\ & = \frac{2^{s_0 + s_1 + s_2 + s_3}}{3^4}\left(\ldots\right) - \frac{2^{s_0 + s_1 + s_2}}{3^4} - \frac{2^{s_0 + s_1}}{3^3} - \frac{2^{s_0}}{3^2} - \frac{1}{3} \notag \end{align}`$
>
> This can be reduced to a sum, plus the exceptional term at the end containing $`2k+1`$:
>
> $`\begin{align} \mathrm{Inverter}\left(s^L\right) & = \sum_{n=0}^{L-1} \frac{-1}{3^{n+1}} \prod_{p=0}^{n-1} 2^{s_p} + \left(2k+1\right) \frac{1}{3^L} \prod_{p=0}^{L-1} 2^{s_p} \notag \end{align}`$
>
> In the case of infinite sequences, we get the following:
>
> $`\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{p=0}^{n-1} 2^{s_p} + \left(2k+1\right) \frac{1}{3^{\infty}} \prod_{p=0}^{\infty} 2^{s_p} \notag \end{align}`$
>
> Every term in the sequence is a natural number, so the product on the right is equivalent to $`2^{\infty}`$:
>
> $`\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{p=0}^{n-1} 2^{s_p} + \left(2k+1\right) \frac{2^{\infty}}{3^{\infty}} \notag \end{align}`$
>
> We are working with 2-adic numbers. Given that $`2^{\infty} \equiv 0 \left(\mathrm{mod} \ 2^k\right)`$, we can substitute $`2^{\infty}`$ for $`0`$, which cancels the right term.
>
> $`\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{p=0}^{n-1} 2^{s_p} \notag \end{align}`$

## 2. 2-adic Division

To use the inverter effectively, we will represent the numbers in binary and use 2-adic division.

<details open>
<summary> 2-adic division </summary>

> Proof 2.1, 2-adic division:
>
> Given a product $`P`$ and a factor $`F`$, we wish to compute output $`O`$ such that $`OF = P`$. All of them are natural numbers.
>
> $`\begin{align} OF & = P \notag \\ O, F, P & \in \mathbb{N} \notag \end{align}`$
>
> We will convert these values into a sum of powers of 2, representing the bits in the binary representation of these values.
>
> $`\begin{align} O_n, F_n, P_n & \in \left\{0, 1\right\} \notag \\ O_n, F_n, P_n & = 0 \ \mathrm{where}\ n < 0 \notag \end{align}`$
>
> $`\begin{align} \left( \sum_{i=0}^{\infty} O_i 2^i \right) \left( \sum_{j=0}^{\infty} F_j 2^j \right) & = \sum_{k=0}^{\infty} P_k 2^k \notag \\ \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} O_i F_j 2^{i+j} & = \sum_{k=0}^{\infty} P_k 2^k \notag \end{align}`$
>
> To solve for a given bit, we will work in $`\mathrm{mod}\ 2^{b+1}`$, where $`b`$ is the index of the bit that we wish to solve for. All terms with a power of 2 greater than $`2^b`$ will be canceled to 0.
>
> $`\begin{align} \sum_{n=0}^{b} \sum_{m=0}^{n} O_m F_{n-m} 2^n & \equiv \sum_{n=0}^{b} P_n 2^n & \left(\mathrm{mod}\ 2^{b+1}\right) \notag \\ 0 & \equiv \sum_{n=0}^{b} P_n 2^n - \sum_{n=0}^{b} \sum_{m=0}^{n} O_m F_{n-m} 2^n & \left(\mathrm{mod}\ 2^{b+1}\right) \notag \\ 0 & \equiv \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^n & \left(\mathrm{mod}\ 2^{b+1}\right) \notag \end{align}`$
>
> We will divide both sides by $`2^b`$. To preserve congruency, we will also divide the modulus.
>
> $`\begin{align} 0 & \equiv \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b} & \left(\mathrm{mod}\ 2\right) \notag \end{align}`$
>
> We will define $`C_b`$ to equal the right hand side of this expression.
>
> $`\begin{align} C_b & = \sum_{n=0}^{b} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b} \notag \\ 0 & \equiv C_b & \left(\mathrm{mod}\ 2\right) \notag \end{align}`$
>
> Then, we will extract out the term such that $`n = b`$.
>
> $`\begin{align} C_b & = P_b - \sum_{m=0}^{b} O_m F_{b-m} + \sum_{n=0}^{b-1} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-b} \notag \end{align}`$
>
> We will extract a factor of $`2^{-1}`$ from the rightmost term.
>
> $`\begin{align} C_b & = P_b - \sum_{m=0}^{b} O_m F_{b-m} + \sum_{n=0}^{b-1} \left( P_n - \sum_{m=0}^{n} O_m F_{n-m} \right) 2^{n-\left(b-1\right)} 2^{-1} \notag \end{align}`$
>
> Part of the rightmost term is equivalent to $`C_{b-1}`$. We will substitute.
>
> $`\begin{align} C_b & = P_b - \sum_{m=0}^{b} O_m F_{b-m} + C_{b-1} 2^{-1} \notag \end{align}`$
>
> To solve for $`O_b`$, we will extract it out of the second term.
>
> $`\begin{align} 0 & \equiv P_b - O_b F_0 - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} & \left(\mathrm{mod}\ 2\right) \notag \\ O_b F_0 & \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} & \left(\mathrm{mod}\ 2\right) \notag \end{align}`$
>
> We will consider only odd values of $`F`$, such that $`F_0 = 1`$.
>
> $`\begin{align} O_b & \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} & \left(\mathrm{mod}\ 2\right) \notag \end{align}`$

</details>

We will use a special case for division by 3.

<details open>
<summary> 2-adic division by 3 </summary>

> Proof 2.2, 2-adic division by 3:
>
> Take the expressions from Proof 2.1 and set $`F = 3`$.
>
> $`\begin{align} O_b & \equiv P_b - \sum_{m=0}^{b-1} O_m F_{b-m} + C_{b-1} 2^{-1} & \left(\mathrm{mod}\ 2\right) \notag \\ C_b & = P_b - \sum_{m=0}^{b} O_m F_{b-m} + C_{b-1} 2^{-1} \notag \end{align}`$
>
> $`\begin{align} F_0, F_1 & = 1 \notag \\ F_n & = 0 \ \mathrm{where}\ n > 1 \notag \end{align}`$
>
> $`\begin{align} O_b & \equiv P_b - O_{b-1} + C_{b-1} 2^{-1} & \left(\mathrm{mod}\ 2\right) \notag \\ C_b & = P_b - O_b - O_{b-1} + C_{b-1} 2^{-1} \notag \end{align}`$

</details>

## 3. The Collatz Loop Function

To further aid our study, we will define a function which will return the number such that, after going through a given sequence of steps in the Collatz function, will return to itself.

> Proof 3.1, the Collatz loop function:
>
> We will define $`\mathrm{Loop}\left(s^L\right)`$ as the number which will return to itself after taking the steps in sequence $`s`$ of length $`L`$ in the Collatz function.
>
> $`\begin{align} \text{Let } \mathrm{Loop}\left(s^L\right) & = x \text{ where} \notag \end{align}`$
>
> $`\begin{align} x & = \frac{\frac{\frac{\frac{3x + 1}{2^{s_0}}3 + 1}{2^{s_1}} \ldots 3 + 1}{2^{s_{L-2}}}3 + 1}{2^{s_{L-1}}} \notag \\ x & = \frac{\frac{\frac{\frac{3^Lx + 3^{L-1}}{2^{s_0}} + 3^{L-2}}{2^{s_1}} \ldots + 3}{2^{s_{L-2}}} + 1}{2^{s_{L-1}}} \notag \end{align}`$
>
> $`\begin{align} & x = \frac{1}{2^{s_{L-1}}} + \frac{3}{2^{s_{L-2} + s_{L-1}}} \ldots \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^Lx}{2^{s_0 + s_1 \ldots s_{L-1}}} \notag \\ \frac{2^{s_0 + s_1 \ldots s_{L-1}} - 3^L}{2^{s_0 + s_1 \ldots s_{L-1}}} & x = \frac{1}{2^{s_{L-1}}} + \frac{3}{2^{s_{L-2} + s_{L-1}}} \ldots \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} \notag \\ \left(2^{s_0 + s_1 \ldots s_{L-1}} - 3^L\right) & x = 2^{s_0 + s_1 \ldots s_{L-2}} + 3 \times 2^{s_0 + s_1 \ldots s_{L-3}} \ldots 3^{L-2} \times 2^{s_0} + 3^{L-1} \notag \\ & x = \frac{2^{s_0 + s_1 \ldots s_{L-2}} + 3 \times 2^{s_0 + s_1 \ldots s_{L-3}} \ldots 3^{L-2} \times 2^{s_0} + 3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}} - 3^L} \notag \end{align}`$
>
> $`\begin{align} \mathrm{Loop}\left(s^L\right) & = \frac{\sum_{t=0}^{L-1} 3^{L-1-t} \prod_{p=0}^{t-1} 2^{s_p}}{\prod_{p=0}^{L-1} 2^{s_p} - 3^L} \notag \end{align}`$

## 4. Basic Theorems

### 4.1. Uniqueness

The Collatz function (1.1) is deterministic. Therefore, a given 2-adic has exactly one infinite sequence of steps that it will follow when carried out by the Collatz function.

Likewise, the Collatz inverter function (1.4) is deterministic. Therefore, a given infinite sequence of steps produces exactly one 2-adic when inverted. Therefore, no two 2-adics share the same infinite sequence of steps.

Thus, there is a bijection between the set of all possible 2-adic numbers and the set of all possible infinite sequences of natural numbers.

> Theorem 4.1, uniqueness of numbers and sequences:
>
> Every 2-adic number has exactly one infinite sequence of steps via the Collatz function, and every infinite sequence of steps has exactly one 2-adic number via the Collatz inverter function.

### 4.2. Looped Sequences

Suppose that you had an infinite sequence of steps $`s^{\infty}`$ that repeated itself every $`c`$ steps, such that $`s_n = s_{n+ck}`$ where $`c, k \in \mathbb{N}`$

Define a second sequence which is the same as the first, except that it is missing the first cycle: $`t_n = s_{n+c}`$

These sequences are actually equivalent: $`s_n = t_n = s_{n+c}`$

Thus, an infinite repeating sequence of steps produces the same number as that same infinite repeating sequence of steps minus the first cycle. Therefore, after said number goes through the steps of the cycle via the Collatz function, it will return to itself. Therefore, infinite repeating sequences of steps refer to loops within the Collatz function, with the period of the sequence being the period of the loop.

> Theorem 4.2, looped sequences:
>
> Every infinite repeating sequence of steps represents a loop within the Collatz function.

### 4.3. Preambles

Suppose that you had an infinite sequence of steps $`s^{\infty}`$ which resolved to a known value $`r`$, such that $`\mathrm{Inverter}\left(s^{\infty}\right) = r`$

Inserting another step $`n`$ at the start of the sequence is equivalent to undoing that same step from $`r`$.

$`\mathrm{Inverter}\left(\left[n, s_0, s_1 \ldots\right]\right) = \mathrm{Collatz}^{-1}\left(r, n\right)`$

This may be applied recursively.

> Theorem 4.3, sequence preambles:
>
> If a number $`r`$ follows the sequence of steps $`s^{\infty}`$ when iterating the Collatz function, then the number which follows a preamble of $`p`$ steps followed up by the sequence $`s^{\infty}`$ will land on $`r`$ after the preamble concludes in $`p`$ steps.

Therefore, if an infinite sequence of steps repeats itself only after some preamble of length $`p`$, such that $`s_n = s_{n+ck}`$ where $`n \ge p`$, then the number which follows these steps will fall into the associated loop after $`p`$ steps.

### 4.4. Rationality

Given some finite sequence of steps $`s^L`$, the Collatz loop function (3.1) will return the number such that, after taking those steps in the Collatz function, will return to itself.

The function returns a fraction, where the numerator and denominator are both integers. Thus, it will always return a rational value. Thus, an irrational value will never return to itself when iterated on the Collatz function.

In 2-adics, a number is rational if the bits repeat infinitely after some preamble, and a number is irrational if it never repeats.

Thus, if an infinite sequence of steps repeats itself, the inverted number will always be rational and have repeating bits. Likewise, if the number does not have repeating bits, then the resulting sequence of steps will not repeat.

> Theorem 4.4, rational loops:
>
> Every member of a loop in the Collatz function is rational. Irrational values will never return to themselves when iterated through the Collatz function.

### 4.5. Rational Collatz Function

A 2-adic number may be used in the Collatz function trivially. 2-adic numbers may represent integers, rational numbers, or irrational numbers. Each of these may be used in the Collatz function if they are expressed in 2-adic form.

When dividing one rational 2-adic by another using 2-adic division (2.1), it will return a rational 2-adic with infinitely repeating bits after some preamble. Multiplying the number by a power of 2 shifts the bits to the left and does not alter the cycle. Neither does adding integers alter the cycle.

If a 2-adic ends with a 0 bit, it may be divided by 2 without altering the cycle. Because $`\frac{1}{2}`$ cannot be represented as a 2-adic, the denominator of a rational 2-adic must always be odd. Thus, if a rational 2-adic may be divided by 2, dividing by 2 does not alter the denominator of the number.

Thus, the Collatz function may be generalized to rationals by considering the parity of the numerator when the ratio is in its simplest form.

> Definition 4.5, rational Collatz function:
>
> $`\begin{align} \mathrm{Collatz}\left(n\right) = & \begin{cases} n/2 & \text{if}\ a \equiv 0 \left(\mathrm{mod}\ 2\right) \\ 3n+1 & \text{if}\ a \equiv 1 \left(\mathrm{mod}\ 2\right) \end{cases} \notag \\ & \text{ where } n = \frac{a}{b}; a, b \in \mathbb{Z}; \mathrm{gcd}\left(a, b\right) = 1 \notag \end{align}`$

### 4.6. Denominator Preservation

When iterating a rational number through the generalized Collatz function, the even step will never alter the denominator of the ratio when expressed in its simplest form because the numerator is even. The odd step will alter the denominator if and only if the denominator is a multiple of 3.

> Theorem 4.6, denominator preservation
>
> When a rational number is iterated through the rational Collatz function, the denominator of the ratio when expressed in its simplest form will not change, unless the denominator is a multiple of 3.
>
> If the denominator is a multiple of 3, the factors of 3 will be canceled out by each iteration.

### 4.7. Rational Divergence

Suppose that you had a rational number which goes through a sequence of steps that does not repeat when iterated through the Collatz function. Such a sequence of numbers may not include the same number twice, as this would produce a loop. Because the denominator is not allowed to change (4.6), by the pigeonhole principle, the sequence of numbers must diverge.

> Theorem 4.7, rational divergence
>
> If a rational number will follow an infinite sequence of steps that does not repeat when iterated through the Collatz function, it must diverge.
# All Natural Numbers Stay Bounded in the Collatz Conjecture

By Jesse Spicer (Dominexis), October 18, 2025

## Outline

1. Abstract
2. Definitions
3. Derivation of the Sequence Inverter Function
4. Derivation of the Loop Function
5. Basic Theorems
6. Density Lower Bound
7. Derivation of the Average Step Size Function
8. Limiting Behavior of the Average Step Size Function
9. The Average Step Sizes of Looped and Divergent Sequences
10. Conclusion
11. References

## 1. Abstract

> Definition 1.1, the Collatz function:
>
> $\begin{align} & \text{If } n \text{ is even, divide by 2} \notag \\ & \text{If } n \text{ is odd, multiply by 3 and add 1} \notag \\ & \mathrm{Collatz}\left(n\right) = \begin{cases} n/2 & \text{if}\ n \equiv 0 \left(\mathrm{mod}\ 2\right) \\ 3n+1 & \text{if}\ n \equiv 1 \left(\mathrm{mod}\ 2\right) \end{cases} \notag \end{align}$

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) states that all positive integers $n$, when iterated through the Collatz function, will eventually reach 1 after a finite number of iterations.

The conjecture is false if either there exists a positive integer sequence which loops but doesn't contain 1, or it does not contain the same number twice and diverges. Proving that the conjecture is true will require disproving both statements.

In this paper, I will attempt to disprove the latter statement and show that all positive integer sequences remain bounded and fall into loops.

This paper relies heavily on the use of [2-adic](https://en.wikipedia.org/wiki/P-adic_number) numbers.

## 2. Definitions

If $n$ is odd, $3n$ is odd, and $3n+1$ is even. Thus, odd steps will be followed by even steps.

We will describe sequences of steps as lists of positive integers representing the number of consecutive even steps between the odd steps with the following notation: $s^L$, where $L$ is the length of the sequence.

We will reference particular indices within the list with the following notation: $s_i$, where $i$ is the 0-indexed key (i.e. $i=0$ refers to the first term in the list).

> Definition 2.1, sequence notation:
> 
> $\begin{align} s^L = \left[s_0, s_1, s_2, ... s_{L-1}\right] \text{ where } s_i \in \mathbb{N}, s_i \neq 0 \notag \end{align}$

We will define the weight of a sequence as the sum of all its terms: 

> Definition 2.2, the sequence weight function:
>
> $\begin{align} \mathrm{W}\left(s^L\right) = \sum_{i=0}^{L-1} s_i \notag \end{align}$

We will define the density of a sequence as the ratio of its weight and length, which is also the ratio of the even steps to the odd steps:

> Definition 2.3, the sequence density function:
>
> $\begin{align} \mathrm{D}\left(s^L\right) = \frac{\mathrm{W}\left(s^L\right)}{L} \notag \end{align}$

## 3. Derivation of the Sequence Inverter Function

We will derive a function which takes a sequence $s^L$ and returns the number which undergoes said sequence of steps when iterated through the Collatz function.

We will start by defining the inverse of the Collatz function, which will undo $c$ even steps and one odd step.

> Definition 3.1, the inverse Collatz function:
>
> $\begin{align} \mathrm{Collatz}^{-1}\left(n,c\right) = \left(2^cn - 1\right)/3 \notag \end{align}$

To define the sequence inverter function, we will apply the inverse Collatz function to a sequence of steps. It will be defined recursively, undoing the last steps in the deepest layer and working its way outwards.

In the trivial case where the sequence is empty and there are no steps to invert, we will return an odd number $2k+1$, where $k \in \mathbb{Z}$.

> Definition 3.2, the sequence inverter function:
>
> $\begin{align} \mathrm{Inverter}\left(s^L\right) = & \begin{cases} 2k+1 & \text{if}\ L = 0 \\ \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_1 \ldots s_{L-1}\right]\right), s_0\right) & \text{else} \end{cases} \notag \end{align}$

We will expand out the definition to produce a reduced expression.

> Proof 3.3, the reduced sequence inverter formula:
>
> Expanding out the general case of the sequence inverter function, we get:
>
> $\begin{align} \mathrm{Inverter}\left(s^L\right) & = \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_1, s_2, s_3 \ldots\right]\right), s_0\right) \notag \\ & = \left(2^{s_0} \mathrm{Collatz}^{-1}\left(\mathrm{Inverter}\left(\left[s_2, s_3 \ldots\right]\right), s_1\right) - 1\right)/3 \notag \\ & = \left(2^{s_0}\left(2^{s_1}\left(2^{s_2}\left(2^{s_3}\left(\ldots\right)/3 - 1\right)/3 - 1\right)/3 - 1\right)/3 - 1\right)/3 \notag \\ & = 2^{s_0}\left(2^{s_1}\left(2^{s_2}\left(2^{s_3}\left(\ldots\right)\frac{1}{3^4} - \frac{1}{3^4}\right) - \frac{1}{3^3}\right) - \frac{1}{3^2}\right) - \frac{1}{3} \notag \\ & = \frac{2^{s_0 + s_1 + s_2 + s_3}}{3^4}\left(\ldots\right) - \frac{2^{s_0 + s_1 + s_2}}{3^4} - \frac{2^{s_0 + s_1}}{3^3} - \frac{2^{s_0}}{3^2} - \frac{1}{3} \notag \end{align}$
>
> This can be reduced to a sum, plus the exceptional term at the end containing $2k+1$:
>
> $\begin{align} \mathrm{Inverter}\left(s^L\right) & = \sum_{n=0}^{L-1} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} + \left(2k+1\right) \frac{1}{3^L} \prod_{i=0}^{L-1} 2^{s_i} \notag \\ & = \sum_{n=0}^{L-1} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} + \left(2k+1\right) \frac{2^{\mathrm{W}\left(s^L\right)}}{3^L} \notag \end{align}$
>
> In the case of infinite sequences, we get the following:
>
> $\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} + \left(2k+1\right) \frac{2^{\mathrm{W}\left(s^{\infty}\right)}}{3^{\infty}} \notag \\ & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} + \left(2k+1\right) \frac{2^{\infty}}{3^{\infty}} \notag \end{align}$
>
> In the case where the sequence's density is less than $\mathrm{log_2}\left(3\right)$, which guarantees $2^{\mathrm{W}\left(s^L\right)}$ grows slower than $3^L$, the rightmost term becomes vanishingly small in the limit, and the entire sum converges to a real value:
>
> $\begin{align} & \sum_{n=0}^{\infty} \frac{2^{\mathrm{D}\left(s^L\right)n}}{3^n} = \sum_{n=0}^{\infty} \frac{2^{\mathrm{D}\left(s^L\right)n}}{2^{\mathrm{log}_2\left(3\right)n}} = \sum_{n=0}^{\infty} 2^{\left(\mathrm{D}\left(s^L\right) - \mathrm{log}_2\left(3\right)\right)n} \notag \\ & \text{If } \mathrm{D}\left(s^L\right) < \mathrm{log}_2\left(3\right), \text{then } \sum_{n=0}^{\infty} 2^{\left(\mathrm{D}\left(s^L\right) - \mathrm{log}_2\left(3\right)\right)n} \text{ converges.} \notag \end{align}$
>
> In the alternative case where the sum diverges, we will use 2-adic numbers, where $2^{\infty} \equiv 0$, which also cancels the rightmost term.
>
> $\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} \notag \end{align}$

## 4. Derivation of the Loop Function

We will derive a function which takes a finite sequence $s^L$ and returns the number which undergoes said sequence of steps when iterated through the Collatz function, and then returns to itself.

> Proof 4.1, the loop function:
>
> $\begin{align} \text{Let } \mathrm{Loop}\left(s^L\right) & = x \text{ where} \notag \end{align}$
>
> $\begin{align} x & = \frac{\frac{\frac{\frac{3x + 1}{2^{s_0}}3 + 1}{2^{s_1}} \ldots 3 + 1}{2^{s_{L-2}}}3 + 1}{2^{s_{L-1}}} \notag \\ x & = \frac{\frac{\frac{\frac{3^Lx + 3^{L-1}}{2^{s_0}} + 3^{L-2}}{2^{s_1}} \ldots + 3}{2^{s_{L-2}}} + 1}{2^{s_{L-1}}} \notag \end{align}$
>
> $\begin{align} & x = \frac{1}{2^{s_{L-1}}} + \frac{3}{2^{s_{L-2} + s_{L-1}}} \ldots \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^Lx}{2^{s_0 + s_1 \ldots s_{L-1}}} \notag \\ \frac{2^{s_0 + s_1 \ldots s_{L-1}} - 3^L}{2^{s_0 + s_1 \ldots s_{L-1}}} & x = \frac{1}{2^{s_{L-1}}} + \frac{3}{2^{s_{L-2} + s_{L-1}}} \ldots \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} \notag \\ \left(2^{s_0 + s_1 \ldots s_{L-1}} - 3^L\right) & x = 2^{s_0 + s_1 \ldots s_{L-2}} + 3 \cdot 2^{s_0 + s_1 \ldots s_{L-3}} \ldots 3^{L-2} \cdot 2^{s_0} + 3^{L-1} \notag \\ & x = \frac{2^{s_0 + s_1 \ldots s_{L-2}} + 3 \cdot 2^{s_0 + s_1 \ldots s_{L-3}} \ldots 3^{L-2} \cdot 2^{s_0} + 3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}} - 3^L} \notag \end{align}$
>
> $\begin{align} \mathrm{Loop}\left(s^L\right) & = \frac{\sum_{n=0}^{L-1} 3^{L-1-n} \prod_{i=0}^{n-1} 2^{s_i}}{\prod_{i=0}^{L-1} 2^{s_i} - 3^L} \notag \end{align}$
>
> We will define the function $\mathrm{T_{Sum}}$ to simplify the numerator:
>
> $\begin{align} \text{Let } \mathrm{T_{Sum}}\left(s^L\right) = \sum_{n=0}^{L-1} 3^{L-1-n} \prod_{i=0}^{n-1} 2^{s_i} \notag \end{align}$
>
> $\begin{align} \mathrm{Loop}\left(s^L\right) & = \frac{\mathrm{T_{Sum}}\left(s^L\right)}{2^{\mathrm{W}\left(s^L\right)} - 3^L} \notag \end{align}$

## 5. Basic Theorems

### 5.1. Extending the Collatz Function to 2-adics

A 2-adic number may be used in the Collatz function trivially. 2-adic numbers may represent integers, rational numbers, irrational numbers, or complex numbers. Each of these may be used in the Collatz function if they are expressed in 2-adic form by considering the units bit for the parity, assuming there are no bits to the right of the decimal point.

### 5.2. Uniqueness

The Collatz function (1.1) is deterministic. Thus, a given number has exactly one infinite sequence of steps that it will follow when carried out by the Collatz function.

Likewise, the sequence inverter function (3.3) is deterministic. Thus, a given infinite sequence of steps produces exactly one number when inverted. Thus, no two numbers share the same infinite sequence of steps.

> Theorem 5.2, uniqueness of numbers and sequences:
>
> Every 2-adic number has exactly one infinite sequence of steps via the Collatz function, and every infinite sequence of steps has exactly one 2-adic number via the sequence inverter function.

### 5.3. Looped Sequences

Given an infinite sequence of steps $s^{\infty}$, if it repeats every $c$ steps such that $s_n = s_{n+ck}$ where $c, k \in \mathbb{N}, c \neq 0$, then it is equivalent to the same sequence with the first period removed. Thus, the number undergoing the sequence returns to itself every period.

> Theorem 5.3, looped sequences:
>
> Every infinite repeating sequence of steps represents a loop within the Collatz function.

### 5.4. Rationality

Given some finite sequence of steps $s^L$, the loop function (4.1) will return the number such that, after taking those steps in the Collatz function, will return to itself.

The function returns a fraction, where the numerator and denominator are both integers. Thus, it will always return a rational value. Thus, an irrational value will never return to itself when iterated on the Collatz function.

> Theorem 5.4, rational loops:
>
> Every member of a loop in the Collatz function is rational. Irrational values will never return to themselves when iterated through the Collatz function.

### 5.5. Denominator Preservation

The parity of a rational number is determined by the parity of the numerator when the ratio is in its simplest form.

When iterating a rational number through the Collatz function, the even step will never change the denominator of the ratio because the numerator is even. The odd step will change the denominator if and only if the denominator is a multiple of 3.

> Theorem 5.5, denominator preservation
>
> When a rational number is iterated through the rational Collatz function, the denominator of the ratio when expressed in its simplest form will not change, unless the denominator is a multiple of 3.
>
> If the denominator is a multiple of 3, the factors of 3 will be canceled out with each iteration.

### 5.6. Rational Divergence

If there exists a rational number which undergoes an infinite unrepeating sequence of steps, the sequence will never include the same number twice. Because the denominator is not allowed to change (5.5), the numerator must diverge by the pigeonhole principle.

> Theorem 5.6, rational divergence
>
> If a rational number undergoes an infinite unrepeating sequence of steps, it must diverge.

## 6. Density Lower Bound

Considering again the sequence inverter function:

$\begin{align} \mathrm{Inverter}\left(s^{\infty}\right) & = \sum_{n=0}^{\infty} \frac{-1}{3^{n+1}} \prod_{i=0}^{n-1} 2^{s_i} \notag \end{align}$

With every term in the infinite series being a ratio of powers with the same sign, the series will converge if the denominator grows faster than the numerator, and diverge in the case where the numerator grows at the same speed as or faster than the denominator.

For sequences with a well-defined density, the numerator grows at the same speed as the denominator when the density is $\mathrm{log}_2\left(3\right)$. Thus, the series converges if the density is less than $\mathrm{log}_2\left(3\right)$, and it diverges if the density is equal to or greater than $\mathrm{log}_2\left(3\right)$.

For sequences without a well-defined density (e.g. unrepeating sequences where the density has cyclic behavior in the limit), only the relative growth of the numerator and denominator need to be considered for the purposes of this paper.

The conjecture is concerned with positive integers only. Given each term in the series is negative, the infinite series may only produce a positive value if the series diverges, and 2-adics are used to compute the true value.

Thus:

> Theorem 6.1, density lower bound
>
> All positive integers, when iterated through the Collatz function, undergo sequences which cause the sequence inverter function to diverge. If the sequence has a well-defined density, that density must be equal to or greater than $\mathrm{log}_2\left(3\right)$.

## 7. Derivation of the Average Step Size Function

We will derive a function which takes a number $x$ and the sequence $s^L$ which proceeds from $x$ when iterated through the Collatz function, and returns the average step size of each iteration.

We will define a single step size as the difference between $\mathrm{Collatz}\left(x\right)$ iterated until the next odd value, and $x$:

> Definition 7.1, the step size function:
>
> $\begin{align} \mathrm{Step}\left(x, s^L, i\right) = \frac{3x + 1}{2^{s_i}} - x \notag \end{align}$

Taking the average of several consecutive steps amounts to taking the difference between the resulting value after said steps and the starting value, then dividing by the number of steps.

> Proof 7.1, the average step size function:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^L\right) & = \frac{\frac{\frac{\frac{\frac{3x + 1}{2^{s_0}}3 + 1}{2^{s_1}} \ldots 3 + 1}{2^{s_{L-2}}}3 + 1}{2^{s_{L-1}}} - x}{L} \notag \\ & = \frac{\frac{\frac{\frac{\frac{3^Lx + 3^{L-1}}{2^{s_0}} + 3^{L-2}}{2^{s_1}} \ldots  + 3}{2^{s_{L-2}}} + 1}{2^{s_{L-1}}} - x}{L} \notag \end{align}$
>
> $\begin{align} & = \frac{\frac{3^L}{2^{s_0 + s_1 \ldots s_{L-1}}}x + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} \ldots \frac{3}{2^{s_{L-2} + s_{L-1}}} + \frac{1}{2^{s_{L-1}}} - x}{L} \notag \\ & = \frac{\frac{3^L - 2^{s_0 + s_1 \ldots s_{L-1}}}{2^{s_0 + s_1 \ldots s_{L-1}}}x + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} \ldots \frac{3}{2^{s_{L-2} + s_{L-1}}} + \frac{1}{2^{s_{L-1}}}}{L} \notag \end{align}$
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^L\right) & = \frac{\frac{3^{L} - 2^{\mathrm{W}\left(s^L\right)}}{2^{\mathrm{W}\left(s^L\right)}}x + \sum_{n=0}^{L-1}\frac{3^n}{\prod_{i=L-1-n}^{L-1}2^{s_i}}}{L} \notag \end{align}$

## 8. Limiting Behavior of the Average Step Size Function

We will extend the sequences to infinite length and derive the limiting behavior of the average step sizes in the different possible cases.

The lower bound of $\prod_{i=L-1-n}^{L-1}2^{s_i}$ will be set to $\infty - n$ instead of $\infty - 1 - n$ because the upper bound of its containing sum is $L-1$, not $L$.

> Proof 8.1, average step sizes of infinite sequences with high density:
>
> For sequences with a density greater than $\mathrm{log}_2\left(3\right)$, or otherwise where $2^{\mathrm{W}\left(s^L\right)}$ grows faster than $3^L$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{\frac{3^{\infty} - 2^{\mathrm{W}\left(s^{\infty}\right)}}{2^{\mathrm{W}\left(s^{\infty}\right)}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \\ & = \frac{\frac{3^{\infty} - 2^{\infty}}{2^{\infty}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> As $2^{\mathrm{W}\left(s^L\right)}$ grows faster than $3^L$, $\frac{3^{L} - 2^{\mathrm{W}\left(s^L\right)}}{2^{\mathrm{W}\left(s^L\right)}}$ approaches $-1$ as $L$ approaches $\infty$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{-x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> The denominator of each term grows faster than the numerator, so the terms of the series $\sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}$ become vanishingly small as $n$ approaches $\infty$, meaning the series converges to some finite value $f$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{-x + f}{\infty} \notag \end{align}$
>
> The numerator is finite while the denominator is infinite. Thus, sequences with a density greater than $\mathrm{log}_2\left(3\right)$, or otherwise where $2^{\mathrm{W}\left(s^L\right)}$ grows faster than $3^L$, converge to $0$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = 0 \notag \end{align}$

> Proof 8.2, average step size of infinite sequences with low density:
>
> For sequences with a density less than $\mathrm{log}_2\left(3\right)$, or otherwise where $2^{\mathrm{W}\left(s^L\right)}$ grows slower than $3^L$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{\frac{3^{\infty} - 2^{\mathrm{W}\left(s^{\infty}\right)}}{2^{\mathrm{W}\left(s^{\infty}\right)}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \\ & = \frac{\frac{3^{\infty} - 2^{\infty}}{2^{\infty}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> As $2^{\mathrm{W}\left(s^L\right)}$ grows slower than $3^L$, $\frac{3^{L} - 2^{\mathrm{W}\left(s^L\right)}}{2^{\mathrm{W}\left(s^L\right)}}$ approaches $\infty$ as $L$ approaches $\infty$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{{\infty}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> The denominator of each term grows slower than the numerator, so the terms of the series $\sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}$ diverge as $n$ approaches $\infty$, meaning the series diverges to $\infty$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{{\infty}x + \infty}{\infty} \notag \end{align}$
>
> If $x$ is equal to or greater than $0$, this will diverge to $\infty$. If $x$ is negative, it will either converge to some finite value or diverge to $\infty$ depending on the particular sequence.

> Proof 8.3, average step size of infinite sequences with balanced density:
>
> For sequences with a density equal to $\mathrm{log}_2\left(3\right)$, or otherwise where $2^{\mathrm{W}\left(s^L\right)}$ grows at the same rate as $3^L$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{\frac{3^{\infty} - 2^{\mathrm{W}\left(s^{\infty}\right)}}{2^{\mathrm{W}\left(s^{\infty}\right)}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \\ & = \frac{\frac{3^{\infty} - 2^{\infty}}{2^{\infty}}x + \sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> As $2^{\mathrm{W}\left(s^L\right)}$ grows at the same rate as $3^L$, $\frac{3^{L} - 2^{\mathrm{W}\left(s^L\right)}}{2^{\mathrm{W}\left(s^L\right)}}$ approaches $0$ as $L$ approaches $\infty$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{\sum_{n=0}^{\infty}\frac{3^n}{\prod_{i=\infty-n}^{\infty}2^{s_i}}}{\infty} \notag \end{align}$
>
> The numerator and the denominator in each term grow at the same rate. Thus, the terms approach some finite value as $n$ approaches $\infty$. The numerator has one less factor than the denominator in each of the terms. Because they grow at the same rate, they differ by a factor of $3$. Thus, the terms approach $\frac{1}{3}$ as $n$ approaches $\infty$.
>
> There is one term for each step in the sequence, and this is divided by the length of the sequence. Thus, sequences with a density equal to $\mathrm{log}_2\left(3\right)$, or otherwise where $2^{\mathrm{W}\left(s^L\right)}$ grows at the same rate $3^L$, converge to $\frac{1}{3}$:
>
> $\begin{align} \mathrm{AverageStep}\left(x, s^{\infty}\right) & = \frac{1}{3} \notag \end{align}$

## 9. The Average Step Sizes of Looped and Divergent Sequences

For a given repeating sequence, the steps before the loop are finite, so they have no contribution to the average step size when carried out to the limit. Within the loop, every movement in one direction must be perfectly canceled in the other direction to return to where it started.

Thus:

> Theorem 9.1, average step size of repeating sequences:
>
> The average step size of an infinite repeating sequence is $0$.

For a given divergent sequence of positive integers starting at some number $n$, the sequence cannot contain the same number twice. Thus, all the finitely many numbers less than $n$ will be exhausted in the limit and do not contribute to the average step size of the sequence. The slowest the sequence may diverge is by iterating through all the odd numbers greater than $n$ in any order.

Thus:

> Theorem 9.2, average step size of divergent sequences:
>
> The average step size of an infinite divergent sequence of positive integers must be at least $2$.

From theorem 6.1, all positive sequences must have a density equal to or greater than $\mathrm{log}_2\left(3\right)$, or otherwise $2^{\mathrm{W}\left(s^L\right)}$ must grow at the same rate as or faster than $3^L$.

For sequences with density greater than $\mathrm{log}_2\left(3\right)$, proof 8.1 requires the average step size to be $0$. This is less than the minimum average step size of $2$ required for a divergent sequence of positive integers. Thus, no divergence sequence of positive integers with density greater than $\mathrm{log}_2\left(3\right)$ exists.

For sequences with density equal to $\mathrm{log}_2\left(3\right)$, proof 8.3 requires the average step size to be $\frac{1}{3}$. This is less than the minimum average step size of $2$ required for a divergent sequence of positive integers. Thus, no divergence sequence of positive integers with density equal to $\mathrm{log}_2\left(3\right)$ exists.

Thus:

> Theorem 9.3, divergent positive integer sequences:
>
> No positive integer sequence exists that diverges.

For sequences with density equal to $\mathrm{log}_2\left(3\right)$, proof 8.3 requires the average step size to be $\frac{1}{3}$. This is not the required $0$ for a repeating sequence. Thus, no repeating sequence with density equal to $\mathrm{log}_2\left(3\right)$ exists.

Theorem 5.6 requires that an integer sequence must either loop or diverge. Theorem 9.3 requires that positive integer divergent sequences do not exist.

Thus:

> Theorem 9.4, repeating positive integer sequences:
>
> All positive integers belong to looped sequences.

## 10. Conclusion

Because all positive integers fall into loops, all positive integers have a maximum size that they will reach, and they are thus bounded.

If the reasoning in this paper is sound, then the matter of divergence is settled, and half of the Collatz conjecture is solved. All that remains is the matter of looped sequences, and whether there are any other sequences in the positive integers besides the loop containing 1.

## 11. References

- Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture
- P-adic numbers: https://en.wikipedia.org/wiki/P-adic_number
# The T Sum Equation

This proof was part of research into the loop problem as part of the original paper which has been postponed until later.

## 1. The T Sum Equation

> Proof 1.1, the T sum equation:
>
> Given a number $x$ which undergoes sequence $s^L$, $3x + 1$ divides by $2$ $s_0$ times. Thus, $3x + 1$ is divisible by $2^{s_0}$. This divisibility holds after arbitrarily many steps.
>
> $\begin{align} \frac{\frac{\frac{\frac{3x + 1}{2^{s_0}}3 + 1}{2^{s_1}} \ldots 3 + 1}{2^{s_{L-2}}}3 + 1}{2^{s_{L-1}}}3 + 1 & \equiv 0 \left(\text{mod } 2^{s_L}\right) \notag \\ \frac{\frac{\frac{\frac{3^Lx + 3^{L-1}}{2^{s_0}} + 3^{L-2}}{2^{s_1}} \ldots + 3^2}{2^{s_{L-2}}} + 3}{2^{s_{L-1}}} + 1 & \equiv 0 \left(\text{mod } 2^{s_L}\right) \notag \end{align}$
>
> $\begin{align} \frac{3^Lx}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^{L-1}}{2^{s_0 + s_1 \ldots s_{L-1}}} + \frac{3^{L-2}}{2^{s_1 \ldots s_{L-1}}} \ldots \frac{3}{2^{s_{L-1}}} + 1 & \equiv 0 \left(\text{mod } 2^{s_L}\right) \notag \end{align}$
>
> We will multiply both sides of the equation by $2^{s_0 + s_1 \ldots s_{L-1}}$. We will be multiplying the modulus by the same.
>
> $\begin{align} 3^Lx + 3^{L-1} + 3^{L-2} \cdot 2^{s_0} \ldots 3 \cdot 2^{s_0 + s_1 \ldots s_{L-2}} + 2^{s_0 + s_1 \ldots s_{L-1}} & \equiv 0 \left(\text{mod } 2^{s_0 + s_1 \ldots s_L}\right) \notag \end{align}$
>
> $\begin{align} 3^{L-1} + 3^{L-2} \cdot 2^{s_0} \ldots 3 \cdot 2^{s_0 + s_1 \ldots s_{L-2}} + 2^{s_0 + s_1 \ldots s_{L-1}} & \equiv -3^Lx \left(\text{mod } 2^{s_0 + s_1 \ldots s_L}\right) \notag \end{align}$
>
> The factors of $3$ can be extracted from each term so that the left side can be constructed incrementally instead of summing together very large terms.
>
> $\begin{align} \left(\left(3 + 2^{s_0}\right)3 + 2^{s_0 + s_1} \ldots \right)3 + 2^{s_0 + s_1 \ldots s_{L-1}} & \equiv -3^Lx \left(\text{mod } 2^{s_0 + s_1 \ldots s_L}\right) \notag \end{align}$
>
> Alternatively, the terms can be collected into sums and products:
>
> $\begin{align} \sum_{n=0}^{L-1} 3^{L-1-n} \prod_{i=0}^{n-1} 2^{s_i} & \equiv -3^Lx \left(\text{mod } 2^{\mathrm{W}\left(s^L\right) + s_L}\right) \notag \end{align}$
>
> The left side is equivalent to the T sum function from proof 4.1:
>
> $\begin{align} \mathrm{T_{Sum}}\left(s^L\right) & \equiv -3^Lx \left(\text{mod } 2^{\mathrm{W}\left(s^L\right) + s_L}\right) \notag \end{align}$
>
> We will extend it to sequences of infinite length.
>
> $\begin{align} \mathrm{T_{Sum}}\left(s^{\infty}\right) & \equiv -3^{\infty}x \left(\text{mod } 2^{\mathrm{W}\left(s^{\infty}\right) + s_{\infty}}\right) \notag \\ \mathrm{T_{Sum}}\left(s^{\infty}\right) & \equiv -3^{\infty}x \left(\text{mod } 2^{\infty}\right) \notag \end{align}$
>
> We will use 2-adics when using this equation. A modulus of $2^{\infty}$ is equivalent to both sides of the equation being truly equal, not merely congruent.
>
> $\begin{align} \mathrm{T_{Sum}}\left(s^{\infty}\right) & = -3^{\infty}x \notag \end{align}$

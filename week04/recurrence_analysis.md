# Recurrence analysis

In divide & conquer problems, $T(n)$ is the time required to solve a problem of size $n$. By breaking the problem into $r$ smaller problems scaled by $1/c$, we can express the solution time as

$$
T(n) = r\, T\left (\frac{n}{c} \right) + f(n)
$$

Here $f(n)

We can also break a problem of size $n/c$ into $r$ smaller problems, scaled down by $1/c$ and find the time it takes to solve them.

$$
T\left (\frac{n}{c} \right) = rT \left (\frac{n}{c^2} \right) + f\left (\frac{n}{c} \right)
$$

Substituting for $T(n/c)$ in the expression for $T(n)$ gives us

$$
\begin{align}
T(n) & = r\, \left [ rT \left (\frac{n}{c^2} \right) + f\left (\frac{n}{c} \right) \right ] + f(n) \\
     & = r^2\,T \left (\frac{n}{c^2} \right) + r\,f\left (\frac{n}{c} \right) + f(n)
\end{align}
$$

In the expression above we can reevaluate $T \left ({n}/{c^2} \right)$ in terms of smaller problems scaled down, again, by $1/c$ as $rT \left ({n}/{c^3} \right) + f \left ({n}/{c^2} \right)$ and substitute in the expression for $T(n)$:

$$
\begin{align}
T(n) & = r^2\,T \left (\frac{n}{c^2} \right) + r\,f\left (\frac{n}{c} \right) + f(n) \\
     & = r^2 \left[ rT \left (\frac{n}{c^3} \right) + f \left (\frac{n}{c^2} \right) \right ] + r\,f\left (\frac{n}{c} \right) + f(n) \\
     & = r^3 T \left (\frac{n}{c^3} \right) + r^2 f \left (\frac{n}{c^2} \right)  + r\,f\left (\frac{n}{c} \right) + f(n) 
\end{align}
$$

We can keep scaling problems down, resulting to a seemingly endless and useless expression:

$$
\begin{align}
T(n) = r^L \, T\left(\frac{n}{c^{L}}\right )
     + r^{L-1} \, f \left(\frac{n}{c^{L-1}}\right )
     + r^{L-2} \, f \left(\frac{n}{c^{L-2}}\right )
     + \ldots
     + r^{2} \, f \left(\frac{n}{c^{2}}\right )
     + r^1 \, f \left(\frac{n}{c^1}\right )
     + r^{0} \, f \left(\frac{n}{c^{0}}\right )
\end{align}
$$

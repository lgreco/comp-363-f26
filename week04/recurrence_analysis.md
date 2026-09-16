# Recurrence analysis

In divide & conquer problems, $T(n)$ is the time required to solve a problem of size $n$. By breaking the problem into $r$ smaller problems scaled by $1/c$, we can express the solution time as

$$
T(n) = r\, T\left (\frac{n}{c} \right) + f(n)
$$

Here $f(n)$ is a fixed cost associated with the scaling down of the problem and other related operations. We do not quite know the cost of these operations but it is reasonable to *assume* that $f(n)\in\mathcal O(n^d)$ and for that matter, $f(n)=n^d$.

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
\begin{align*}
T(n) & = r^L \ T\left(\frac{n}{c^{L}}\right )
     + r^{L-1} \ f \left(\frac{n}{c^{L-1}}\right )
     + r^{L-2} \ f \left(\frac{n}{c^{L-2}}\right )
     + \ldots
     + r^{2} \ f \left(\frac{n}{c^{2}}\right )
     + r^1 \ f \left(\frac{n}{c^1}\right )
     + r^{0} \ f \left(\frac{n}{c^{0}}\right ) \\ \\
     & =  r^L \ T\left(\frac{n}{c^{L}}\right ) 
       + \sum_{k=0}^{L-1}r^k\ f \left(\frac{n}{c^{k}}\right ) 
\end{align*}
$$

This is still an endless expression, so let's find when it stops. As we are scaling the problems by a factor $1/c$ at each iteration, at some point we reach a subproblem so small that it cannot be scaled any further. For example, in *mergesort* we keep dividing an array into halves until we end up with a bunch of single element arrays that can no longer be divided. In mathematical terms 
$T\left(\dfrac{n}{c^{L}}\right )=T(1)$. Therefore 
 $\dfrac{n}{c^L}=1$
 and $L=\log_c n$. And so we can write the total time as

$$
\begin{align*}
T(n) & 
     & =  r^L \ T(1) 
       + \sum_{k=0}^{L-1}r^k\ f \left(\frac{n}{c^{k}}\right ) 
\end{align*}
$$

Knowning that in general $T(n) = T(n/c) + f(n)$ and also that $T(1)$ cannot be scaled further, i.e., $T(1/c) = 0$, we have $T(1) = f(1)$ and substituting above,



$$
\begin{align*}
T(n)  
     & =  r^L \ f(1) 
       + \sum_{k=0}^{L-1}r^k\ f \left(\frac{n}{c^{k}}\right ) && (\text{remember that}\ 1=\frac{n}{c^L}) \\
         
     & =  r^L \ f\left(\frac{n}{c^L}
     \right) 
       + \sum_{k=0}^{L-1}r^k\ f \left(\frac{n}{c^{k}}\right )  && (\text{wrap the first term into the sum})  \\
     & =  \sum_{k=0}^{L}r^k\ f \left(\frac{n}{c^{k}}\right )
\end{align*}
$$

Now we have an expression that is no longer endless (it has $1+\log_cn$ terms), but still looks useless. Let's find some good use for it, by considering three distinct scenarios for its terms $r^k\ f \left(\frac{n}{c^{k}}\right )$

## Terms are equal-ish

This scenario assumes

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) = r^1\ f \left(\frac{n}{c^{1}}\right ) = \ldots = r^L\ f \left(\frac{n}{c^{L}}\right )
$$

## Terms are increasing

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) > r^1\ f \left(\frac{n}{c^{1}}\right ) > \ldots > r^L\ f \left(\frac{n}{c^{L}}\right )
$$

## Terms are decreasing

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) < r^1\ f \left(\frac{n}{c^{1}}\right ) < \ldots < r^L\ f \left(\frac{n}{c^{L}}\right )
$$

## The Master Theorem

## Multiplication

Consider two integer numbers $x, y$ each with $n$ digits, where is a power of two, $n=2^p$. Their product $xy$ is also an integer number with $2n-1$ or $2n$ digits.
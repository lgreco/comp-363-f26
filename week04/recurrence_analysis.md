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
+ \sum_{k=0}^{L-1}r^k\ f \left(\frac{n}{c^{k}}\right )  && (\text{wrap the first term into the sum}) \\
 & =  \sum_{k=0}^{L}r^k\ f \left(\frac{n}{c^{k}}\right )
\end{align*}
$$

Now we have an expression that is no longer endless (it has $1+\log_cn$ terms), but still looks useless. Let's find some good use for it, by considering three distinct scenarios for its terms $r^k\ f \left(\dfrac{n}{c^{k}}\right )$

## Terms are equal-ish

This scenario assumes

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) = r^1\ f \left(\frac{n}{c^{1}}\right ) = \ldots = r^L\ f \left(\frac{n}{c^{L}}\right )
$$

Focusing on the two first terms, gives us the condition under which the terms of the sum are equal.

$$
\begin{align*}
r^0\ f \left(\frac{n}{c^{0}}\right ) & = r^1\ f \left(\frac{n}{c^{1}}\right ) && (\text{simplify exponents, e.g.}\ r^0=1) \\
f(n) & = rf \left(\frac{n}{c}\right ) && (\text{use}\ f(n)=n^d) \\
n^d & = r \left(\frac{n}{c}\right )^d  && (\text{cancel out terms on both sides}) \\
1 & = \frac{r}{c^d} && (\text{multiply both sides by}\ c^d) \\ 
r &= c^d
\end{align*}
$$

If this condition $r=c^d$ is observed, then all terms of the sum are the same and therefore,

$$
\begin{align*}
T(n) & = \sum_{k=0}^{L}r^k\ f \left(\frac{n}{c^{k}}\right ) && (\text{replace all terms with first term } r^0\ f \left(\frac{n}{c^{0}}\right )) \\
     & = \sum_{k=0}^{L} f \left(n\right )&& (\text{sum has } L+1\text{ terms}) \\
     & = (L+1) f(n) && (L+1\approx L\text{ for large }L) \\
     & = Lf(n) && (\text{switch terms around and replace } f) \\
     & = n^d L && (\text{substitute } L=\log_cn) \\
     & = n^d \log_c n
\end{align*}
$$

## Terms are increasing

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) > r^1\ f \left(\frac{n}{c^{1}}\right ) > \ldots > r^L\ f \left(\frac{n}{c^{L}}\right )
$$

In this scenario, the dominant term of the sum is the last one. For sufficiently large values of $n$, we can argue that

$$
\begin{align*}
T(n) & \approx r^L\ f \left(\frac{n}{c^{L}}\right ) && (n/c^L=1) \\
     & = r^{L}f(1) && (f(1)=1,\  L=\log_cn) \\
     & = r^{\log_cn} && (\text{use change-of-base }\log_cn =\frac{\ln n}{\ln c}) \\
     & = n^{\log_cr}
\end{align*}
$$

The condition for this situation can be derived by the first two terms of the sum, for which we know

$$
\begin{align*}
r^0\ f \left(\frac{n}{c^{0}}\right ) & > r^1\ f \left(\frac{n}{c^{1}}\right ) \\
f(n) & > r f \left(\frac{n}{c^{1}}\right ) \\
n^d & > r\left(\frac{n}{c^{1}}\right )^d \\
1 & > \frac{r}{c^{d}} \\
r & < c^d
\end{align*}
$$

## Terms are decreasing

$$
r^0\ f \left(\frac{n}{c^{0}}\right ) < r^1\ f \left(\frac{n}{c^{1}}\right ) < \ldots < r^L\ f \left(\frac{n}{c^{L}}\right )
$$

The dominant term in this scenario is the first term and we can write

$$
\begin{align*}
T(n) & \approx r^0\ f \left(\frac{n}{c^{0}}\right ) = f(n) = n^d
\end{align*}
$$

The condition for this scenario is obtained from

$$
\begin{align*}
r^0\ f \left(\frac{n}{c^{0}}\right ) & < r^1\ f \left(\frac{n}{c^{1}}\right ) \\
n^d & < r\left(\frac{n}{c}\right )^d \\
1 <\frac{r}{c^d} \\
r > c^d
\end{align*}
$$



## The Master Theorem

The three cases above comprise the *Master Theorem* for divide and conquer problem whose timing is a recurrence of the form $T(n)=rT(n/c)+f(n)$, with $f(n)=n^d$. If we know the values $r$, $c$, and $d$, we can determine the actual time as

$$
T(n) \in \begin{cases} 
\mathcal O \left( n^d\log_cn\ \right ) & \text{when } & r & = & c^d \\
\mathcal O \left( n^{\log_cr} \right ) & \text{when } & r & < & c^d \\
\mathcal O \left( n^d         \right ) & \text{when } & r & > & c^d
\end{cases}
$$

# Multiplication

Consider two integer numbers $x, y$ each with $n$ digits, where is a power of two, $n=2^p$. Their product $xy$ is also an integer number with $2n-1$ or $2n$ digits. If the numbers are sufficiently large, a computer may not be able to represent them using internal arithmetic. And yet programming languages like Python and Java routinely handle numbers much larger than what they can represent internally. How?

Let's assume that we have a computer for which $x=1234$ and $y=5678$ are "large" numbers. Such computers where the state of the art in the 1980s, using 8-bit processor whose internal integer arithmetic only covers numbers in the interval $[-128,127]$.

The numbers can be split into left and right halves as

$$
\begin{align*}
x & = 12 \times 10^2 + 34 \times 10^0 \\
y & = 56 \times 10^2 + 78 \times 10^0
\end{align*}
$$
and their product can be rewritten as


$$
\begin{align*}
xy & = \left ( 12 \times 10^2 + 34 \times 10^0 \right ) \times 
       \left ( 56 \times 10^2 + 78 \times 10^0 \right ) \\
   & = (12)\times(56)\times 10^4 + \left [ (12)\times(78)+(34)\times(56) \right]\times 10^2 + (34)\times (78)\times 10^0
\end{align*}
$$

Multiplications by a power of 10 are trivial because all we need to do is shift the digits to the left by as many places as the exponent of 10. The remaining products can be decomposed in similar fashion. For example


$$
\begin{align*}
(34) \times (78) & = (3\times 10^1 + 4\times 10^0) \times (7\times 10^1 + 8\times 10^0) \\
                 & = (3)\times(7)\times 10^2 + [(3)\times (8)+(4)\times(7)]\times 10^1 + (4)\times(8)\times 10^0\\
                 & = 21\times 10^2 + (24+28)\times 10^1 + 32\times 10^0 \\
                 & = 2100 +520 + 32 = \mathbf{2652}\\
\end{align*}
$$
In the step above, all products are single-digit multiplications and therefore trivial to compute.

In general, two numbers $x,y$ with $n$ digits each can be written as


$$
\begin{align*}
x & = A \times 10^{n/2} + B \\
y & = C \times 10^{n/2} + D
\end{align*}
$$
Assuming that $n=2^p$ (a power of two), then $a,b$ are the left and right halves of $x$, and $c,d$ the left and right halves of $y$. Using this representation, the product can be written as

$$
\begin{align*}
xy & = (A \times 10^{n/2} + B) \times (C \times 10^{n/2} + D) \\
   & = AC\times 10^n+(BC+AD)\times 10^{n/2} + DB
\end{align*}
$$

The products above, $AC$, $AD$, $BC$, and $BD$ can be further decomposed using the similar technique and we can continue spliting the operants in halves until we end up with the simple single digit multiplications as in the example earlier.

Because $x$ and $y$ are big numbers than cannot be represented as `int` data types, we opt to represent them as strings; for example

```python
x: str = '1234'
y: str = '5678'
```
Thus, splitting them in left and right halves becomes a trivial string slicing assignment.
```python
n = len(x)    # assume len(x) == len(y) > 0
mid = n // 2  # remember n is power of 2
A = x[0:mid]  # left half of x
B = x[mid:n]  # right half of x
C = y[0:mid]  # left half of y
D = y[mid:n]  # right half of y
```

Decomposing the product of two numbers $n$ digits long to four products of two numbers, $n/2$ digits long, implies a recurrence of the form

$$
T(n) = 4T\left (\frac{n}{2} \right ) +f(n)
$$

Here, $r=4$ and $c=2$. In order to apply the Master Theorem, first we need to establish that $f(n)=n^d$ and then estimate the value of $d$.

In the product
$$
\begin{align*}
xy & = AC\times 10^n+(BC+AD)\times 10^{n/2} + DB
\end{align*}
$$
we split $x$ and $y$ into halves. Assuming these numbers are represented by strings of length $n$, the spliting can be done as simply as:
```python
left_half = ''
right_half = ''
n = len(string)
mid = n//2
for i in range(n):
     digit = string[i]
     if i < mid:
          left_half += digit
     else:
          right_half += digit
```
Of course, in real Python this process is done with `string[:mid]` and `string[mid:]` slicing. But regardless of implementation, the slicing requires as many steps as the length of the string and therefore, $f(n)=n$. So, $d=1$.

For this recurrence, we have $r > c^d$ because $4>2^1$ and from the Master Theorem we get that $T(n)\in\mathcal O(n^{\log_cr})= \mathcal O(n^{\log_24}) = \mathcal O(n^{2})$

A simple algebraic manipulation can lead to better performance. In 1960, while attending a workshop on computational complexity, Anatoly Karatsuba challenged his professor's assumptions about recursive multiplication. His professor was Andrey Kolmogorov, one of the most influential mathematicians of the 20th century. Kolmogorov believed that $\mathcal O (n^2)$ was as good as it gets for multiplication.

Karatsuba proposed that instead of splitting the product into four subproblems, it could be done with three:

$$
\begin{align*}
xy & = AC\times 10^n+{\color{maroon}{(BC+AD)}}\times 10^{n/2} + DB && (\text{classic solution}) \\
   & = AC\times 10^n+{\color{maroon}{((A+B)(C+D)-BC-AD)}}\times 10^{n/2} + DB && (\text{Karatsuba's solution})
\end{align*}
$$

It is trivial to show that $(A+B)(C+D)-AC-BD=BC+AD$. And by using this simple substitution Karatsuba reduced the problem's $r$ from 4 to 3. We are still in the $r>c^d$ part of the Master Theorem, and the time it takes for Karatsuba's product to compute is $\mathcal O (n^{\log_{2}{{\color{red}3}}}) = \mathcal O (n^{{1.58}} )$. 

Going from $n^2$ to $n^{1.58}$ may not seem a big deal, except it is. Consider two numbers with 1024 digits each. Using the classic multiplication, the time to complete the operation is $\mathcal O(1024^2)=\mathcal O(1,048,576)$. Using Karatsuba's technique, the required time is  $\mathcal O(1024^{1.58})=\mathcal O(57,052)$. That's a significant improvement.
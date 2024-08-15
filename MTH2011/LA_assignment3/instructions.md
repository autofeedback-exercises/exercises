LA assignment 3: computer questions

Q1. Show that an arbitrary matrix in $M_2(\mathbb{R})$ can be expressed as a linear combination of:

$$m_0 = \left(
\begin{array}{ccc}
1 & 0 \\ 0 & 1
\end{array}
\right), \; \; 
m_1= \left(
\begin{array}{ccc}
1 & 0 \\ 0 & -1
\end{array}
\right), \; \; 
m_2 = \left(
\begin{array}{ccc}
0 & 1 \\ 1 & 0
\end{array}
\right), \; \; 
m_3 = \left(
\begin{array}{ccc}
0 & 1 \\ -1 & 0
\end{array}
\right).$$

Specifically, determine the values of the coefficients $w, x, y$ and $z$, such that

$$w\cdot m_0 + x\cdot m_1 + y\cdot m_2 + z\cdot m_3 = 
\left(
\begin{array}{ccc}
a & b \\ c & d
\end{array}
\right)$$

Q2. Show that the vectors, $(1,2,0,0)$, $(0,-1,1,1)$ and $2,0,1,-1$ are linearly independent. **Please be wary with this one**:, `sympy` has a little bug that means that `sy.solve` does not treat matrices and arrays the same way. The best way around this is to use `sy.Matrix` for your vectors, and then use an expression (which is assumed to be equal to zero) in `sy.solve`, rather than using a `sy.Eq` (which will break `sympy`). 

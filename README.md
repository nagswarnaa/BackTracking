## Dynamic Programming

### Optimal substructure
Optimal substructure is a principle mainly used in the context of dynamic programming and some greedy algorithms. It refers to a situation where the optimal solution to a problem can be constructed efficiently from optimal solutions to its subproblems.

This property is crucial because it ensures that once you've found the optimal solutions to the subproblems, you can combine them to solve the overall problem. In other words, a problem exhibits optimal substructure if an optimal solution to the entire problem contains within it optimal solutions to the subproblems.

For example, in the shortest path problem, if a shortest path from point A to point C goes through point B, then the segment of the path from A to B must itself be the shortest path from A to B. This characteristic allows algorithms like Dijkstra's and Floyd-Warshall to efficiently compute shortest paths by systematically building on solutions to smaller instances of the same problem.

Let's consider the example of the Fibonacci sequence, which is a classic case demonstrating optimal substructure, often used in teaching dynamic programming.

### Problem Statement:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is, the sequence starts 0, 1, 1, 2, 3, 5, 8, 13, ...

### Task:
Compute the \( n \)-th Fibonacci number.

### Explanation with Optimal Substructure:
The Fibonacci sequence is defined recursively as:
\[ F(n) = F(n-1) + F(n-2) \]
with base cases:
\[ F(0) = 0 \]
\[ F(1) = 1 \]

Here, the optimal substructure property is evident because:
- The solution to finding \( F(n) \) (the \( n \)-th Fibonacci number) can be derived by summing up the solutions to the subproblems \( F(n-1) \) and \( F(n-2) \).
- This property suggests that if we know the optimal solutions to \( F(n-1) \) and \( F(n-2) \), we can compute \( F(n) \).

### Dynamic Programming Approach:
Using dynamic programming, we can store the solutions to these subproblems in a table (memoization) and use them to construct the solution to the bigger problem. Here's how it works:

1. **Initialization**: Start by storing the base cases:
   - \( F(0) = 0 \)
   - \( F(1) = 1 \)

2. **Building up solutions**:
   - For each \( i \) from 2 to \( n \), compute \( F(i) \) as \( F(i-1) + F(i-2) \) using the previously computed values stored in the table.

3. **Optimal Solution**: \( F(n) \) is the \( n \)-th Fibonacci number.

This method ensures we only compute each Fibonacci number once, making it significantly more efficient than the naive recursive approach, which computes many Fibonacci numbers multiple times.

In summary, the optimal substructure of the Fibonacci sequence allows us to build an efficient solution using dynamic programming by combining the solutions of smaller, overlapping subproblems.

Overlapping subproblems is another key concept in dynamic programming. It refers to a scenario where the same smaller problems are solved multiple times during the computation of the overall problem. This redundancy makes a naive recursive solution inefficient and justifies using dynamic programming or memoization to store the results of these subproblems.

### Example: Computing the Fibonacci Sequence

Consider the computation of the Fibonacci sequence again, where:
\[ F(n) = F(n-1) + F(n-2) \]
with initial conditions:
\[ F(0) = 0 \]
\[ F(1) = 1 \]

### Naive Recursive Approach:
When implementing a naive recursive function to compute \( F(n) \), you would typically call it like this:

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

For each non-base case, the function calls itself twice, and each of those function calls resolves into further calls. Here’s a breakdown of how the function calls expand for \( n = 5 \):

- \( F(5) \)
  - \( F(4) \) + \( F(3) \)
    - \((F(3) + F(2)) + (F(2) + F(1))\)
      - \(((F(2) + F(1)) + (F(1) + F(0))) + ((F(1) + F(0)) + 1)\)
        - etc...

Notice how \( F(2) \) is computed multiple times and each of its calculations in turn recomputes \( F(1) \) and \( F(0) \). As \( n \) increases, the number of redundant calculations grows exponentially.

### Dynamic Programming Approach (Memoization):
To address the inefficiency of recomputing the same values repeatedly, dynamic programming suggests storing these results:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

In this approach:
- Each Fibonacci number is computed once and stored in a dictionary (`memo`).
- Subsequent requests for the same Fibonacci number retrieve the value from `memo`, avoiding redundant computations.

This transformation drastically improves the efficiency, reducing the time complexity from exponential to linear in terms of the number of function calls, thanks to the reuse of results from the overlapping subproblems.

In essence, the overlapping subproblems property makes problems suitable for dynamic programming, as it ensures that efficiency gains are possible by caching and reusing solutions.

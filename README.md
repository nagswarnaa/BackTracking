# BackTracking Algorithms

Dynamic Programming Basics
Optimal substructure:
Optimal substructure is a principle mainly used in the context of dynamic programming and some greedy algorithms. It refers to a situation where the optimal solution to a problem can be constructed efficiently from optimal solutions to its subproblems.
This property is crucial because it ensures that once you've found the optimal solutions to the subproblems, you can combine them to solve the overall problem. In other words, a problem exhibits an optimal substructure if an optimal solution to the entire problem contains within it optimal solutions to the subproblems.
For example, in the shortest path problem, if a shortest path from point A to point C goes through point B, then the segment of the path from A to B must itself be the shortest path from A to B. This characteristic allows algorithms like Dijkstra's and Floyd-Warshall's to efficiently compute the shortest paths by systematically building on solutions to smaller instances of the same problem.
Let's consider the example of the Fibonacci sequence, which is a classic case demonstrating optimal substructure, often used in teaching dynamic programming.
Problem Statement:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is, the sequence starts 0, 1, 1, 2, 3, 5, 8, 13, …
Task:
Compute the n-th Fibonacci number.
Explanation with Optimal Substructure:
The Fibonacci sequence is defined recursively as:
F(n) = F(n-1) + F(n-2) 
with base cases:
F(0) = 0
F(1) = 1
Here, the optimal substructure property is evident because:
The solution to finding F(n), the n-th Fibonacci number, can be derived by summing up the solutions to the subproblems F(n-1) and F(n-2). This property suggests that if we know the optimal solutions to F(n-1) and F(n-2) , we can compute F(n).
Dynamic Programming Approach:
Using dynamic programming, we can store the solutions to these subproblems in a table (memoization) and use them to construct the solution to the bigger problem. Here's how it works:
1. Initialization: Start by storing the base cases:
F(0) = 0 
F(1) = 1
2. Building up solutions:
For each i from 2 to n , compute F(i) as F(i-1) + F(i-2) using the previously computed values stored in the table.
3. Optimal Solution: F(n) is the nth Fibonacci number.
This method ensures we only compute each Fibonacci number once, making it significantly more efficient than the naive recursive approach, which computes many Fibonacci numbers multiple times.
In summary, the optimal substructure of the Fibonacci sequence allows us to build an efficient solution using dynamic programming by combining the solutions of smaller, overlapping subproblems.

# M-Coloring Problem

## Overview
The **M-Coloring Problem** is a classic constraint-satisfaction problem in graph theory. Given an undirected graph, the goal is to determine if the vertices can be colored using at most $M$ different colors such that no two adjacent vertices share the same color.

---

## Problem Statement
Given an undirected graph with $N$ vertices (0-indexed) and $E$ edges, determine whether the graph can be colored with a maximum of $M$ colors.

### Constraints
* No two adjacent vertices (vertices connected by an edge) can have the same color.
* If a valid coloring is found, return **true**.
* If no such coloring exists within the limit of $M$ colors, return **false**.

---

## Examples

### Example 1
**Input:** - $N = 4$ (Vertices)
- $M = 3$ (Available Colors)
- $E = 5$ (Edges)
- **Edges:** `[(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]`

**Output:** `true`

**Explanation:** Consider the three colors to be {Red, Green, Blue}.
- Vertex 0 $\rightarrow$ Red
- Vertex 1 $\rightarrow$ Blue
- Vertex 2 $\rightarrow$ Green
- Vertex 3 $\rightarrow$ Blue
In this configuration, no two adjacent nodes share a color.

### Example 2
**Input:**
- $N = 3, M = 2, E = 3$
- **Edges:** `[(0, 1), (1, 2), (0, 2)]`

**Output:** `false`

**Explanation:**
This graph forms a triangle (K3). Since every vertex is connected to every other vertex, you would need at least 3 colors. With $M=2$, a valid coloring is impossible.

---

## Technical Specifications

### Input Constraints
- $1 \le N \le 20$
- $1 \le E \le \frac{N(N-1)}{2}$
- $1 \le M \le N$

### Complexity Analysis
- **Time Complexity:** $O(M^N)$. In the worst case, the algorithm tries $M$ colors for each of the $N$ vertices.
- **Space Complexity:** $O(N)$. This includes the recursion stack depth and the array used to store color assignments.

---

## Practice Challenge
**Input:** $N = 5, M = 3, E = 6$  
**Edges:** `[(0, 1), (1, 2), (0, 2), (2, 3), (2, 4), (3, 4)]`

**Is it colorable with 3 colors?**
- [x] **true**
- [ ] **false**

*Hint: This graph consists of two triangles sharing a single vertex (Vertex 2). Each triangle independently requires 3 colors.*

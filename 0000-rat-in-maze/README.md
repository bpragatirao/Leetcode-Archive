# Rat in a Maze - Problem Statement

## Description
Given a grid of dimensions $n \times n$, a rat is placed at coordinates $(0, 0)$ and wants to reach coordinates $(n-1, n-1)$. 

Find all possible paths that the rat can take to travel from the start to the destination. The rat can move in the following directions:
- **'U'**: Up
- **'D'**: Down
- **'L'**: Left
- **'R'**: Right

### Grid Rules
- A value of **0** denotes a blocked cell that the rat cannot enter.
- A value of **1** denotes a path cell that the rat can travel through.
- If the starting cell $(0, 0)$ is **0**, no paths are possible.
- **Constraint:** In any single path, no cell can be visited more than once.

---

## Constraints
- $2 \le n \le 5$
- $0 \le \text{grid}[i][j] \le 1$

---

## Examples

### Example 1
**Input:** $n = 4$
$\text{grid} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \end{bmatrix}$

**Output:** `["DDRDRR", "DRDDRR"]`

**Explanation:** 1. Path 1: $(0,0) \to (1,0) \to (2,0) \to (2,1) \to (3,1) \to (3,2) \to (3,3)$
2. Path 2: $(0,0) \to (1,0) \to (1,1) \to (2,1) \to (3,1) \to (3,2) \to (3,3)$

### Example 2
**Input:** $n = 2$
$\text{grid} = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}$

**Output:** `-1` (No valid path exists)

---

## Practice Challenge
**Input:** $n = 3$
$\text{grid} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}$

**Identify the valid path:**
1. [ ] `DDRR`
2. [ ] `DRRD`
3. [ ] `RRDD`
4. [x] `DRDR`

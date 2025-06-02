# Android Assignment - Set 2

## 📌 Overview

This repository contains solutions for the Android Assignment - Set 2, focused on algorithm design, graph theory and GPU-based rendering using Python.

---

## 🔸 Question 1: N-Queens Puzzle

**Problem**: Place `n` queens on an `n x n` chessboard so that no two queens attack each other.

**Approach**:
- Use backtracking to explore all valid placements row by row.
- Validate queen positions to ensure no conflicts on columns or diagonals.

**Run Example**:
```bash
$ python que1.py
Enter the number of queens 1 t0 9: 4
Solutions:
. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
```

---

## 🔸 Question 2: Cycle Detection in Module Dependencies

**Problem**: Given dependencies between modules (directed graph), check for circular dependencies.

**Approach**:
- Represent the graph using adjacency lists.
- Use Depth-First Search (DFS) with recursion stack tracking to detect cycles.

**Run Example**:
```bash
$ python que2.py
Example 1:
Output:
false
Example 2:
Output:
True
```

---

## 🔸 Question 3: GPU Accelerated Particle System using OpenGL

**Problem**: Simulate a fireworks or magical energy burst using GPU and OpenGL.

**Approach**:
- Use `pygame` and `PyOpenGL` for rendering.
- Particles are generated with velocity, lifetime, color fading.
- User interaction (mouse click) spawns a new burst.

> **Note**: This may require `pygame`, `PyOpenGL`, and a local machine with OpenGL support.

**Installation**:
```bash
pip install pygame PyOpenGL PyOpenGL_accelerate
```

---

## 🔸 Tools and Technologies

- Python 3
- Data Structures & Algorithms
- DFS & Graph Traversal
- Pygame + OpenGL (for Q3)


---

## 📁 File Structure

```
├── que1.py                # Question 1 solution
├── que1_answer.PNG        # Question 1 solution screenshot
├── que1.py                # Question 2 solution
├── que2.answer.PNG        # Question 2 solution screenshot
├── que3.ipynb             # Question 3 solution (GPU rendering)
├── README.md              # Assignment documentation
```

---

## 🙋 Author

- **Name**: [Vikram Abid]
- **Email**: vikramabid012@gmail.com

---



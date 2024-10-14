# Union-Find with Path Compression and Union by Weight

The Union-Find (or Disjoint Set) data structure supports the following key operations:
- **Union**: Merges two sets that contain two specified elements.
- **Find (Root)**: Determines the root of the set that contains a specified element. This is used to check if two elements are in the same set.
- **Connected**: Returns whether two elements are in the same set or not.

### Optimizations
1. **Path Compression**: When finding the root of an element, we make the path from that element to its root shorter by making all nodes on the path directly point to the root. This helps in flattening the tree structure.
   
2. **Union by Weight**: When merging two sets, the smaller tree is always connected to the root of the larger tree. This helps in reducing the tree height, making future operations faster.

---

## Time Complexity Analysis

### 2. **Root Finding (`_root(i)`)**:
   - **Time Complexity**: **O(log* N)**, where **log* N** is the iterated logarithm of N. This grows extremely slowly and is almost constant for practical purposes.

### 3. **Union (`union(p, q)`)**:
   - **Time Complexity**: **O(log* N)** for each operation, thanks to union by weight and path compression.

### 4. **Connected (`connected(p, q)`)**:
   - **Time Complexity**: **O(log* N)** since it checks the roots of both elements using path compression.

### Space Complexity:  
   - **O(N)** for maintaining the `id` and `weight` arrays.

---

## Time Complexity Summary Table

| Function            | Time Complexity  |
|---------------------|------------------|
| **Initialization**  | O(N)             |
| **_root(i)** (Find) | O(log* N)        |
| **union(p, q)**     | O(log* N)        |
| **connected(p, q)** | O(log* N)        |

---



class UF:
    """
    This class implements the Union-Find (or Disjoint Set) data structure 
    with path compression and union by weight to efficiently manage and 
    merge disjoint sets.
    """
    
    def __init__(self, size):
        """
        Initializes the Union-Find structure with a given size.
        
        - Each element is initially its own root, i.e., id[i] = i.
        - The weight array tracks the size of the trees for union optimization.
        
        Example:
        For size = 5, id = [0, 1, 2, 3, 4], weight = [1, 1, 1, 1, 1]
        """
        self.id = list(range(size)) 
        self.weight = [1] * size

    def _root(self, i):
        """
        Finds the root of element `i` with path compression.
        
        - Path compression: Every time we look for the root of `i`, we make 
          nodes in the path point directly to the root, flattening the tree 
          structure.
        
        Example:
        If id = [0, 1, 1, 3, 4], calling _root(2) will return 1 and compress
        the path.
        """
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # Path compression
            i = self.id[i]
        return i

    def union(self, p, q):
        """
        Unites the sets containing elements `p` and `q` by connecting their roots.
        
        - If they are already connected (have the same root), no union is performed.
        - The smaller tree is always connected to the larger tree based on weights.
        
        Example:
        If p=1, q=2, and their roots are different, union will connect them, 
        updating their ids and weights.
        """
        root_p = self._root(p)
        root_q = self._root(q)

        if root_p == root_q:
            return

        if self.weight[root_p] < self.weight[root_q]:
            self.id[root_p] = root_q
            self.weight[root_q] += self.weight[root_p]
        else:
            self.id[root_q] = root_p
            self.weight[root_p] += self.weight[root_q]

    def connected(self, p, q):
        """
        Checks if elements `p` and `q` are in the same set.
        
        - Returns True if `p` and `q` have the same root, meaning they are connected.
        - Returns False otherwise.
        
        Example:
        If p=1 and q=2, this function returns whether they belong to the same group.
        """
        return self._root(p) == self._root(q)


if __name__ == "__main__":
    """
    Reads input from a file, initializes the Union-Find structure,
    performs union operations, and checks for connectivity.
    
    - The first line of the file contains the number of connections (pairs).
    - Each subsequent line contains pairs of integers (p, q) that need to be connected.
    
    The function prints the final state of the `id` array after performing
    all union operations.
    """
    with open("UF.txt", 'r') as file:
        connections = int(file.readline().strip())
        max_value = 0
        pairs = []

        # Read pairs from the file and track the largest value for array size
        for _ in range(connections):
            p, q = map(int, file.readline().strip().split())
            pairs.append((p, q))
            max_value = max(max_value, p, q)

        # Initialize the Union-Find with a size based on the maximum element
        uf = UF(max_value + 1)

        # Perform union operations for all pairs
        for p, q in pairs:
            if not uf.connected(p, q):
                uf.union(p, q)

    # Print the final state of the id array
    print(uf.id)


class WeightedQuickUnionUF:
    def __init__(self, n):
        """Initializes an empty union-find data structure with n elements 0 through n-1.
        Initially, each element is in its own set."""
        if n < 0:
            raise ValueError("Number of elements must be nonnegative")
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def count_sets(self):
        """Returns the number of sets."""
        return self.count

    def find(self, p):
        """Returns the canonical element of the set containing element p."""
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def validate(self, p):
        """Validates that p is a valid index."""
        n = len(self.parent)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} is not between 0 and {n-1}")

    def connected(self, p, q):
        """Returns true if the two elements are in the same set."""
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Merges the set containing element p with the set containing element q."""
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -= 1

# Example usage
if __name__ == "__main__":
    # Assuming an input method to get n and pairs (p, q), such as user input or reading from a file.
    n = int(input("Enter the number of elements: "))
    uf = WeightedQuickUnionUF(n)
    try:
        while True:
            p, q = map(int, input("Enter a pair (p q): ").split())
            if not uf.connected(p, q):
                uf.union(p, q)
                print(f"{p} {q}")
    except EOFError:  # Use EOF to stop the loop in this example
        pass
    print(f"{uf.count_sets()} components")

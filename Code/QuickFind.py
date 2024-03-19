class QuickFindUF:
    def __init__(self, n):
        """Initializes an empty union-find data structure with n elements 0 through n-1.
        Each element is initially in its own set."""
        if n < 0:
            raise ValueError("Number of elements must be nonnegative")
        self.count = n
        self.id = list(range(n))

    def count_sets(self):
        """Returns the number of sets."""
        return self.count

    def find(self, p):
        """Returns the canonical element of the set containing element p."""
        self.validate(p)
        return self.id[p]

    def validate(self, p):
        """Validates that p is a valid index."""
        n = len(self.id)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} is not between 0 and {n-1}")

    def connected(self, p, q):
        """Returns true if the two elements are in the same set."""
        self.validate(p)
        self.validate(q)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        """Merges the set containing element p with the set containing element q."""
        self.validate(p)
        self.validate(q)
        pID = self.id[p]
        qID = self.id[q]

        if pID == qID:
            return

        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        self.count -= 1

# Example of using this class
if __name__ == "__main__":
    # This example assumes you have a way to read input n and pairs (p, q) from the user or a file.
    n = int(input("Enter the number of elements: "))
    uf = QuickFindUF(n)
    try:
        while True:
            p, q = map(int, input("Enter a pair (p q): ").split())
            if uf.find(p) != uf.find(q):
                uf.union(p, q)
                print(f"{p} {q}")
    except EOFError:  # Assuming input ends with EOF to stop the loop
        pass
    print(f"{uf.count_sets()} components")

class Node:
    def __init__(self, key, val, size):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.size = size

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.size(self.root) == 0

    def size(self, x=None):
        if x is None:
            x = self.root
        if x is None:
            return 0
        else:
            return x.size

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key, x=None):
        if x is None:
            x = self.root
        while x is not None:
            cmp = (key > x.key) - (key < x.key)
            if cmp < 0:
                x = x.left
            elif cmp > 0:
                x = x.right
            else:
                return x.val
        return None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, 1)
        cmp = (key > x.key) - (key < x.key)
        if cmp < 0:
            x.left = self._put(x.left, key, val)
        elif cmp > 0:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x

    def min(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        return self._min(self.root).key

    def _min(self, x):
        if x.left is None:
            return x
        else:
            return self._min(x.left)

    def max(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x
        else:
            return self._max(x.right)

    def deleteMin(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x

    def deleteMax(self):
        if self.isEmpty():
            raise ValueError("BST is empty")
        self.root = self._deleteMax(self.root)

    def _deleteMax(self, x):
        if x.right is None:
            return x.left
        x.right = self._deleteMax(x.right)
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None
        cmp = (key > x.key) - (key < x.key)
        if cmp < 0:
            x.left = self._delete(x.left, key)
        elif cmp > 0:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x


    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None:
            return None
        else:
            return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        cmp = (key > x.key) - (key < x.key)
        if cmp == 0:
            return x
        if cmp < 0:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self, key):
        x = self._ceiling(self.root, key)
        if x is None:
            return None
        else:
            return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        cmp = (key > x.key) - (key < x.key)
        if cmp == 0:
            return x
        if cmp > 0:
            return self._ceiling(x.right, key)
        t = self._ceiling(x.left, key)
        if t is not None:
            return t
        else:
            return x

    def select(self, rank):
        return self._select(self.root, rank).key

    def _select(self, x, rank):
        if x is None:
            return None
        leftSize = self.size(x.left)
        if leftSize > rank:
            return self._select(x.left, rank)
        elif leftSize < rank:
            return self._select(x.right, rank - leftSize - 1)
        else:
            return x

    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, x):
        if x is None:
            return 0
        cmp = (key > x.key) - (key < x.key)
        if cmp < 0:
            return self._rank(key, x.left)
        elif cmp > 0:
            return 1 + self.size(x.left) + self._rank(key, x.right)
        else:
            return self.size(x.left)


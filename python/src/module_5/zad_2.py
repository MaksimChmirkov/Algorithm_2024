class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def is_balanced(self):
        return self._is_balanced(self.root) is not None

    def _is_balanced(self, node):
        if node is None:
            return 0

        left_height = self._is_balanced(node.left)
        if left_height is None:
            return None

        right_height = self._is_balanced(node.right)
        if right_height is None:
            return None

        if abs(left_height - right_height) > 1:
            return None

        return max(left_height, right_height) + 1


numbers = list(map(int, input().split()))


tree = BinarySearchTree()
for num in numbers:
    if num == 0:
        break
    tree.insert(num)


is_balanced = tree.is_balanced()


print("YES" if is_balanced else "NO")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False


def bfs(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


def preorder(root):
    if root is None:
        return []

    return (
        [root.value]
        + preorder(root.left)
        + preorder(root.right)
    )


def inorder(root):
    if root is None:
        return []

    return (
        inorder(root.left)
        + [root.value]
        + inorder(root.right)
    )


def postorder(root):
    if root is None:
        return []

    return (
        postorder(root.left)
        + postorder(root.right)
        + [root.value]
    )


class AVLTree(BinaryTree):

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return (
            self.get_height(node.left)
            - self.get_height(node.right)
        )

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        middle = x.right

        x.right = y
        y.left = middle

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        middle = y.left

        y.left = x
        x.right = middle

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, node):
        self.update_height(node)

        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)

            return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)

            return self.left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._avl_insert(self.root, value)

    def _avl_insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._avl_insert(node.left, value)
        elif value > node.value:
            node.right = self._avl_insert(node.right, value)
        else:
            return node

        return self.rebalance(node)


print("ЗАДАНИЕ 1: БИНАРНОЕ ДЕРЕВО")

tree = BinaryTree()

for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

print("Поиск 40:", tree.search(40))
print("Поиск 100:", tree.search(100))
print()


print("ЗАДАНИЕ 2: ОБХОД В ШИРИНУ BFS")

print("BFS:", bfs(tree.root))
print()


print("ЗАДАНИЕ 3: ОБХОДЫ В ГЛУБИНУ DFS")

print("Preorder:", preorder(tree.root))
print("Inorder:", inorder(tree.root))
print("Postorder:", postorder(tree.root))
print()


print("ЗАДАНИЕ 4: AVL-ДЕРЕВО")

avl = AVLTree()

for value in [10, 20, 30, 40, 50, 25]:
    avl.insert(value)

print("Поиск 30:", avl.search(30))
print("Поиск 100:", avl.search(100))
print("Обход AVL:", bfs(avl.root))

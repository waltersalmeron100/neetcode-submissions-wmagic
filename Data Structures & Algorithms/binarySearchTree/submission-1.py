from typing import List

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return

        current = self.root

        while True:
            if key < current.key:
                if not current.left:
                    current.left = TreeNode(key, val)
                    return
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = TreeNode(key, val)
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root

        while current:
            if key == current.key:
                return current.val
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current.left:
            current = current.left

        return current.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        current = self.root
        while current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        def remove_node(node, key):
            if not node:
                return None

            if key < node.key:
                node.left = remove_node(node.left, key)
            elif key > node.key:
                node.right = remove_node(node.right, key)
            else:
                # Case 1: no left child
                if not node.left:
                    return node.right

                # Case 2: no right child
                if not node.right:
                    return node.left

                # Case 3: two children
                successor = node.right
                while successor.left:
                    successor = successor.left

                node.key = successor.key
                node.val = successor.val
                node.right = remove_node(node.right, successor.key)

            return node

        self.root = remove_node(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.key)
            inorder(node.right)

        inorder(self.root)
        return result
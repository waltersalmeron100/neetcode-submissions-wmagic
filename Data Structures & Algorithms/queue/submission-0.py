class DequeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Deque:
    
    def __init__(self):
        # Dummy Nodes
        self.head = DequeNode(-1)
        self.tail = DequeNode(-1)
        # Initialize
        self.head.right = self.tail
        self.tail.left = self.head


    def isEmpty(self) -> bool:
        return self.head.right == self.tail # Dummy Nodes
        

    def append(self, value: int) -> None:
        new_node = DequeNode(value)

        new_node.left = self.tail.left
        new_node.right = self.tail

        self.tail.left.right = new_node
        self.tail.left = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = DequeNode(value)

        new_node.left = self.head
        new_node.right = self.head.right

        self.head.right.left = new_node
        self.head.right = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last_node = self.tail.left
        popped = last_node.val

        last_node.left.right = self.tail
        self.tail.left = last_node.left

        return popped
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first_node = self.head.right
        popped = first_node.val

        first_node.right.left = self.head
        self.head.right = first_node.right

        return popped

        
        

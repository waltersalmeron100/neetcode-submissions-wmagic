class ListNode: # Helper class to visualize each node
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # Dummy Node
        self.tail = self.head

    
    def get(self, index: int) -> int:
        current = self.head.next # skips the dummy node
        i = 0 # current node

        while current: # while the node is not null
            if i == index:
                return current.val
            i += 1
            current = current.next

        return  -1


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) # initalize new head
        new_node.next = self.head.next # have the new head point the the next node
        self.head.next = new_node # dummy value points to new head

        if new_node.next is None: # sets the tail to the new node if it's the only node
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val) # initalize new tail
        self.tail.next = new_node # points previous tail to new tail
        self.tail = new_node # sets new node as the tail
        

    def remove(self, index: int) -> bool:
        current = self.head # start at dummy node
        i = 0

        while i < index and current: # this condition gets us to the node right before the one we want to remove
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail: # if we're removing the tail set the current node (node before the one we are removing) as the tail
                self.tail = current

            current.next = current.next.next # otherwise current.next now skips over the "removed" node and points at it's next node
            return True

        return False
        

    def getValues(self) -> List[int]:
        vals = []
        current = self.head.next # start after dummy node
        
        while current:
            vals.append(current.val)
            current = current.next

        return vals

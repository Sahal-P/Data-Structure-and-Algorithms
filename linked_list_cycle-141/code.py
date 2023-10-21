from typing import Optional

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_end(self, data):
        for val in range(len(data)):
            new_node = Node(data[val])
            if self.head is None:
                self.head = new_node
                continue

            current_node = self.head
            while (current_node.next):
                current_node = current_node.next

            current_node.next = new_node


linkl = SinglyLinkedList()
linkl.insert_at_end([3,2,0,-4])

cHead = linkl.head
tHead = linkl.head

while cHead:
    prev = cHead
    cHead = cHead.next
    
prev.next = tHead.next



def hasCycle(head: Optional[Node]) -> bool:
    hashSet = set()
    while head:
        hashSet.add(head)
        if head.next in hashSet:
            return True
        head = head.next
    return False
    
# Floyd’s cycle finding algorithm or Hare-Tortoise algorithm
def hasCycle_m(head: Optional[Node]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(hasCycle_m(tHead))
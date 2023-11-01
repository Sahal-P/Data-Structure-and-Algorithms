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
    # T O(n) M O(1)
    def two_pointer_reverseList(self) -> Optional[Node]:
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        print(prev.next.data)
        
    # T O(n) M O(n)
    def recursive_reverseList(self, head) -> Optional[Node]:
        newHead = head
        print(newHead.data)
        if head.next:
            newHead = self.recursive_reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
slist = SinglyLinkedList()
slist.insert_at_end([1,2,3,4,5,])

# slist.two_pointer_reverseList()
slist.recursive_reverseList(slist.head)

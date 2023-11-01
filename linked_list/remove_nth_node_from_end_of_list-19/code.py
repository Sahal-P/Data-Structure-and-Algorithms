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
linkl.insert_at_end([1,2,3,4,5])


def removeNthFromEnd_b( head: Optional[Node], n: int) -> Optional[Node]:
    count = 0
    currentHead = head
    RemovedHead = Node(0)
    RemovedHead.next = head
    while currentHead:
        count +=1
        currentHead = currentHead.next
    nth = count - n
    count = 0
    while RemovedHead:
        if count == nth:
            if count == 0:
                RemovedHead = None
                return None
            if RemovedHead.next and RemovedHead.next.next:
                RemovedHead.next = RemovedHead.next.next
            else:
                RemovedHead.next = None
        count +=1
        RemovedHead = RemovedHead.next
    return head

def removeNthFromEnd( head: Optional[Node], n: int) -> Optional[Node]:
    dummy = Node(0)
    dummy.next = head
    left = dummy
    right = head
    
    while n > 0 and right:
        right = right.next
        n-=1
        
    while right:
        left = left.next
        right = right.next
        
    left.next = left.next.next
    return dummy.next

n = 1
head = removeNthFromEnd(linkl.head, n)

# print(head.next.next.next)
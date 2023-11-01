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

list1 = SinglyLinkedList()
list1.insert_at_end([1,2,4])

list2 = SinglyLinkedList()
list2.insert_at_end([1,3,4])

def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    dummy = Node(None)
    tail = dummy
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    print(dummy.next.data)
    return dummy.next.data
    
mergeTwoLists(list1.head, list2.head)
from typing import Optional, List

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
list1.insert_at_end([1,4,5])

list2 = SinglyLinkedList()
list2.insert_at_end([1,3,4])

list3 = SinglyLinkedList()
list3.insert_at_end([2,6])

lists = [list1.head, list2.head, list3.head]

def mergeKLists(lists: List[Optional[Node]]) -> Optional[Node]:
    dummy = Node(None)
    tail = dummy
    for node in lists:
        while node:
            tail.next = node
            node = node.next
    data = []
    print(tail.next.data)
    while dummy:
        data.append(dummy.data)
        dummy = dummy.next
    print(data)
mergeKLists(lists)
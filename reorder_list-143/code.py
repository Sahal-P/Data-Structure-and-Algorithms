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
linkl.insert_at_end([1,2,3,4])

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def reorderList(head: Optional[Node]) -> None:
    arr = []
    currentHead = head
    while currentHead:
        arr.append(currentHead.data)
        currentHead = currentHead.next
    arr1, arr2 = split_list(arr)
    arr2.reverse()
    newArr = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        newArr.append(arr1[pointer1])
        newArr.append(arr2[pointer2])
        pointer1 +=1
        pointer2 +=1
        
    while pointer1 < len(arr1):
        newArr.append(arr1[pointer1])
        pointer1 +=1
        
    while pointer2 < len(arr2):
        newArr.append(arr[pointer2])
        pointer2+=1
    index = 0
    Nhead = head
    while Nhead:
        if index < len(newArr):
            Nhead.data = newArr[index]
        else:
            break
        Nhead = Nhead.next
        index+=1
        
reorderList(linkl.head)
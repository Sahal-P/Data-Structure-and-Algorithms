from typing import List, Optional

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)
            
    def _add(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(data, node.right)

def sortedArrayToBST(nums: List[int]) -> Optional[Node]:
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = Node(data=nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root


nums = [1,2,3,4,5,6,7]
root = sortedArrayToBST(nums)

# print(root.data)

tree = BinaryTree()
tree.add(5)
tree.add(4)
tree.add(6)

print(tree.root.left.data)
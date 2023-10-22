from typing import List, Optional

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add_list_to_tree(self, arr):
        for data in arr:
            self.add(data)
        
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
                
tree = BinaryTree()
tree.add_list_to_tree([4,2,7,1,3,6,9])


def invertTree(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    
    # swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root
        
        
root = invertTree(root=tree.root)

print(root.right.right.data)
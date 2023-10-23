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
                
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            # Inorder traversal: Left, Root, Right
            self._print_tree(node.left)
            print(node.data, end=" ")  # Print the node's data
            self._print_tree(node.right)
                
tree = BinaryTree()
tree.add_list_to_tree([4,2,7,1,3,6,9])
tree.add_list_to_tree([8,4,2,9,0])

tree.print_tree() 
print()

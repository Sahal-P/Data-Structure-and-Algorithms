from typing import Optional

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      
class BinaryTree:
    def __init__(self) -> None:
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
                
tree1 = BinaryTree()
tree1.add_list_to_tree([1,2,4,3])
tree2 = BinaryTree()
tree2.add_list_to_tree([1,2,4,3])

# T O(p + q) M O(h)
def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.data != q.data:
        return False
    a = isSameTree(p.left,q.left)
    b = isSameTree(p.right,q.right)
    return (a and b)

# T O(p + q) M O(n)
def ArrayMethod(p: Optional[Node], q: Optional[Node]) -> bool:
    firstTree, secondTree = [], []

    def get_value(array, root):
        if root:
            array.append(root.data)
            get_value(array,root.left)
            get_value(array,root.right)
        
    
    get_value(firstTree, p)
    get_value(secondTree, q)
    print(firstTree, secondTree)
    return firstTree == secondTree
    
# print(isSameTree(tree1.root, tree2.root))
print(ArrayMethod(tree1.root, tree2.root))
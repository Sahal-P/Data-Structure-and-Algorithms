from typing import Optional

class Node:
   def __init__(self, data):
      self.data = data
      self.left: Node | None = None
      self.right: Node | None  = None
      
root = Node(3)
root.right = Node(5)
root.left = Node(4)
root.left.left = Node(1)
root.left.right = Node(2)

subroot = Node(4)
subroot.right = Node(2)
subroot.left = Node(1)

# T O(h) M O(h)

#  T O(M-N when i get the job i will start to get)

def isSubtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    if not subRoot: return True
    if not root: return False

    if isSametree(root, subRoot):
        return True
    return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))
    
def isSametree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    if not root and not subRoot:
        return True
    if root and subRoot and root.data == subRoot.data:
        return (isSametree(root.left, subRoot.left) and isSametree(root.right, subRoot.right))
    return False
    
print(isSubtree(root, subroot))
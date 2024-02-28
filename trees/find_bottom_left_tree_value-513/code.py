from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    q = deque([root])

    while q:
        node = q.popleft()

        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    return node.val

# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
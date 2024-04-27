from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val + ord('a')))  # Convert node value to character
            if not node.left and not node.right:  # If leaf node
                paths.append("".join(path[::-1]))  # Reverse path to get leaf-to-root string
            dfs(node.left, path[:])  # Explore left subtree
            dfs(node.right, path[:])  # Explore right subtree

        paths = []
        dfs(root, [])
        return min(paths)
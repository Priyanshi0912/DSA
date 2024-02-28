# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.maxDepth = -1
        self.leftval = 0

    def dfs(self, root: Optional[TreeNode], depth: int) -> None:
        if root is None:
            return
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.leftval = root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.leftval

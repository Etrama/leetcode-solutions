# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summation = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.summation += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)
        dfs(root)
        return self.summation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value_set = set()
        def dfs(node):
            if node is None:
                value_set.add(None)
            else:
                dfs(node.left)
                value_set.add(node.val)
                dfs(node.right)
        dfs(root)
        value_set.remove(None)
        # print(value_set)
        return len(value_set) == 1
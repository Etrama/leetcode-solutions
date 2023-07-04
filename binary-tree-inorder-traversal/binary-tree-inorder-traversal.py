# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        def dfs(node):
            if node is None:
                pass
            else:
                dfs(node.left)
                # print(node.val)
                self.result.append(node.val)
                dfs(node.right)
        dfs(root)
        return self.result
        
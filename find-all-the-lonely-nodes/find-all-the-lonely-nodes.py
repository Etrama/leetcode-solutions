# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.lonely_nodes = []
        #starting with dfs of all nodes
        # def dfs(node):
        #     if node is not None:
        #         self.lonely_nodes.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        # dfs(root)
        def dfs(node):
            if node is not None:
                if node.left == None and node.right != None:
                    self.lonely_nodes.append(node.right.val)
                elif node.right == None and node.left != None:
                    self.lonely_nodes.append(node.left.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.lonely_nodes
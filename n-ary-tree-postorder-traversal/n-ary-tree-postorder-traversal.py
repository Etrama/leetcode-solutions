"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(node):
            if node is not None:
                for child in node.children:
                    dfs(child)
                    result.append(child.val)
        dfs(root)
        if root is not None:
            result.append(root.val)
        return result

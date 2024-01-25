# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        else:
            max_index = nums.index(max(nums))
            left_prefix = nums[:max_index]
            right_prefix = nums[max_index+1:]
            return TreeNode(val=max(nums), 
            left=self.constructMaximumBinaryTree(left_prefix),
            right=self.constructMaximumBinaryTree(right_prefix))

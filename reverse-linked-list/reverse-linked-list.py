# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        pointer = head
        while pointer:
            stack.append(pointer.val)
            pointer = pointer.next
        pointer = head
        while pointer:
            pointer.val = stack.pop()
            pointer = pointer.next
        return head
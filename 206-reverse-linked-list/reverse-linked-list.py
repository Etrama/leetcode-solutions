# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            prev, current, next_node = None, head, head.next
            while current:
                current.next = prev
                prev = current
                current = next_node
                next_node = next_node.next if next_node is not None else None
            return prev
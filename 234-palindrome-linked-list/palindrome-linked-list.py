# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_len = head
        length = 0
        while head_len:
            length += 1
            head_len = head_len.next
        stack = []
        length2 = 0
        while head:
            length2 += 1
            if length2 <= length // 2:
                stack.append(head.val)
            if length2 > length // 2:
                if len(stack) != 0 and stack[-1] == head.val:
                    stack.pop(-1)
            head = head.next
        return len(stack) == 0
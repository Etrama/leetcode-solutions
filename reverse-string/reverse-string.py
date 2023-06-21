class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) != 1:
            if len(s) % 2 == 1:
                left = int(len(s) / 2 - 1)
                right = int(len(s) / 2 + 1)
            elif len(s) % 2 == 0:
                right = int(len(s) / 2)
                left = right - 1
            # print(left, right)
            while left >= 0:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                right += 1
                left -= 1
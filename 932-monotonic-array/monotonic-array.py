class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag_up = True
        flag_down = True
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                flag_up=False
                break
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                flag_down=False
                break
        return flag_up or flag_down

        
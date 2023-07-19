class SparseVector():
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.vector[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        indices = set(self.vector.keys()).intersection(set(vec.vector.keys()))
        result = 0
        for index in indices:
            result += self.vector[index] * vec.vector[index]
        return result
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
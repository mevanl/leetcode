# Runtime: 35ms
# Memory: 16.18MB
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        original_size = len(nums)
        occurence_counter = 0

        while (val in nums):
            nums.remove(val)
            occurence_counter += 1
        
        return original_size - occurence_counter

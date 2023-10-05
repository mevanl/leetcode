# While this is correct, time limit exceeded so not a valid solution 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        size = len(nums)

        for i in range(size):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    return True
        return False
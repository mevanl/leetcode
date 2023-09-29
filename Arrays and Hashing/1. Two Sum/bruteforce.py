# Brute force method
# Runtime: 2521ms
# Memory: 17.07MB

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        size = len(nums)

        for i in range(size):
            for j in range(i+1, size):
                if (nums[i] + nums[j] == target):
                    return [i, j]   
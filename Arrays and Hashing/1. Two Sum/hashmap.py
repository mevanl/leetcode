class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for index, element in enumerate(nums):
            target_difference = target - element

            if target_difference in hashmap:
                return [hashmap[target_difference], index]
            hashmap[element] = index
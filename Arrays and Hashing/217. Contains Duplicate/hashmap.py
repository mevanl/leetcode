# Runtime: 464ms
# Memory: 35.52mb

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}

        for index, element in enumerate(nums):
            if element in hashmap:
                return True
            hashmap[element] = index
        return False
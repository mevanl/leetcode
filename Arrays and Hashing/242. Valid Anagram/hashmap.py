# Runtime: 56ms
# Size: 16.77mb
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        length = len(s)
        sHashmap = {}
        tHashmap = {}

        for char in range(length):
            sHashmap[s[char]] = sHashmap.get(s[char], 0) + 1
            tHashmap[t[char]] = tHashmap.get(t[char], 0) + 1
        return sHashmap == tHashmap
    
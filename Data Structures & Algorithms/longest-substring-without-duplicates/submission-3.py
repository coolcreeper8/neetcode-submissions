class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        maxl = 0
        start = 0
        for i in range(len(s)):
            while s[i] in cset:
                cset.remove(s[start])
                start+=1
            cset.add(s[i])
            maxl = max(maxl,len(cset))
        return maxl
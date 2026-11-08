class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        left = 0
        leng = 0
        right = 0
        while right < len(s):
            while s[right] in cset:
                cset.remove(s[left])
                left += 1
            cset.add(s[right])
            leng = max(leng, right - left + 1)
            right += 1
        return leng

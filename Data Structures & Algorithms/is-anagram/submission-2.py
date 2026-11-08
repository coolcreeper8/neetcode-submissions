class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charset = []
        for char in s:
            charset.append(char)
        for char in t:
            if not char in charset:
                return False
            charset.remove(char)
        return len(charset) == 0
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "cattac"
        s = s.strip()
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        

        i = 0
        left = 0
        right = len(s) - 1
        while i < len(s) // 2:
            if left == right:
                return True
            if right < left:
                return True
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
            i+=1
        
        return True

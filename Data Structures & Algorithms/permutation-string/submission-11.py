class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        charArray = [0]*26
        for char in s1:
            charArray[ord(char) - ord('a')] +=1
        # now for abc we should ahve [1 1 1 0 0 ... 0]

        start = 0
        checknow = [0]*26
        for i in range(len(s2)):

            # if this character isnt in s1 we can chuck it out
            if charArray[ord(s2[i])-ord('a')] == 0:
                start = i+1
                checknow = [0]*26
            else:
                if charArray[ord(s2[i]) - ord('a')] > checknow[ord(s2[i]) - ord('a')]:
                    checknow[ord(s2[i]) - ord('a')] +=1
                else:
                    checknow[ord(s2[i]) - ord('a')] +=1
                    while charArray[ord(s2[i]) - ord('a')] != checknow[ord(s2[i]) - ord('a')]:
                        charTo = s2[start]
                        checknow[ord(charTo) - ord('a')]-=1
                        start+=1

            if checknow == charArray:
                return True
        
        print(charArray)
        print(checknow)
        return charArray == checknow



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqmap = {}
        maxl = 0
        start = 0
        end = 0

        for i in range(len(s)):
            # FIRST ADD ELEMENT TO FREQUENCY MAP
            if s[i] in freqmap:
                freqmap[s[i]]+=1
            else:
                freqmap[s[i]] = 1
            
            # SHRINK THE WINDOW IF NECESSARY
            numdiff = i - start + 1 - max(freqmap.values())


            while numdiff > k:
                # decrease the freqmap entry associated with start
                #print(f"{s[start]} is the letter being judged, {freqmap} has {numdiff}")
                if freqmap[s[start]] > 1:
                    freqmap[s[start]] = freqmap[s[start]] - 1
                else:
                    freqmap.pop(s[start])
                numdiff -=1
                #print(f"UPDATE: {s[start]} is the letter being judged, {freqmap} has {numdiff}")

                start +=1
            # STORE THE MAXIMUM LENGTH OF THE REPEATED SUBSTRING
            maxl = max(maxl, i - start + 1)
            #print(maxl)

        return maxl

                





# HGGBSSSG num of letters u can change 
# longest substring with repeat: SSS
# k = 1, you would change G or B 
# k = 2 you can change both, 
# HSSSSSSS
# ABCAADDEE k = 2


# AAABACB"
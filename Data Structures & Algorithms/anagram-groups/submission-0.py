class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(t,q):
            freqt = {}
            freqq = {}
            for char in t:
                if char not in freqt:
                    freqt[char] = 1
                else:
                    freqt[char]+=1
            for char in q:
                if char not in freqq:
                    freqq[char] = 1
                else:
                    freqq[char]+=1

            return freqt == freqq
        seen = set()
        out = []
        for i in range(len(strs)):
            cond = False
            for wlist in out:
                if len(wlist) > 0:
                    if isAnagram(strs[i], wlist[0]):
                        wlist.append(strs[i])
                        cond = True
                        break
            if cond == False:
                out.append([strs[i]])
        return out
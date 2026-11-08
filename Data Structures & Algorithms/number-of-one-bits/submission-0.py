class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = int(bin(n)[2:])
        count = 0
        while binary != 0:
            if binary%10==1:
                count+=1
            binary//=10
        return count
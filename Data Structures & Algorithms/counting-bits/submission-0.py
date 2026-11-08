class Solution:
    def countBits(self, n: int) -> List[int]:
        def OneCount(num: int):
            bina = int(bin(num)[2:])
            count = 0
            while bina!=0:
                if (bina%10 == 1):
                    count += 1
                bina//=10
            return count
        return [OneCount(i) for i in range(0,n+1)]

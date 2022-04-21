# 202
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while(True):
            k=0
            while(n):
                k+=(n%10)**2
                n//=10
            if k in s: return False
            if(k==1): return True
            s.add(k)
            n=k
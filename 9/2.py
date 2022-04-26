# 1309
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans, z = "", 0
        while(z<len(s)-2):
            if s[z:z+3].endswith('#'): ans, z = ans+chr(int(s[z:z+2])+96), z+3
            else: ans, z = ans+chr(int(s[z])+96), z+1
        for y in range(z,len(s)): ans+=chr(int(s[y])+96)
        return ans
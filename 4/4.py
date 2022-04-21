# 1790
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a, b = [], []
        for z in range(len(s1)):
            if(s1[z]!=s2[z]):
                a.insert(0, s1[z])
                b.append(s2[z])
        return (s1==s2 or (len(a)==2 and a==b))
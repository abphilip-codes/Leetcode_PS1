# 242
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for z in s: a[ord(z)-97]+=1
        for z in t: a[ord(z)-97]-=1
        return a.count(0)==26
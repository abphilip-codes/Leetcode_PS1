# 1768
# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        k = [word1[z] + word2[z] for z in range(l)]
        return "".join(k) + word1[l:] + word2[l:]
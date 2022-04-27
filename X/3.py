# 104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

import string
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict()
        for z in range(26): d[order[z]]=string.ascii_lowercase[z]
        for z, k in enumerate(words):
            k = [d[c] for c in k]
            words[z] = "".join(k)
        return (words==sorted(words))
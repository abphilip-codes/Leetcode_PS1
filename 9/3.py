# 389
# https://leetcode.com/problems/find-the-difference/

import string
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o=dict()
        for i in range(26):
            o[order[i]]=string.ascii_lowercase[i]
        for i,word in enumerate(words):
            word=[o[c] for c in word]
            words[i]="".join(word)
        return words==sorted(words)
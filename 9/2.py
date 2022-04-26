# 1309
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def interpret(self, command: str) -> str:
        ans, z, k = '', 0, command
        while(z<len(command)):
            if(k[z]=='G'): ans, z = ans+'G', z+1
            elif(k[z:z+2]=='()'): ans, z = ans+'o', z+2
            else: ans, z = ans+'al', z+4
        return ans
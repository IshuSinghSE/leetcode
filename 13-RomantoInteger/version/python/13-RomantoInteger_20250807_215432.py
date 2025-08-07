# Last updated: 8/7/2025, 9:54:32 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        alph = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(0,len(s)-1):
            if alph.get(s[i]) < alph.get(s[i+1]):
                result -= alph.get(s[i])
            else:
                result += alph[s[i]]
        result += alph.get(s[-1])
        return result
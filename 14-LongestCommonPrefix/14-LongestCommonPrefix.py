# Last updated: 8/7/2025, 9:27:55 PM
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            print(string)
            while not string.startswith(prefix):
                prefix = prefix[:-1]
        
                if not prefix:
                    return ""
        return prefix

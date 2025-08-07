# Last updated: 8/7/2025, 9:27:54 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif stack and mapping.get(c) == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack
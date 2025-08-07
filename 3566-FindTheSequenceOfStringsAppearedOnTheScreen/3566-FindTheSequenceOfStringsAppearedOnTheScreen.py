# Last updated: 8/7/2025, 9:27:46 PM
class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        result = []
        curr_str = ""
       
        for char in target:
            curr_str += 'a'
            result.append(curr_str)

            while curr_str[-1] != char:
                curr_str = curr_str[:-1] + chr(ord(curr_str[-1])+1)
                result.append(curr_str)
        return result
        
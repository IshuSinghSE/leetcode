# Last updated: 8/7/2025, 9:27:53 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # Pointer for the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Update the position of the next unique element
        
        return i + 1  # Number of unique elements
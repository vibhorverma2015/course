"""
leetcode question practice of Arrays in regards to remove
duplicate numbers from a list.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                i += 1
            else:
                nums.pop(i + 1)

        return len(nums)

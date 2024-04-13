class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # fast start from 0: check the index 0's val
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                # different with leetcode 26: assign first then increment->
                # make sure the first element is not val
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
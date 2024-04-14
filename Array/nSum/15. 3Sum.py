# 需要优化：太慢

class Solution(object):
    def twoSumTarget(self, nums, start, target):
        # nums.sort()
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            s = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if s < target:
                # skip the same numebr => prevent repetition
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # target can not be zero
        target = 0
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            # start from i+1
            tuples = self.twoSumTarget(nums, i + 1, target - nums[i])
            for tuple in tuples:
                tuple.append(nums[i])
                tuple.sort()
                # maybe tuple have repetition
                if tuple not in res:
                    res.append(tuple)
            # skip the same number
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        return res
        
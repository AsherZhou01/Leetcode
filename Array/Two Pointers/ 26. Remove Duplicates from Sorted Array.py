# leetcode83: 去除链表中的重复元素很相似（快慢指针）
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # target: nums[0, nums] doesn't have same num
        slow = 0 
        fast = 1
        # fast will traverse the whole array
        while fast < len(nums):
            # if these two are different, then assign fast to slow
            # 最坏情况是每一个都不一样，这种情况下原数组保持不变
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        # 数组长度为索引 + 1
        return slow + 1
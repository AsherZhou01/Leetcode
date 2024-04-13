class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # j 是下一个非零元素将要插入的位置 （j encounter 0 then stop）
        j = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                # 交换非零元素到前面的位置
                nums[j], nums[i] = nums[i], nums[j]  
                j += 1
        return nums
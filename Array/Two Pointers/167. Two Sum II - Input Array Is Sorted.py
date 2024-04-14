class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 一左一右两个指针相向而行
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                # 题目要求的索引是从 1 开始的
                return [left + 1, right + 1]
            # 让 sum 大一点
            elif sum < target:
                left += 1 
            # 让 sum 小一点
            else:
                right -= 1 
        return [-1, -1]
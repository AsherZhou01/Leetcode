# 反转数组同反转字符串
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 一左一右两个指针相向而行
        left = 0
        right = len(s) - 1
        while left < right:
            # 交换 s[left] 和 s[right]
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
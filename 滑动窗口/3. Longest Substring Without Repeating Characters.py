class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}  # 用于记录窗口中各字符出现的次数
        left, right = 0, 0  # 窗口的左右边界
        res = 0  # 用于记录结果

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1  # 更新窗口和字符的出现次数

            # 判断窗口是否需要收缩：遇到的char已经在window中出现第二次了
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1  # 更新窗口和字符的出现次数
                # 继续判断进入循环直到window[c]==1

            res = max(res, right - left)  # 更新结果

        return res
        
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # defaultdict: 当访问一个不存在的键时，会自动创建并赋初值为0（而且速度比{}更快）
        need, window = defaultdict(int), defaultdict(int)
        # record each char's frequency in the dictionary
        for c in t:
            need[c] += 1

        left, right = 0, 0
        valid = 0
        start, length = 0, float('inf')  # 使用 float('inf') 表示无限大

        while right < len(s):
            # the char will be added into the window
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                # if this char's number meet the number of need, then increment valid
                if window[c] == need[c]:
                    valid += 1
            # all the chars' number meet the need, then begin try to shrink the window
            while valid == len(need):
                # 检查当前的窗口大小（right - left）是否小于之前记录的最小窗口大小（length）
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float('inf') else s[start:start + length]

        
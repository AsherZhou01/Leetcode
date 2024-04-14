class Solution(object):
    def checkInclusion(self, t, s):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1

        left, right = 0, 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩: 一定是定长的一个窗口(要和target的字符串长度相等)
            while right - left >= len(t):
                # 在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return False


# 这道题中 [left, right) 其实维护的是一个定长的窗口，窗口大小为 t.size()。因为定长窗口每次向前滑动时只会移出一个字符，所以可以把内层的 while 改成 if，效果是一样的。
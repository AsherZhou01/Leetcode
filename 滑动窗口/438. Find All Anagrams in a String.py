class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1

        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1
            if right - left == len(t):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
        
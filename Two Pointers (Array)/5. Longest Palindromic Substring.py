class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(s, l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            # 以 s[i] 为中心：长度为奇数的最长回文子串
            s1 = palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心：长度为偶数的最长回文子串
            s2 = palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

        
# 关键是找到一个单调函数和target
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = 1000000000
        
        while left <= right:
            mid = left + (right - left) // 2
            # 这里合并了分支，并且因为是单调递减所以和template不一样
            if self.f(piles, mid) <= h:
                right = mid-1
            else:
                left = mid + 1
        return left
    
    # in spped of x, Koko need f time to finish these piles
    def f(self, piles, x):
        hours = 0
        for i in range(len(piles)):
            hours += piles[i] // x
            # the remaining banana in the pile need one more hour to eat
            if piles[i] % x > 0:
                hours += 1
        return hours


        
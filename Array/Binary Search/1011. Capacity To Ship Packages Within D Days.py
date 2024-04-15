class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = 0
        right = 0
        # cap的最小值为最大的w，cap的最大值为所有w的和
        for w in weights:
            left = max(left, w)
            right += w
        while left <= right:
            mid = left + (right - left) // 2
            # 所需天数<target，所以缩小右边界，看看更小的cap是否也可以
            if self.f(weights, mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    # capacity为x的情况下，需要f天来运输weights这些货物
    def f(self, weights, x):
        days = 0
        # 尽可能多的装货
        i = 0
        while i < len(weights):
            cap = x
            # one day
            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            days += 1
        return days
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            result = max(result, prices[r] - prices[l])

        return result

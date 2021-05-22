"""
leetcode practice question for the searching in regards to
finding the maximum profit from buying and selling in the array.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                if prices[i] > min_value:
                    maxProfit += prices[i] - min_value
                    min_value = prices[i]

        return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        curMax = 0
        for i in range(1, n):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > curMax:
                curMax = prices[i] - buy
        return curMax
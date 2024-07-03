class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0

        for p in prices:
            if min > p:
                min = p
            profit = max(profit, p - min)

        return profit
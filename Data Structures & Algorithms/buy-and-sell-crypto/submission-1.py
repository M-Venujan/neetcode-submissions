class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1,len(prices)):
            curr_profit = prices[right] - prices[left]
            if curr_profit <= 0:
                left = right
            else:
                max_profit = max(max_profit , curr_profit)
        return max_profit
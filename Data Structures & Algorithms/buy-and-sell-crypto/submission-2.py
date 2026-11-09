class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        # brute force
        for i in range(len(prices) - 1):
            for y in range(i + 1, len(prices)):
                diff = prices[y] - prices[i]
                max_diff = max(max_diff, diff)

        return max_diff
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_b = prices[0]
        for i in prices: 
            if i < min_b: 
                min_b = i 
            if i - min_b > max_p:
                max_p = i - min_b
        return max_p
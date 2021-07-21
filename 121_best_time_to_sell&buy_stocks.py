class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for i in prices:
            if i < min_price:
                min_price=i
            elif(i-min_price > max_profit):
                max_profit=i-min_price
        return max_profit
                

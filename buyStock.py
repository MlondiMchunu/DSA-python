class Solution:
    def maxProfit(self,prices:List[int])->int:
        buy_price = prices[0]
        profit = 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        buy = prices[i]
        sell = 0
        for j in range(1,len(prices)):
            if prices[j]<prices[i]:
                buy = prices[i]
                i=j
            else:
                cur_sell = prices[j]-prices[i]
                sell = max(sell,cur_sell)
        return sell
            


        
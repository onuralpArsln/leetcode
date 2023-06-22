

## bad solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buyDay=0
        sellDay=0
        currentDay=0
        loopRange = len(prices)
        prices.reverse()
        for i in  range(loopRange):
            if prices[i] > buyDay :
                buyDay = prices[i]
                for j in  prices[i:]:
                    if buyDay - j > maxProfit:
                        maxProfit = buyDay - j  

        return maxProfit
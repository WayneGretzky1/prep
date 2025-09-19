class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            curr_profit = prices[i] - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit
    
if __name__ == "__main__":
    test = Solution()
    test1 = [1,2,3]
    test2 = [4,3,2,1]
    test3 = [9]
    test4 = [9,9,9]
    test5 = [4,1,2,3]
    test6 = [7,1,5,3,6,4]
    assert(test.maxProfit(test1) == 2)
    assert(test.maxProfit(test2) == 0)
    assert(test.maxProfit(test3) == 0)
    assert(test.maxProfit(test4) == 0)
    assert(test.maxProfit(test5) == 2)
    assert(test.maxProfit(test6) == 5)



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__ == "__main__":
    stairs = Solution()
    test1 = 2
    test2 = 4
    test3 = 8
    test4 = 7

    assert(stairs.climbStairs(test1) == 2)
    assert(stairs.climbStairs(test2) == 5)
    assert(stairs.climbStairs(test3) == 34)
    assert(stairs.climbStairs(test4) == 21)
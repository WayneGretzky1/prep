class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # visited = set()
        # while n != 1:
        #     digits_sum = 0
        #     num = n
        #     while num != 0:
        #         remainder = num % 10
        #         num //= 10
        #         print(remainder)
        #         digits_sum += remainder ** 2
        #     n = digits_sum
        #     if n in visited:
        #         return False
        #     visited.add(n)
        # return True
        visited = set()
        while n != 1:
            num = n
            digits_sum = sum(int(digit) ** 2 for digit in str(n))
            n = digits_sum
            if n in visited:
                return False
            visited.add(n)
        return True
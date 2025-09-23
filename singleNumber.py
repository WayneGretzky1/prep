class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = 0
        for i in range(len(nums)):
            bit = bit ^ nums[i]
        return bit
    
if __name__ == "__main__":
    test = Solution()
    test1 = [1,2,2]
    test2 = [4,3,4]
    test3 = [9]
    test4 = [9,9,9]
    assert(test.singleNumber(test1) == 1)
    assert(test.singleNumber(test2) == 3)
    assert(test.singleNumber(test3) == 9)
    assert(test.singleNumber(test4) == 9)
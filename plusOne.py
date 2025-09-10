class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if i == 0:
                if digits[i] == 10:
                    digits[i] = 0
                    digits.insert(0,1)
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
  
        return digits
    
if __name__ == "__main__":
    digits = Solution()
    test1 = [1,2,3]
    test2 = [4,3,2,1]
    test3 = [9]
    test4 = [9,9,9]
    assert(digits.plusOne(test1) == [1,2,4])
    assert(digits.plusOne(test2) == [4,3,2,2])
    assert(digits.plusOne(test3) == [1,0])
    assert(digits.plusOne(test4) == [1,0,0,0])


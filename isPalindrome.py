class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [c.lower() for c in s if c.isalnum()]

        l = 0
        r = len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l+=1
            r-=1
        return True
    
if __name__ == "__main__":
    test = Solution()
    test1 = "A man, a plan, a canal: Panama"
    test2 = "race a car"
    test3 = " "

    assert(test.isPalindrome(test1) == True)
    assert(test.isPalindrome(test2) == False)
    assert(test.isPalindrome(test3) == True)

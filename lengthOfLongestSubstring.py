#Sliding window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        max_len = start = 0
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len
    
if __name__ == "__main__":
    test = Solution()
    test1 = "abcddef"
    test2 = "bbbbb"
    test3 = "abcabcbb"

    assert(test.lengthOfLongestSubstring(test1) == 4)
    assert(test.lengthOfLongestSubstring(test2) == 1)
    assert(test.lengthOfLongestSubstring(test3) == 3)

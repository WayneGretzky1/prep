class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bin = bin(n)
        str_reverse_n_bin = ""
        for i in range(2,len(n_bin)):
            str_reverse_n_bin = str(n_bin[i]) + str_reverse_n_bin
        while len(str_reverse_n_bin) < 32:
            str_reverse_n_bin = str_reverse_n_bin + "0"

        reverse_n = int(str_reverse_n_bin, 2)
        return reverse_n
    
if __name__ == "__main__":
    bits = Solution()
    test1 = 43261596
    test2 = 2147483644

    assert(bits.reverseBits(test1) == 964176192)
    assert(bits.reverseBits(test2) == 1073741822)
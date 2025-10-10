class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dec_to_bin(num):
            if num == 0:
                return "0"
            bin_num = ""
            while num > 0:
                remainder = str(num % 2)
                bin_num = remainder + bin_num
                num //= 2

            return int(bin_num)
        
        bin_str = str(bin(n))
        count = 0
        for i in range(len(bin_str)):
            if bin_str[i] == "1":
                count += 1
        return count

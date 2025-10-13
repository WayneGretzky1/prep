class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max_32 = 2147483647
        min_32 = -2147483648
        is_negative = x < 0
        s = str(abs(x))[::-1]
        if len(s) > 10:
            return 0
        reverse_s = int(s)

        if is_negative:
            reverse_s = -reverse_s
        if reverse_s < min_32 or max_32 < reverse_s:
            return 0
        return reverse_s

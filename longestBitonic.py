
class Solution(object):

    def longest_bitonic_subsequence(self, arr):
        n = len(arr)
        inc = [1] * n
        # Longest increasing sequence
        for i in range(1,n):
            for j in range(i):
                if arr[i] > arr[j] and inc[i] < inc[j] + 1:
                    inc[i] = inc[j] + 1
        dec = [1] * n
        for i in range(n-2,-1,-1):
            for j in range(n-1, i, -1):
                if arr[i] > arr[j] and dec[i] < dec[j] + 1:
                    dec[i] = dec[j] + 1
        max_len = 0
        for i in range(n):
            max_len = max(max_len, inc[i] + dec[1] - 1)
        return max_len

if __name__ == "__main__":
    test = Solution()
    test1 = [12, 11, 40, 5, 3, 1]
    assert(test.longest_bitonic_subsequence(test1) == 5)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}

        def str_to_int(s: str) -> int:
            int_list = []
            for c in s:
                int_list.append(digits[c]) 
            result = 0
            order = 1
            for i in range(len(int_list)-1, -1, -1):
                result += int_list[i] * order
                order *= 10
            return result

        def int_to_str(n: int) -> str:
            if n == 0:
                return "0"
            result = ""
            while n > 0:
                remainder = n % 10
                result = str(remainder) + result
                n //= 10
            return result

        n1 = str_to_int(num1)
        n2 = str_to_int(num2)
        product = n1 * n2
        return int_to_str(product)



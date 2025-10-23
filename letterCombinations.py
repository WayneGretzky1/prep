class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        telephone_buttons = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r", "s"], "8":["t","u","v"], "9":["w","x","y","z"]}

        n = len(digits)
        result = []

        def backtrack(index, path):
            if index == n:
                result.append(path)
                return
            for letter in telephone_buttons[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


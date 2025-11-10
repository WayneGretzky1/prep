class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alpha_count = defaultdict(int)

        for char in s:
            alpha_count[char] += 1
        
        for char in t:
            alpha_count[char] -= 1
            if alpha_count[char] < 0:
                    return False
        
        for val in alpha_count.values():
            if val != 0:
                return False
        return True

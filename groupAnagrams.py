class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}
        # n = len(strs)

        # for i in range(n):
        #     word = strs[i]
        #     sorted_characters = sorted(word)
        #     sorted_word = "".join(sorted_characters)

        #     if sorted_word not in anagrams:
        #         anagrams[sorted_word] = [word]
        #     else:
        #         anagrams[sorted_word] += [word]

        # return list(anagrams.values())
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())
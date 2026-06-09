from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seen = {}
        for word in strs:
            sorted_word = list(word)
            sorted_word.sort()
            word_str = "".join(sorted_word)
            if word_str not in seen:
                seen[word_str] = [word]
            else:
                anagram = seen.get(word_str)
                anagram.append(word)
        
        for val in seen.values():
            output.append(val)

        return output
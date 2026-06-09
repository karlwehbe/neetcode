class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        count_1 = count_s - count_t
        count_2 = count_t - count_s


        if len(list(count_1.elements())) > 0 or len(list(count_2.elements())) > 0:
            return False
        
        return True

        
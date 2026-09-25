class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(best):
                    best = s[l + 1:r]
        return best

        # Every palindrome has a middle. 
        # So go through each spot in the string, treat it as the middle, and grow outward while both sides match. 
        # You check two kinds of middles, one letter (odd length like "aba") and between two letters (even length like "abba").
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        dp = [1] * n
        best_len, best_end = 1, 0

        for i in range(1, n):
            start = max(0, i - dp[i - 1] - 1)
            for j in range(start, i + 1):
                sub = s[j:i + 1]
                if sub == sub[::-1]:
                    dp[i] = i - j + 1
                    break

            if dp[i] > best_len:
                best_len, best_end = dp[i], i

        return s[best_end - best_len + 1:best_end + 1]
        
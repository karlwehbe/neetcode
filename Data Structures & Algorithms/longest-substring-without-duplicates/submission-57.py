class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest, l, r = 1, 0, 1

        substring = set(s[l])
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
            else:
                if s[r] == s[r-1]:
                    while l < r:
                        substring.remove(s[l])
                        l += 1
                    substring.add(s[r])
                else:
                    while s[l] != s[r]:
                        substring.remove(s[l])
                        l += 1
                    l += 1
            
            longest = max(longest, len(substring))
            r += 1
            
        
        return longest
                


        
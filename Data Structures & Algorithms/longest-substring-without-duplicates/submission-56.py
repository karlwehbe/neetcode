class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest, l, r = 1, 0, 1

        substring = set(s[l])
        while r < len(s):
            print("curr char is", s[r], )
            if s[r] not in substring:
                print("adding", s[r])
                substring.add(s[r])

            else:
                if s[l] == s[r]:
                    print(f"char {s[l]} is the same as {s[r]} ")
                    l += 1
                elif s[r] == s[r-1]:
                    while l < r:
                        substring.remove(s[l])
                        l += 1
                    substring.add(s[r])
                else:
                    while s[l] != s[r]:
                        print(l, r, "removing", s[l])
                        substring.remove(s[l])
                        l += 1
                    l += 1
            
            print(substring)
            print("left = ", l, "right = ", r)
            longest = max(longest, len(substring))
            r += 1
            print()
            
        
        return longest
                


        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        for char in s:
            if char.isalnum():
                forward.append(char.lower())
        
        backward = []
        for i in reversed(range(len(s))):
            char = s[i]
            if char.isalnum():
                backward.append(char.lower())
        
        print(forward, backward)

        return forward == backward
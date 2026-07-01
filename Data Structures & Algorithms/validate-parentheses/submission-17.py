class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        stack = []
        bracket_types = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            print(char)
            print(stack)
            if char in bracket_types.keys():
                stack.append(char)
            else:
                if len(stack) == 0: return False
                
                open_bracket = stack.pop(-1)
                
                if open_bracket not in bracket_types.keys(): return False
                elif bracket_types[open_bracket] != char: return False
                
        if len(stack) != 0: return False
        return True
                
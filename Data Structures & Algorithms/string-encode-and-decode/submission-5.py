class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for string in strs:
            encoded += string
            if string == "":
                encoded += ":;"
            else: 
                encoded += ":;"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split(":;")[:-1]
        return decoded
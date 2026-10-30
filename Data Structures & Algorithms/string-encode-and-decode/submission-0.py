class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for s in strs:
            encoded += s + "\\£"
        return encoded

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        string = ""
        i = 0
        while i <len(s):
            c = s[i]
            if c == "\\" and s[i+1] == "£":
                decoded.append(string)
                string = ""
                i += 1
            else:
                string += c
            i += 1
        return decoded
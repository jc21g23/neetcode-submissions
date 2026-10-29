class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sDict = {}

        for cs in s:
            sDict[cs] = sDict.get(cs, 0) + 1

        for ct in t:
           sDict[ct] = sDict.get(ct, 0) - 1
        
        print(sDict)
        for count in sDict.values():
            print(count)
            if (count != 0): return False
        
        return True


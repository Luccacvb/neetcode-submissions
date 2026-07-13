class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for val in s:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        
        for val in t:
            if val in count:
                count[val] -= 1
            else:
                return False
        
        for _, v in count.items():
            if v > 0:
                return False
        
        return True
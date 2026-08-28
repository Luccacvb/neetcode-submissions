class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        mapp = {}
        for ch in s:
            if ch in mapp:
                mapp[ch] += 1
            else:
                mapp[ch] = 1
        
        odd = 0
        for k, v in mapp.items():
            if v % 2 != 0:
                odd += 1
            
            if odd > 1:
                return False

        return True
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1):
            calc = abs(ord(s[i + 1]) - ord(s[i]))
            res = res + calc

        return res

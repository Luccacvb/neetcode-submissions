class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left_s, left_t = 0, 0

        while left_s < len(s) and left_t < len(t):
            if s[left_s] == t[left_t]:
                left_t += 1
            left_s += 1

        return len(t) - left_t

class Solution:
    def _search_char(self, char: str) -> int:
        return ord(char) - ord("a")

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for char in s:
            count[self._search_char(char)] += 1

        for char in t:
            idx = self._search_char(char)
            count[idx] -= 1

            if count[idx] < 0:
                return False

        return True

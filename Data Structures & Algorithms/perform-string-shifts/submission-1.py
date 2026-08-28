class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total = 0

        for direction, amount in shift:
            if direction == 0:
                total += amount
            else:
                total -= amount
        
        total %= len(s)
        return s[total:] + s[:total]
class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        count = 0

        for v in arr:
            if v + 1 in seen:
                count += 1
        
        return count
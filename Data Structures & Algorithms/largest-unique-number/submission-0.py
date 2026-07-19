class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        big_num = -1
        visited = set()

        for n in nums:
            if n not in visited:
                visited.add(n)
            else:
                visited.remove(n)

        if len(visited) > 0:
            big_num = max(visited)

        return big_num

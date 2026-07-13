class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        steps = 2
        ans = []

        while steps > 0:
            for n in nums:
                ans.append(n)

            steps -= 1

        return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered = sorted(nums)
        res = []

        for i in range(len(ordered)):
            anchor = ordered[i]
            l = i + 1
            r = len(ordered) - 1

            while l < r:
                total = ordered[l] + ordered[r] + anchor

                if total == 0:
                    if [ordered[l], ordered[r], anchor] not in res:
                        res.append([ordered[l], ordered[r], anchor])
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res

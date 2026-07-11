class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        
        for i, n in enumerate(nums):
            res = target - n
        
            if res in mapp:
                return [mapp[res], i]
        
            mapp[n] = i

        return [-1,-1] 
        
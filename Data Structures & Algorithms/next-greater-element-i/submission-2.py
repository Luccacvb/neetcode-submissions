class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []

        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(nextGreater.get(num, -1))

        return res

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        open_items = {"[", "(", "{"}
        pairs = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for item in s:
            if item in open_items:
                stack.append(pairs[item])
            else:
                if len(stack) > 0 and stack[-1] == item:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

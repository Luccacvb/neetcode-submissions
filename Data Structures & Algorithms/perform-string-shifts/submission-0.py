class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        new_s = deque(list(s))

        for s in shift:
            if s[0] == 0:
                for _ in range(s[1]):
                    new_s.append(new_s.popleft())
            else:
                for _ in range(s[1]):
                    new_s.insert(0, new_s.pop())


        return "".join(new_s)
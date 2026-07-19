class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for ch in strs:
            default = sorted(ch)
            default = "".join(default)
            groups[default].append(ch)

        res = list(groups.values())
        return res

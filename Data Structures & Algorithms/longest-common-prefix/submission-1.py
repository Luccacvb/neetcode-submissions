class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for position in range(len(strs[0])):
            for string in strs:
                if len(string) <= position:
                    return res

                if string[position] != strs[0][position]:
                    return res

            res += strs[0][position]

        return res

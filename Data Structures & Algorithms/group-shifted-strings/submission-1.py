class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for string in strings:
            signature = []

            for i in range(len(string) - 1):
                char1 = string[i]
                char2 = string[i + 1]
                difference = (ord(char2) - ord(char1)) % 26
                signature.append(difference)

            key = tuple(signature)
            if key not in groups:
                groups[key] = []

            groups[key].append(string)

        return list(groups.values())

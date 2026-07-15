class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                letter_row = words[i][j]

                if j < len(words) and i < len(words[j]):
                    letter_col = words[j][i]
                else:
                    return False

                if letter_row != letter_col:
                    return False

        return True

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapp = {}
        for i, k in enumerate(keyboard):
            mapp[k] = i
    
        count = 0
        j = 0
        for w in word:
            find_position = mapp[w]
            count += abs(j - find_position)
            j = find_position
        
        return count

        


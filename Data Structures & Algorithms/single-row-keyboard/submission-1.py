class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapp = {}
        for i, k in enumerate(keyboard):
            mapp[k] = i
    
        count = 0
        j = 0
        for w in word:
            while w != keyboard[j]:
                position = mapp[keyboard[j]]
                find_position = mapp[w]
                
                if position == find_position:
                    break

                if position < find_position:
                    j += 1
                elif position > find_position:
                    j -= 1
                
                count += 1
        
        return count

        


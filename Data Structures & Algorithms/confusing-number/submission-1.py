class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        tmp_n = n
        final = 0

        while tmp_n > 0:
            tmp_n, val  = divmod(tmp_n, 10)
            
            if val not in mapping:
                return False
            
            final = final * 10 + mapping[val]
        
        return final != n
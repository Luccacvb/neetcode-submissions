class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        reverse = n[::-1]
        return n == reverse

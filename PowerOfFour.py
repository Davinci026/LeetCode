class Solution:
    def isPowerOfFour(self, n: int) :
        if n == 1:
                return True
        if n < 1 or n % 4 != 0:
                return False
        return self.isPowerOfFour(n // 4)
class Solution:
   def isPalindrome(self, x: int) -> bool:
        test=(list(str(x)))
        test.reverse()
        return list(str(x)) == test

class Solution:
    def sortedSquares(self, nums) :
        aux=[numbers**2 for numbers in nums]
        aux.sort()
        return aux

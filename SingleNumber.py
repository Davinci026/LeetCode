class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        i=0
        result=0
        while i < len(nums):
            result= result ^ nums[i]
            i+=1
        return result
x=Solution()
print(x.singleNumber([2,2,1,3,4,3,5,4,5]))

class Solution(object):
    def twoSum(self, nums, target):
       complementarMap={}
       i=0
       complement = 0
       while i < len(nums):
           if nums[i]  in complementarMap:
               return i,complementarMap[nums[i]]
           complement = target - nums[i]
           complementarMap[complement]=i
           complement=0
           i+=1

test=Solution()
print((test.twoSum([3,2,4],6)))


            
        



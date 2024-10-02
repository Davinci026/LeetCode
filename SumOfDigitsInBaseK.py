class Solution:
    def sumBase(self, n: int, k: int) -> int:
       if n < k:
           return n
       else:
           div=n//k
           return self.sumBase(div, k) + (n % k)
           
        
x=Solution()
print(x.sumBase(64,6))
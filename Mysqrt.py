class Solution:
    # I am using the Newton-Rapson method to approximate the square root of a number
    def mySqrt(self, x: int) -> int: 
        num=x
        init=1.0
        e=0.0000000001
        while abs(num - init)>e:
            num=(num+init)/2
            init=x/num 
        return int(num)
x=Solution()
print(x.mySqrt(144))
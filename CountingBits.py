class Solution:
    def countBits(self, n: int) :
        ans=[]
        i=0
        while i < n+1:
            count=0
            for j in range(2,len(bin(i))):
                if bin(i)[j] == '1':
                    count=count + 1
            ans.append(count)
            i=i+1
        return ans
x=Solution()
y=x.countBits(5)
print(y)
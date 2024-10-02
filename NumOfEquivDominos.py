class Solution:
    def numEquivDominoPairs(self, dominoes :list[list[int]]) -> int:
        i=0
        count=0
        visitedDominoesMap={}
        while i<len(dominoes):
            dominoes[i].sort()
            if tuple(dominoes[i]) in visitedDominoesMap :
                visitedDominoesMap[tuple(dominoes[i])]+=1
                i+=1
            else:
                visitedDominoesMap[tuple(dominoes[i])]=1
                i+=1
        for keys in visitedDominoesMap:
            if visitedDominoesMap[keys] > 1:
                count=count+visitedDominoesMap[keys]*((visitedDominoesMap[keys]-1)/2)
        return int(count)
x=Solution()
dom=[[1,2],[2,1],[3,4],[4,3],[1,2]]
print(x.numEquivDominoPairs(dom))

                
class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        i=0
        while i < len(s)-1:
            if (romanMap[s[i]] >=  romanMap[s[i+1]]) :
                total+=romanMap[s[i]]
                i+=1
            elif romanMap[s[i]] < romanMap[s[i+1]]:
                total-=romanMap[s[i]]
                i+=1
        total += romanMap[s[i]]
        return total
x=Solution()
print(x.romanToInt("XIV"))
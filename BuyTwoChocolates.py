class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        saldo=0
        i=0
        j=1
        while j < len(prices):
            if (prices[i] + prices[j]) <= money:
                saldo = money-(prices[i]+prices[j])
                return saldo
            else:
                 i+=1
                 j+=1
        return money
            
        

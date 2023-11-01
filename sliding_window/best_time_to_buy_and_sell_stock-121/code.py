from typing import List
from testcase import testcase

# Brute Force Method Runs in O(n2)
def maxProfit_b( prices: List[int] ) -> int:
    dif = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            val = prices[j]-prices[i]
            dif = max(dif,val)
    return dif



# Linear Time Solution O(n)

def maxProfit( prices: List[int] ) -> int:
    left , right = 0, 1
    maxProfit = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            profit  = prices[right] - prices[left]
            maxProfit = max(maxProfit,profit)
        else:
            left = right
        right +=1
    return maxProfit


case1 = [2,4,1]
case2 = [7,1,5,3,6,4]
print(maxProfit(testcase))
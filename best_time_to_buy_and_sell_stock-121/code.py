from typing import List
from testcase import testcase

# Brute Force Method Runs in O(n2)
def maxProfit( prices: List[int] ) -> int:
    dif = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            val = prices[j]-prices[i]
            dif = max(dif,val)
    return dif

case1 = [2,4,1]
case2 = [7,1,5,3,6,4]
print(maxProfit(testcase))
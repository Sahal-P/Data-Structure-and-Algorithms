from typing import List
from testcase import testcase
import math

# Brute Force method O(n2)T O(1)S
def maxArea_b( height: List[int] ) -> int:
    res = 0
    for i in range(len(height)):
        for j in range(1,len(height)):
            width = j-i
            val = min(height[i],height[j])
            sqrt = val*width
            # if res < sqrt:
            #     res=sqrt
            res = max(res,sqrt)
    return res

# Linear time solution O(n)T O(1)S
def maxArea( height: List[int] ) -> int:
    res = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        area = (right-left) * min(height[left],height[right])
        res = max(res, area)
        
        if height[left] < height[right]:
            left+=1
        elif height[left] > height[right]:
            right-=1
        else:
            right-=1
    return res

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))
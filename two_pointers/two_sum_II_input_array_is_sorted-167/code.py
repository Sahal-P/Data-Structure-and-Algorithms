from typing import List
from testcase import testcase
# Brute Force
# O(n2)
def twoSum2_b(numbers: List[int], target: int) -> List[int]:
    
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if i == j:
                continue
            val = numbers[i]+numbers[j]
            
            # when we added this there is a diffrence of 10s in testcase
            if val > target:
                break
            # --
            if val == target:
                return [i+1, j+1]

# this solution runs O(n) ST complexity
def twoSum2_t(numbers: List[int], target: int) -> List[int]:
    has_map = {}
    for i in range(len(numbers)):
        c = target - numbers[i]
        if c in has_map:
            return [has_map[c]+1, i+1]
        has_map[numbers[i]] = i
        
# this solution is best for space and time complexity where O(n)T O(1)S        
def twoSum2_s(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1
    
    while left < right:
        val = numbers[left]+numbers[right]
        
        if val == target:
            return [left+1, right+1]

        if left < right and val > target:
            right-=1
            continue
            
        if left < right and val < target:
            left+=1
            continue
        left, right = left+1, right-1


# print(testcase[13010],testcase[13011])

print(twoSum2_s(testcase,5))
# print(twoSum2_s([2,7,11,15],9))
from typing import List

# make a set
# left to right: 
# check if a num is the start of a seq 
# by checking if it has a left neighbor,
# if yes, then it's not the start of a seq, move on.
# if it is the start of a seq, check if the next num exists
# eventually count the length

def longestConsecutive(nums: List[int]) -> int:
    sets = set(nums)
    longest = 0
    print(sets)
    for i in range(len(nums)):
        if nums[i]-1 not in sets:
            length = 0 
            while (nums[i] + length) in sets:
                length+=1
            
            longest = max(length,longest)
            # if length > longest:
            #     longest=length
            
    print(longest)
from functools import cache
    
def longestConsecutive1(nums: List[int]) -> int:
    nset = set(nums)
    @cache
    def dfs(n: int) -> int:
        if n not in nset:
            return 0
        return 1 + dfs(n + 1)
    
    res = 0
    for n in nums:
        res = max(res, dfs(n))
    print(res)
    return res


longestConsecutive1([100,4,200,1,3,2])

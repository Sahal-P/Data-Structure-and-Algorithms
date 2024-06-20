from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    # math solution
    
    # count = Counter(nums)
    # res = 0
    # for n, c in count.items():
    #     res += c * (c-1) // 2
    
    # without math
    
    res = 0
    count = {}
    for n in nums:
        if n in count:
            res += count[n]
            count[n] += 1
        else:
            count[n] = 1

    return res

nums = [1,2,3,1,1,3]
numIdenticalPairs(nums)

# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

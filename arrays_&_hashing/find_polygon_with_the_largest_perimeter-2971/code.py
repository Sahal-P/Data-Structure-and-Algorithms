from typing import List

# O(nlog n) + O(n)
def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    result = -1
    total = 0

    for n in nums:
        if total > n:
            result = total + n
        total += n
    return result

nums = [1,12,1,2,5,50,3]
print(largestPerimeter(nums))
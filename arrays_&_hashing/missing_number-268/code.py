from typing import List


def create_set(num):
    num_set = set()
    for i in range(num + 1):
        num_set.add(i)
    return num_set

def missingNumber(nums: List[int]) -> int:
    num_set = create_set(len(nums))
    for i in range(len(nums)):
        if nums[i] in num_set:
            num_set.remove(nums[i])
    for i in num_set:
        return i

# nums = [3,0,1]
# Output: 2

# nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
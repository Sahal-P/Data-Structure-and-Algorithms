from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
    pos, neg = [], []

    for n in nums:
        if n > 0:
            pos.append(n)
        else:
            neg.append(n)

    i = 0
    while 2 * i < len(nums):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
        i += 1

    return nums

nums = [3,1,-2,-5,2,-4]

rearrangeArray(nums)

# [3,-2,1,-5,2,-4]
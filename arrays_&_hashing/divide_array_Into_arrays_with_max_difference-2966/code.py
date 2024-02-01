from typing import List

def divideArray(nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                  return []
            res.append(nums[i:i+3])
        return res
    
def divideArray_(nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        is_possible = True
        for i in range(0, len(nums)-2, 3):
            print(i, nums[i])
            first, second, third = nums[i], nums[i+1], nums[i+2]
            if third-first <= k:
                result.append([first, second, third])
            else:
                is_possible=False
                break
        if not is_possible:
            return []
        return result
    
nums = [1,3,4,8,7,9,3,5,1]
k = 2

print(divideArray_(nums, k))
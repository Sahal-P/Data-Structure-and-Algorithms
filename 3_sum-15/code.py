from typing import List
import heapq
import time

from testcase import testcase


# brute force method O(n3) + O(nlogn) 
def threeSum_b(nums: List[int]) -> List[List[int]]:
    nums.sort()  
    # Sort the array to make duplicate checks easier
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  
        # Skip duplicates to avoid duplicate combinations

        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  
            # Skip duplicates to avoid duplicate combinations

            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue  
                # Skip duplicates to avoid duplicate combinations

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result

# combinations = threeSum_b(testcase)
# print(combinations)

def heapSort(arr: List[int]) -> List[int]:
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result




# used heap sort for achiving O(1) S
# overall Time Complexity is O(n logn) + O(n2) = O(n2)

def threeSum(nums: List[int]) -> List[List[int]]:
    res=[]
    nums = heapSort(nums)

    for indx, val in enumerate(nums):
        print(indx, val)
        if indx > 0 and val == nums[indx-1]:
            # Skip duplicates to avoid duplicate combinations
            continue
        
        left, right = indx + 1 , len(nums) -1
        while left < right:
            threeSum = val + nums[left] + nums[right]
            if threeSum > 0:
                right-=1
            elif threeSum < 0:
                left+=1
            else:
                res.append([val, nums[left], nums[right]])
                left+=1
                while nums[left] == nums[left-1] and left < right:
                    # Skip duplicates to avoid duplicate combinations
                    left+=1
    return res




nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
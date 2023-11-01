from typing import List


def findMin(nums: List[int]) -> int:
    res = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return res


nums = [3, 4, 5,6, 1, 2]
# nums = [0,1,2,3,4,5,6,7,8]


def findMin_1(nums: List[int]) -> int:
    res = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        elif nums[mid] < nums[left]:
                right = mid - 1
        if nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
            print('here')
            return nums[mid]

    return res
print(findMin_1(nums))


def findMin_2(self, nums: List[int]) -> int:
    s = 0
    e = len(nums) - 1
    if nums[e] > nums[s] or len(nums) == 1:
        return nums[0]

    while s < e:
        m = (s + e) // 2

        if nums[m] > nums[e]:
            s = m + 1
        else:
            e = m

    return nums[e]

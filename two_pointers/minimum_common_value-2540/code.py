from typing import List

def getCommon(nums1: List[int], nums2: List[int]) -> int:
    n1, n2 = len(nums1), len(nums2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return -1


def getCommon(nums1: List[int], nums2: List[int]) -> int:
    
    intersection = set(nums1) & set(nums2)
    # set intersection convert into common elements in the 2 sets
    if intersection:
        return min(intersection)
    return -1
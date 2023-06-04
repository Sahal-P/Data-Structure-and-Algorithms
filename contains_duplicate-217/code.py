from typing import List

# worst case O(n2)

def containsDuplicate(nums: List[int]) -> bool:
        size = len(nums)
        for i in range(0,size):
            for j in range(1, size):
                if i!=j and nums[i] == nums[j]:
                    return True
        return False
    

# another way of approch is sorting 
# we only have to iterate through the array once 
# sorting alogorithm takes O(nlog n) Space O(1) 

# another way of approch is using hashset
# we only have to iterate through once 
# if we sacrifice space complexity we can achive some time complexity
# here space complexity that hash map using is O(n) and time complexity is also O(n)


def containsDuplicateHashSet(nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
            print(hashset)
        return False
    
    
# Another approach: convert the list to a set if the len(set)==len(list), return False else: return True

def containsDuplicateHashSet2(nums: List[int]) -> bool:
        return (len(set(nums)) != len(list(nums)))
    
    
result = containsDuplicateHashSet2([1,2,3,4,1])
print(result)
from typing import List

# this is a simple memmory efficient way to concatitate two array rather than just appending it 
# here i am creating double the size of the array at the start
# and for in the range of length of array i am assigning the value from first to the length and
# i am repeating the same by asigning from the middle as i can get the start of the middle is the end length of array 

def getConcatenation(nums: List[int]) -> List[int]:

    ans = [0] * len(nums)*2
    for i in range(len(nums)):
        print(ans[i], nums[i])
        ans[i] = nums[i]
        ans[len(nums)+i] = nums[i]
        
    return ans




resutl = getConcatenation(nums=[1,2,1])
print(resutl)
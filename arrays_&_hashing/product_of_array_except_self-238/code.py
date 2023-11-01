def BruteForceSolution(arr):
    res=[0]*len(arr)
    for i in range(len(arr)):
        val=0
        for j in range(len(arr)):
            if i !=j:
                val *= arr[j]
        res[i]=val

BruteForceSolution([1,2,3,4])

def usingPrefixSuffix(nums):
    lent = len(nums)
    prefix = [0]*lent
    sufix = [0]*lent
    product = [0]*lent
    prefix[0]=1
    for i in range(1,lent):
        prefix[i]=nums[i-1]*prefix[i-1]
    sufix[lent-1]=1
    for i in range(n-2,-1,-1):
        sufix[i]=nums[i+1]*sufix[i+1]
    for i in range(lent):
        product[i]=prefix[i]*sufix[i]
    return product

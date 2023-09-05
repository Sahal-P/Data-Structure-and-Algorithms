from collections import Counter
from testcase import testcase

# the time complexity of the provided algorithm is O(n^3 * k) in the worst case, and the space complexity is O(k).
def characterReplacement_b(s: str, k: int) -> int:    
    longest = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            count = Counter(s[i:j])
            char=""
            for v in count:
                if (j-i) - count[v] <= k:
                    longest = max(longest,(j-i))
    return longest

# Linear time solution O(26*n) which O(n)
def characterReplacement(s: str, k: int) -> int:    
    count = {}
    res = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] = 1+ count.get(s[right], 0)
        if (right-left+1) - max(count.values()) >k:
            count[s[left]]-=1
            left+=1
        res = max(res, (right-left+1))
    return res
s = "AABABBA"
k = 1

testcasek= 100
print(characterReplacement(testcase, testcasek))
from collections import Counter
from testcase import testcase

# the time complexity of the provided algorithm is O(n^3 * k) in the worst case, and the space complexity is O(k).
def characterReplacement(s: str, k: int) -> int:    
    longest = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            count = Counter(s[i:j])
            char=""
            for v in count:
                if (j-i) - count[v] <= k:
                    longest = max(longest,(j-i))
    return longest
    
            
        
s = "AAAB"
k = 1

testcasek= 100
print(characterReplacement(testcase, testcasek))
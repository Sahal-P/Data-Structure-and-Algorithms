from collections import Counter, defaultdict
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
def characterReplacement_l(s: str, k: int) -> int:    
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

# O(n) time complexity setting max_count and avoiding lookup
def characterReplacement(s: str, k: int) -> int:
        max_len, max_count = 0, 0
        f = defaultdict(int)
        for i in range(len(s)):
            f[s[i]] += 1
            max_count = max(max_count, f[s[i]])
            if max_len - max_count >= k :
                f[s[i - max_len]] -= 1
            else:
                max_len += 1
        return max_len
    
def characterReplacement(s: str, k: int) -> int:
        count = {}
        maxf, l = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1
    
s = "AABABBA"
k = 1

testcasek= 100
print(characterReplacement(testcase, testcasek))
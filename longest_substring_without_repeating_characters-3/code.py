from testcase import testcase


# Brute force approch
def lengthOfLongestSubstring_b(s: str) -> int:
    sets = set()
    longest = 1
    for i in range(len(s)):
        sub = s[i]
        for j in range(i + 1, len(s)):
            sub += s[j]

            unique_chars = set()
            # duplicate_chars = set()
            is_dup = False
            for char in sub:
                # If the character is already in unique_chars, it is a duplicate
                if char in unique_chars:
                    is_dup = True
                else:
                    unique_chars.add(char)
            if not is_dup:
                sets.add(sub)
    for i in sets:
        longest = max(longest, len(i))

    return longest


def lengthOfLongestSubstring(s: str) -> int:
    sets = set()
    left, right = 0, 0
    longest = 0
    while right < len(s):
        print(s[right])
        if s[right] in sets:
            sets.remove(s[right])
            left += 1
            continue
        else:
            sets.add(s[right])
            longest = max(longest, right - left)
        right += 1

    return longest


case1 = "abcabcbb"
case2 = "bbbbb"
case3 = "pwwkew"

print(lengthOfLongestSubstring(case3))



def lengthOfLongestSubstring_s(s: str) -> int:
    seen = {}
    l = 0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, r - l + 1)
        seen[char] = r

    return length

    
def lengthOfLongestSubstring_m(s: str) -> int:
    window = {}
    left = 0
    right = 0
    ans = 0
    while right < len(s):
        c = s[right]
        right += 1
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1
        while window[c] > 1:
            tmp = s[left]
            left += 1
            window[tmp] -= 1
        ans = max(ans, right - left)

    return ans

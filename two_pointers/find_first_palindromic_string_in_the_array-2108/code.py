from typing import List


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def firstPalindrome(words: List[str]) -> str:
    
    for i in range(len(words)):
        check = is_palindrome(words[i])
        if check:
            return words[i]
    
    return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))
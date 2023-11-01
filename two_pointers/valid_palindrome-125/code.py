from functools import cache

# leetcode easy 
# this approch takes both space and time complexity of O(n)

def isPalindrome(s: str) -> bool:
    new_s = ""
    for i in s:
        if i.isalnum():
            new_s+=i.lower()
    rev_s = ""
    for i in range(len(new_s)-1,-1,-1):
        rev_s+=new_s[i]
        
    return rev_s == new_s

    # return new_s == new_s[::-1]
    
    
# Efficient way of doing this is using two pointers 
# which will take only O(1) space complexity

# if we are using the cache to memorize
# in the worst case space complexity will be the total number of non alphanumeric charecter which is O(1)

def isPalindrome2(s: str) -> bool:
    
    @cache
    def alnum(s: str) -> bool:
        return (ord('A') <= ord(s) <= ord('Z') or 
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9')
                )
        
    left, right = 0, len(s)-1
    
    while left < right:
        while left < right and not alnum(s[left]):
            left+=1
        while right > left and not alnum(s[right]):
            right-=1
        
        if s[left].lower() != s[right].lower():
            return False
        left, right = left+1, right-1
    
    return True

# most run time efficient 
def isPalindrome3(s: str) -> bool:
        s = ''.join([i for i in s if i.isalnum()]).lower()
        print(s)
        x = 0
        y = len(s) - 1
        while x < y:
            if s[x] != s[y]: return False
            x += 1
            y -= 1
        return True
    
print(isPalindrome3("A man, a plan, a canal: Panama"))

# isPalindrome("A man, a plan, a canal: Panamaxxx")
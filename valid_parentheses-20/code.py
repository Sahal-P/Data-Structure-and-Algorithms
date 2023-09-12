
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = { ")": "(", "}": "{", "]": "["}
    
    for i in s:
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                # print(stack[-1], closeToOpen[i])
                stack.pop()
            else:
                return False
        else:
            print(i)
            stack.append(i)
    return True if not stack else False

s = "()[]{}"
print(isValid(s))


def isValid( s: str) -> bool:
    stack = []
    match = {'(':')', '{':'}', '[':']'}
    for char in s:
        if char in match:
            stack.append(char)
        elif len(stack) == 0 or match[stack[-1]] != char:
            return False
        else:
            stack.pop()
    return len(stack) == 0
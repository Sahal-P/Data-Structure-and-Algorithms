from typing import List

# brute forece approch
def sequentialDigits_b(low: int, high: int) -> List[int]:
    result = []
    for num in range(low, high):
        num_str = str(num)
        incremented_digits = [int(digit) for digit in num_str]
        is_sequential = True
        for i in range(len(incremented_digits)-1):
            if incremented_digits[i] + 1 != incremented_digits[i+1]:
                is_sequential = False
                break
        if is_sequential:
            result.append(num)
    return result
# contant time
def sequentialDigits(low: int, high: int) -> List[int]:
    result = []
    low_digit, high_digit = len(str(low)), len(str(high))
    for digit in range(low_digit, high_digit+1):
        for start in range(1, 9):
            if start + digit > 10:
                break
            num = start
            prev = start
            for i in range(digit-1):
                num = num * 10 
                prev += 1
                num += prev
            if low <= num <= high:
                result.append(num)
    print(result)          
    return result

# most efficient
def sequentialDigits_e(low: int, high: int) -> List[int]:
    t = '123456789'
    l = []
    for i in range(len(t)):
        for j in range(i+1, len(t)+1):
            if low <= int(t[i:j]) <= high:
                l.append(int(t[i:j]))
    return sorted(l)
low = 100
high = 300

print(sequentialDigits_e(low, high))
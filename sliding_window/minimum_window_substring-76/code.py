from collections import defaultdict, Counter
from testcase import testcase

# brute force methode
def minWindow_(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    lis = []
    a = set(t)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            b = set(s[i:j])
            result = all(idx in b for idx in a)
            if result:
                lis.append(s[i:j])

    minmW = min(lis, key=lambda x: len(x))
    return minmW

def minWindow_b2(s: str, t:str) -> str:
    lis = []
    need = Counter(t)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            have = dict({x: 0 for x in t}) 
            txt = s[i:j]
            for k in txt:
                if k in have:
                    have[k] = 1+ have.get(k,0)
            have_char = all( val >= need[key] for key, val in have.items())
            if have_char:
                lis.append(txt)
    minmW = min(lis, key=lambda x: len(x))
    return minmW


# Linear time solution 

def minWindow( s: str, t: str) -> str :
    
    countT, window = {}, {}
    
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    
    have , need = 0, len(countT)
    
    for r in range(len(s)):
        c = s[r]
        
        window[c] = 1 + window.get(c, 0)
        
    print(window, countT)
    
s = "ADOBECODEBANC"
t = "ABC"

test1_s = "aaaaaaaaaaaabbbbbcdd"
test1_t = "abcdd"
print(minWindow(testcase[0], testcase[1]))


testd = {
    1960: {"b": 2, "d": 0},
    1970: {"b": 0, "d": 1},
    2009: {"b": 1, "d": 0},
    2010: {"b": 1, "d": 1},
    2015: {"b": 0, "d": 1},
    2020: {"b": 0, "d": 1},
}


def test(data: dict):
    year = 0
    max_alive = 0
    alive = 0
    for key, val in data.items():
        print(alive, val["b"] - val["d"])
        num = val["b"] - val["d"]
        if num > max_alive:
            year = key
        alive += num
        max_alive = max(max_alive, alive)
    print(alive, year)


# test(testd)

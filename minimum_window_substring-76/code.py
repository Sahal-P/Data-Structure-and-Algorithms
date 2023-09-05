from collections import defaultdict, Counter

def minWindow( s: str, t: str ) -> str:
    if len(s)<len(t):
        return ""
    
    lis = []
    a = set(t)
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            b = set(s[i:j])
            result = all(idx in b for idx in a)
            if result:
                lis.append(s[i:j])
    
    print(lis)
    minmW = min(lis, key=lambda x: len(x))
    print(minmW)
    return minmW
s = "ADOBECODEBANC" 
t = "ABC"

test1_s="aaaaaaaaaaaabbbbbcdd"
test1_t= "abcdd"
# print(minWindow('bbaa', 'aba'))


testd = {
    1960: {'b':2, 'd':0},
    1970: {'b':0, 'd':1},
    2009: {'b':1, 'd':0},
    2010: {'b':1, 'd':1},
    2015: {'b':0, 'd':1},
    2020: {'b':0, 'd':1},
}
def test(data: dict):
    year = 0
    max_alive = 0
    alive = 0
    for key, val in data.items():
        print(alive ,val['b'] - val['d'])
        num = val['b'] - val['d']
        if num >max_alive:
            year=key
        alive += num
        max_alive = max(max_alive,alive)
    print(alive,year)
test(testd)
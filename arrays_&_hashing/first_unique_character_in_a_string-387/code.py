from collections import Counter, defaultdict


def firstUniqChar( s: str ) -> int:
        m = defaultdict(int)
        c = defaultdict(int)
        count = 0
        for i in s:
                m[i] +=1
                c[i] = count
                count+=1
        result = -1 if all(value > 1 for value in m.values()) else None
        if result is None:
                min_count = min(m.values())
                min_keys = [key for key, value in m.items() if value == min_count]
                min_key = min(min_keys, key=m.get)
                pos = s.find(min_key)
                print(pos, m)
                return 
        print(result)
        return result
        
# best solution
def firstUniqChar_1( s: str) -> int:
        key = 'abcdefghijklmnopqrstuvwxyz'
        idx = 10**5
        print(idx)
        for i in key:
            x = s.find(i)
            if x != -1 and x == s.rfind(i):
                idx = min(idx,x)
        return idx if idx != 10**5 else -1


s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

firstUniqChar_1(s1)
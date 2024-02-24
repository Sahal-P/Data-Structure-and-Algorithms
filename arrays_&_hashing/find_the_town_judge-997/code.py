from collections import defaultdict
from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:
    incoming = defaultdict(int, {i: 0 for i in range(1, n+1)})
    outgoing = defaultdict(int, {i: 0 for i in range(1, n+1)})
    for i in trust:
        outgoing[i[0]] += 1
        incoming[i[1]] += 1
    for key, val in incoming.items():
        if n - 1  == val:
            if outgoing[key] == 0:
                return key
    
    return -1


# n = 2
# trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

print(findJudge(n, trust))

# n = 3
# trust = [[1,3],[2,3],[3,1]]


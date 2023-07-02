import collections

import heapq

def topKFrequent(arr,k):
   dic=collections.defaultdict(int)
   for i in arr:
    dic[i]+=1
   result = sorted(dic, key=lambda x: dic[x], reverse=True)
   print(result[:k])
   return result[:k]


arr = [1,1,1,2,2,3]
topKFrequent(arr,2)

def usingHeap(arr, k):
    countes = collections.Counter(nums)
    min_heap = []
    for el, freq in countes.items():
      heapq.heappush(min_heap,(freq,el))
      if len(min_heap)>k:
         heapq.heappop(min_heap)
    res=[num for el, num in min_heap]
    return res
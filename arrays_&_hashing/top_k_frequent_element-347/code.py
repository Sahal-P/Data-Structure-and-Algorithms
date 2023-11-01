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

def usingBucketSort(arr,k):
   count = {}
   freq = [[] for i in range(len(arr)+1)]
   for i in arr:
      count[i] = 1 + count.get(i, 0)
   for n, c in count.items():
      freq[c].append(n)
   res =[]
   for i in range(len(freq)-1,0,-1):
      for n in freq[i]:
         res.append(n)
         if len(res)==k:
            return res
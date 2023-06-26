import collections



def topKFrequent(arr,k):
   dic=collections.defaultdict(int)
   for i in arr:
    dic[i]+=1
   result = sorted(dic, key=lambda x: dic[x], reverse=True)
   return result[:k]


arr = [1,1,1,2,2,3]
topKFrequent(arr,2)
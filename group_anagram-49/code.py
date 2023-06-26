from typing import List

#this is done by sorting each string 
#and added in the hashmap as key as word and val as list of anagrams
#time complexity will be O(m*n log n)

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word]=[word]
            else:
                dic[sorted_word].append(word)
        return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]

groupAnagram(strs)


from collections import defaultdict

#problem can be solved in O(m*n)
#this is an efficient way by declaring the needed space firstly for counting each string 

def groupAnagrams(strs):
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()
        
strs = ["eat","tea","tan","ate","nat","bat"]

groupAnagrams(strs)
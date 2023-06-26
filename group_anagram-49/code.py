from typing import List


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
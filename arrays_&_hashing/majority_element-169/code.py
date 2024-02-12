from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    count = Counter(nums)
    max_key, max_count = count.most_common(1)[0]
    print(max_key, max_count)
    return max_key

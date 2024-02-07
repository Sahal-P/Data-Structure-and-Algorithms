from collections import Counter


# solved using hash map
def frequencySort(s: str) -> str:
    char_count = Counter(s)
    sorted_items = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    result = "".join(string * count for string, count in sorted_items)
    return result

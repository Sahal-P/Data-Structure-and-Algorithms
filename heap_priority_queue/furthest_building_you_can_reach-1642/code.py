from typing import List
import heapq


# O(n logn)
def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    heap = []  # max heap of bricks
    length = len(heights) - 1

    for i in range(length):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        bricks -= diff
        heapq.heappush(heap, -diff)
        if bricks < 0:
            if ladders == 0:
                return i
            ladders -= 1
            add_bricks = -heapq.heappop(heap)
            print(add_bricks, i, diff)
            bricks += add_bricks

    return length



def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    i = 0
    while i < len(heights) - 1:
        if heights[i] >= heights[i + 1]:
            i += 1
            continue
        else:
            diff = heights[i + 1] - heights[i]
            if diff > bricks:
                if ladders > 0:
                    ladders -= 1
                    i += 1
                    continue
                else:
                    break
            else:
                bricks -= diff
                i += 1
                continue

    return i

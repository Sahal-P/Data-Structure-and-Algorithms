from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    print(len(heights))
    ladders_, bricks_ = ladders, bricks
    i = 0
    j = 0

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

    while j < len(heights) - 1:
        if heights[j] >= heights[j + 1]:
            j += 1
            continue
        else:
            diff = heights[j + 1] - heights[j]
            if ladders_ > 0:
                ladders_ -= 1
                j += 1
                continue
            elif bricks_ >= diff:
                bricks_ -= diff
                j += 1
                continue
            else:
                break

    return max(i, j)

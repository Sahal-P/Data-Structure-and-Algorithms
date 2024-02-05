class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        arr = self.arr
        arr.sort()
        number = len(arr)
        # print(arr, number)
        if number % 2 == 0:
            mid_1 = arr[number // 2 - 1]
            mid_2 = arr[number // 2]
            m = (mid_1 + mid_2) / 2
        else:
            idx = number // 2
            m = arr[idx]

        return m


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

medianFinder = MedianFinder()
medianFinder.addNum(-1)
print(medianFinder.findMedian())
medianFinder.addNum(-2)
print(medianFinder.findMedian())

medianFinder.addNum(-3)
print(medianFinder.findMedian())
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())
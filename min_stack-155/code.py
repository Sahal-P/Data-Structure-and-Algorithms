class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


val = [0,-2,4]

obj = MinStack()

for i in range(len(val)):
    obj.push(val[i])
obj.pop()
param_3 = obj.top()

param_4 = obj.getMin()
print(param_3,param_4)
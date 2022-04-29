# 232
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for z in range(len(self.s1)-1):
            self.s2.append(self.s1.pop())
        ans = self.s1.pop()
        for z in range(len(self.s1)-1):
            self.s1.append(self.s2.pop())
        return ans

    def peek(self) -> int:
        for z in range(len(self.s1)-1):
            self.s2.append(self.s1.pop())
        ans = self.s1[0]
        for z in range(len(self.s1)-1):
            self.s1.append(self.s2.pop())
        return ans

    def empty(self) -> bool:
        return len(self.s1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
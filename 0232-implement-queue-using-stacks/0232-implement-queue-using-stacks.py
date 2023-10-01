class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.s1.append(x)
        else:
            for i in self.s1[::-1]:
                self.s2.append(i)

            self.s1.clear()
            self.s1.append(x)

            for i in self.s2[::-1]:
                self.s1.append(i)
            self.s2.clear()        

    def pop(self) -> int:
        t = self.s1[-1]
        self.s1.pop()
        return t

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        if len(self.s1) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self):
        self.capacity = 100
        self.queue = [0]*self.capacity
        self.front = 0
        self.rear = 0
        self.count = 0
        
    def push(self, x: int) -> None:
        if self.count == self.capacity:
            return
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        
    def pop(self) -> int:
        if self.empty():
            return -1
        val = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.queue[self.front]
        
    def empty(self) -> bool:
        return self.count == 0
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
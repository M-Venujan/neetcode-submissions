class MinStack:

    def __init__(self):
        self.items = []
        self.mini = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.mini:
            self.mini.append(min(val, self.mini[-1]))
        else:
            self.mini.append(val)
        

    def pop(self) -> None:
        if self.items:
            self.items.pop()
            self.mini.pop()
        

    def top(self) -> int:
        if self.items:
            return self.items[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        

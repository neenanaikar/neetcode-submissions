class MinStack:

    def __init__(self):
        self.main_stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.min_stack.pop()
        self.main_stack.pop()
        
    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        

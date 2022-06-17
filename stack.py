
class Stack:
   
    def __init__(self, size):
        self.capacity = size
        self.top = -1
        self.stack = []
        
    def isEmpty(self):
        return self.top == -1
        
    def isFull(self):
        return self.top == self.capacity-1
        
    def push(self, value):
        if self.isFull():
            print("Stack is full!")
            return
        self.top += 1
        self.stack.append(value)
      
        
    def pop(self):
        if self.isEmpty():
            print('Stack is empty!')
            return
        self.stack.pop()
        self.top -= 1
        
    def peek(self):
        return self.stack[self.top]
        
        
    def print_stack(self):
        for i in range(len(self.stack)-1, -1):
            print(self.stack[i])
            


stack = Stack(10)
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
        

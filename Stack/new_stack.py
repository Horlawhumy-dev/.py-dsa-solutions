

from xmlrpc.client import boolean


class Stack:

    def __init__(self) -> None:
        self.items = []


    def is_empty(self) -> boolean:
        return not self.items
    
    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


    def __str__(self) -> str:
        return str(self.items)




if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(3)
    s.push(9)
    s.push(10)
    s.push(13)
    print(s.peek())
    print(s.pop()) 
    print(s)
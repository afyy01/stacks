class Stack:
    def __init__(self, n):
        self.stack = []
        self.n = n #maximum number of items in the stack
    #methods of stack
    #push - adding new item to the stock

    def push(self, k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("Stack is full")

    #pop - removing top items from the stack
    def pop(self):
        if len(self.stack) == 0: #if stack is empty pop nothhing
            print("Stack is empty")
        else:
            self.stack.pop(-1) #deleting lasr item from the stack and returning it
    #top - inding the top item fromthe stack
    def top(self):
        if len(self.stack) ==0:
            print("The stack is empty")
        else:
            return self.stack[-1]

    #custom methods - our own methods or functions that we need in our project
    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)


#create of object of stack
s = Stack(6)
s.display()
s.push(3)
s.display()

s.push(3)
s.display()

s.push(6)
s.display()

s.push(5)
s.display()

s.push(2)
s.display()

s.push(1)
s.display()

s.push(9)
s.display()

s.push(7)
s.display()

s.pop()
s.display()

print(s.size())

print(s.top())
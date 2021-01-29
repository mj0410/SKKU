class stack :
    def __init__(self) :
        self.items = []
    def isEmpty(self) :
        return self.items == []
    def push(self, item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def print(self) :
        print(self.items)
    def peek(self) :
        return self.items[len(self.items)-1]
    def size(self) :
        return len(self.items)

class queue :
    def __init__(self) :
        self.items = []
        self.front = 0
        self.rear = 0
    def isEmpty(self) :
        return (self.front == self.rear)
    def enqueue(self, items) :
        self.items.append(items)
        self.rear = self.rear+1
    def dequeue(self) :
        self.front = self.front+1
        return self.items[self.front-1]
    def print(self) :
        print(self.items[self.front:self.rear])
    def peek(self) :
        return self.items[self.front]
    def end(self) :
        return self.items[self.rear]
    def size(self) :
        return len(self.items[self.front:self.rear])

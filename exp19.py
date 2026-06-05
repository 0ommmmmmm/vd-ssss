class Node:
    def __init__(self , info , priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self , node):
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.priority)
    
    def delete(self):
        self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print(x.info + ' - ' + str(x.priority))

pqueue = PriorityQueue()

pqueue.insert(Node("A",1))
pqueue.insert(Node("B",2))
pqueue.insert(Node("H",8))
pqueue.insert(Node("R",17))
pqueue.insert(Node("G",6))

pqueue.show()
print("--------")
pqueue.delete()
pqueue.show()
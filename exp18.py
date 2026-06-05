q = []

def enqueue():
    if len(q) == size:
        print("queue is full!!!")
    else:
        element = int(input("enter the element :"))
        q.append(element)
        print(element , "is added")

def dequeue():
    if not q:
        print("stack is empty")
    else:
        m = q.pop(0)
        print(m,"is removed.")

def dispaly():
    print(q)

size = int(input("enter the queue size :"))

while True:
    print("Choose 1.add , 2.delete , 3.display , 4.quit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        dispaly()
    else:
        break   





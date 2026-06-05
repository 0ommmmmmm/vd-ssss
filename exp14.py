max_size = int(input("enter ur max stack"))

stack =[]

while True:
    print("choose \n1.ADD , 2.POP , 3.Display , 4.EXIT")

    choice = int(input("Enter ur element..."))

    if choice == 1:
        if len(stack) < max_size:
            item = int(input("Enter ur element"))
            stack.append(item)
            print(item , "Added")
        else:
            print("Stack overflow")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack underflow ")
        else:
            gone = stack.pop()
            print(gone , "Popped")

    elif choice == 3:
        print(stack)

    elif choice == 4:
        print("Exit ")
        break

    else:
        print("Invalid input")

        
import time 
import matplotlib.pyplot as plt 
import tracemalloc

def linearsearch(array , x , n):
    for i in range(0,n):
        if array[i] == x:
            return i
    return -1

array = [int(b) for b in input("enter the elements...").split()]
x = int(input("enter element search..."))
n = len(array)

start = time.process_time()
tracemalloc.start()
result = linearsearch(array , x ,n)
end = time.process_time()

print("space req :", tracemalloc.get_traced_memory())
print("time required :" , (end-start))
tracemalloc.stop()

if result == -1:
    print("not found .")
else:
    print("found at : ", result)

plt.xlabel("list length")
plt.ylabel("time required")
plt.plot(array , array , label ="linear search")
plt.grid()
plt.legend()
plt.show()
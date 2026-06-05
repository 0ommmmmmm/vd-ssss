import time
import matplotlib.pyplot as plt 
import tracemalloc

def fib_dp(num):
    if n == 0:
        print("Entewr nterms more than 0 ...")
        return 0
    
    arr = [0,1]

    if n ==1:
        print("Fibonnaci series :",[0])
    elif n==2:
        print("Fibonnaci series :",[0,1])

    else:
        for i in range(2,num):
            arr.append(arr[i-1] + arr[i-2])
        print("fibonnaci Series :",arr)

    return arr[num - 2]

n = int(input("enter range of Stack :"))

tracemalloc.start()
start = time.process_time()

result = fib_dp(n)

end = time.process_time()
print("space req :",tracemalloc.get_traced_memory())
print("time req", (end-start))

tracemalloc.stop()

elements = list(range(n))
times = [end - start]*n

plt.xlabel("list length ")
plt.ylabel("time required")
plt.plot(elements ,times , label="fibonacci series")
plt.grid()
plt.legend()
plt.show()

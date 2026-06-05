import time
import matplotlib.pyplot as plt

def binary_search(arr, k, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binary_search(arr, k, low, mid - 1)
    else:
        return binary_search(arr, k, mid + 1, high)

arr = [int(x) for x in input("Enter sorted array: ").split()]
k = int(input("Enter search element: "))

start = time.process_time()
result = binary_search(arr, k, 0, len(arr) - 1)
end = time.process_time()

print(f"Time: {end - start:.6f}s")
if result == k:
    print(" found ", result)
else:
    print("index found")

plt.plot([len(arr)], [end - start], marker='o', label="Binary Search")
plt.xlabel("List Length")
plt.ylabel("Time (s)")
plt.legend()
plt.grid()
plt.show()
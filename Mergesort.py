import time
import numpy as np
import matplotlib.pyplot as plt

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# Benchmark
sizes = [i * 1000 for i in range(1, 10)]
times = []

for n in sizes:
    arr = np.random.randint(1000, size=n).tolist()
    start = time.process_time()
    merge_sort(arr)
    end = time.process_time()
    t = end - start
    times.append(t)
    print(f"Merge Sort | {n} elements | {t:.4f}s")

# Plot
plt.plot(sizes, times, label="Merge Sort")
plt.xlabel("List Length")
plt.ylabel("Time (s)")
plt.title("Merge Sort Time Complexity")
plt.legend()
plt.grid()
plt.show()
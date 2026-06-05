import time
import numpy as np
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Benchmark & Plot
sorts = {"Bubble Sort": bubble_sort, "Selection Sort": selection_sort, "Insertion Sort": insertion_sort}
sizes = [i * 1000 for i in range(1, 10)]

for name, fn in sorts.items():
    times = []
    for n in sizes:
        arr = np.random.randint(1000, size=n).tolist()
        start = time.process_time()
        fn(arr)
        end = time.process_time()
        times.append(end - start)
        print(f"{name} | {n} elements | {end-start:.4f}s")
    plt.plot(sizes, times, label=name)

plt.xlabel("List Length")
plt.ylabel("Time (s)")
plt.legend()
plt.grid()
plt.show()
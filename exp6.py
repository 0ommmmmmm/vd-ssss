import time
import numpy as np
import matplotlib.pyplot as plt


# ── BUBBLE SORT ──────────────────────────────────────────────
# Compare neighbors, bubble the largest to the end each pass.
# Time: O(n²)  |  Space: O(1)
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):   # last i elements already sorted
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]   # Python swap, no temp needed


# ── SELECTION SORT ───────────────────────────────────────────
# Find the smallest element in the unsorted part, place it at front.
# Time: O(n²)  |  Space: O(1)
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):           # scan for minimum
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]  # place minimum at position i


# ── INSERTION SORT ───────────────────────────────────────────
# Pick one element, shift everything larger to the right, insert it.
# Time: O(n²)  |  Space: O(1)
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i] # element to be placed correctly
        j = i - 1
        while j >= 0 and a[j] > key:   
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key      # drop key into its correct spot


# ── BENCHMARK SETUP ──────────────────────────────────────────
sorts = [
    {"name": "Bubble Sort",    "fn": bubble_sort},
    {"name": "Selection Sort", "fn": selection_sort},
    {"name": "Insertion Sort", "fn": insertion_sort},
]

sizes = [i * 1000 for i in range(1, 10)]   # [1000, 2000, ..., 9000]

plt.xlabel("List Length (elements)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Comparison")

# ── RUN EACH SORT ON INCREASING INPUT SIZES ──────────────────
for sort in sorts:
    times = []
    total_start = time.process_time()

    for size in sizes:
        arr = np.random.randint(1000, size=size)   # random array of given size
        
        start = time.process_time()
        sort["fn"](arr)
        end = time.process_time()

        elapsed = end - start
        times.append(elapsed)
        print(f"{sort['name']:15s} | {size:>5} elements | {elapsed:.4f}s")

    total_time = time.process_time() - total_start
    print(f"  → Total for {sort['name']}: {total_time:.4f}s\n")

    plt.plot(sizes, times, label=sort["name"], marker="o")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

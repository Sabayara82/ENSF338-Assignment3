
#inefficient solution 
def inefficient_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
#worst-case time complexity: O(n) for the length of the array, n

#efficient solution

def efficient_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#worst case time complexity: O(log n) for the length of the array, n


#experiment to check this code
import random
import timeit
import matplotlib.pyplot as plt

arr = [i for i in range(100000)]
x = random.randint(0, 99999)
linear_times = []
binary_times = []

for i in range(100):
    linear_time = timeit.timeit(lambda: inefficient_search(arr, x), number=1000)
    binary_time = timeit.timeit(lambda: efficient_search(arr, x), number=1000)
    linear_times.append(linear_time)
    binary_times.append(binary_time)

#plotting measured values
plt.hist(linear_times, bins=20, alpha=0.5, label='Linear Search')
plt.hist(binary_times, bins=20, alpha=0.5, label='Binary Search')
plt.legend(loc='upper right')
plt.title('Search Algorithm Comparison')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Print aggregate
print("Average time for linear search: ", sum(linear_times)/len(linear_times))
print("Average time for binary search: ", sum(binary_times)/len(binary_times))
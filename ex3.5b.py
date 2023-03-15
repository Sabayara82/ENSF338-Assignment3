#inefficient solution
import heapq

def inefficient_priority_queue(data):
    heap = []
    for item in data:
        heapq.heappush(heap, item)  
    result = []
    while heap:
        result.append(heapq.heappop(heap)) 
    return result
#worst case time complexity: O(n log n) for the length of the queue, n

#efficient solution
def efficient_priority_queue(data):
    return sorted(data)
#worst case time complexity: O(n log n), for the length of the queue,
# n (however, the memory used is less in this code implementation)


#experiement to check this code
import random
import timeit
import matplotlib.pyplot as plt

data = [random.randint(1, 1000) for _ in range(1000)]

inefficient_times = []
for i in range(100):
    start_time = timeit.default_timer()
    inefficient_priority_queue(data)
    end_time = timeit.default_timer()
    inefficient_times.append(end_time - start_time)

efficient_times = []
for i in range(100):
    start_time = timeit.default_timer()
    efficient_priority_queue(data)
    end_time = timeit.default_timer()
    efficient_times.append(end_time - start_time)

# Plotting measured values
plt.hist(inefficient_times, bins=20, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, bins=20, alpha=0.5, label='Efficient')
plt.legend()
plt.show()

# Print aggregate
print('Inefficient - Min time:', min(inefficient_times))
print('Efficient - Min time:', min(efficient_times))
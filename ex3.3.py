import sys

# Initialize an empty list
lst = []
capacity = sys.getsizeof(lst)

# Loop from 0 to 63 integers
for i in range(64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != capacity:
        print(f"Capacity changed at {i} elements: {capacity} bytes -> {new_capacity} bytes")
        capacity = new_capacity

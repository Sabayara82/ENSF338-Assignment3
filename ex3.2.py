import json
import requests
import matplotlib.pyplot as plt
import time

def load_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def load_tasks(url):
    response = requests.get(url)
    tasks = json.loads(response.text)
    return tasks

def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

def find_best_midpoint(arr, target):
    start = 0
    end = len(arr) - 1
    best_mid = (start + end) // 2
    best_time = float('inf')
    for i in range(start, end+1):
        mid = i
        t0 = time.time()
        binary_search(arr, target, start, mid)
        t1 = time.time()
        elapsed = t1 - t0
        if elapsed < best_time:
            best_time = elapsed
            best_mid = mid
    return best_mid

if __name__ == '__main__':
    data_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json'
    tasks_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json'
    data = load_data(data_url)
    tasks = load_tasks(tasks_url)
    best_mids = []
    for task in tasks:
        best_mid = find_best_midpoint(data, task)
        best_mids.append(best_mid)
        print(f"Task {task}: best midpoint = {best_mid}")

    plt.scatter(tasks, best_mids)
    plt.xlabel('Search task')
    plt.ylabel('Best midpoint')
    plt.title('Best midpoint for each search task')
    plt.show()
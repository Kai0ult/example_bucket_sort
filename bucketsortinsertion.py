import random
import time
from datetime import datetime


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # print(f"   - Balde ordenado: {arr}")
    return arr


def bucket_sort(arr, num_buckets=10):
    if len(arr) == 0:
        return arr

    min_value, max_value = min(arr), max(arr)
    bucket_range = (max_value - min_value) // num_buckets + 1

    buckets = [[] for _ in range(num_buckets)]

    # print("\n Distribuindo elementos nos baldes:")
    for num in arr:
        index = (num - min_value) // bucket_range
        buckets[index].append(num)

    sorted_arr = []
    for i, bucket in enumerate(buckets):
        sorted_bucket = insertion_sort(bucket)
        sorted_arr.extend(sorted_bucket)

    print("Array final ordenado:", sorted_arr)
    return sorted_arr


array = [random.randint(0, 9223372036854775807) for _ in range(200000)]
# print(" Array original:", array)

start_time = time.time()
sorted_array = bucket_sort(array)
end_time = time.time()

time_seg = datetime.fromtimestamp(end_time - start_time)

print(time_seg.strftime('%M:%S'))
print(f"Ordenação concluída em {end_time - start_time:.5f} segundos!")

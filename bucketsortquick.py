import random
import time
from datetime import datetime


def quick_sort(bucket):

    if len(bucket) <= 1:
        return bucket
    pivot = bucket[len(bucket) // 2]
    left = [x for x in bucket if x < pivot]
    middle = [x for x in bucket if x == pivot]
    right = [x for x in bucket if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bucket_sort(array, num_buckets=100):

    if len(array) == 0:
        return array

    buckets = [[] for _ in range(num_buckets)]

    min_value, max_value = min(array), max(array)
    bucket_range = (max_value - min_value) / num_buckets

    for num in array:
        index_b = int((num - min_value) / bucket_range)
        if index_b == num_buckets:
            index_b -= 1
        buckets[index_b].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(quick_sort(bucket))

    print("Array final ordenado:", sorted_array)
    return sorted_array


array = [random.randint(0, 9223372036854775807) for _ in range(200000)]
# print(" Array original:", array)

start_time = time.time()
sorted_array = bucket_sort(array)
end_time = time.time()

time_seg = datetime.fromtimestamp(end_time - start_time)

print(time_seg.strftime('%M:%S'))
print(f"Ordenação concluída em {end_time - start_time:.5f} segundos!")

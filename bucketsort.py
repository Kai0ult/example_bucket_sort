import random


def bucket_sort(arr, num_buckets=10):
    if len(arr) == 0:
        return arr

    min_value, max_value = min(arr), max(arr)
    bucket_range = (max_value - min_value) // num_buckets + 1

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = (num - min_value) // bucket_range
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


array = [random.randint(0, 1000) for _ in range(100)]


sorted_array = bucket_sort(array)


print("Array original:", array)
print("Array ordenado:", sorted_array)

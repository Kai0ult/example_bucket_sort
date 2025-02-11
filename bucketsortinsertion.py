import random


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(f"   - Balde ordenado: {arr}")
    return arr


def bucket_sort(arr, num_buckets=10):
    if len(arr) == 0:
        return arr

    min_value, max_value = min(arr), max(arr)
    bucket_range = (max_value - min_value) // num_buckets + 1

    print(
        f"\n Min: {min_value}, Max: {max_value}, Intervalo por balde: {bucket_range}")

    buckets = [[] for _ in range(num_buckets)]

    print("\n Distribuindo elementos nos baldes:")
    for num in arr:
        index = (num - min_value) // bucket_range
        buckets[index].append(num)

    for i, bucket in enumerate(buckets):
        print(f"   Balde {i}: {bucket}")

    sorted_arr = []
    for i, bucket in enumerate(buckets):
        sorted_bucket = insertion_sort(bucket)
        sorted_arr.extend(sorted_bucket)

    print("\n Array final ordenado:", sorted_arr)
    return sorted_arr


array = [random.randint(0, 10) for _ in range(20)]
print(" Array original:", array)
sorted_array = bucket_sort(array)

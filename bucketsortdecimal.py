import random
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucketSort(array, num_buckets=10):
    bucket = []

    for i in range(num_buckets):
        bucket.append([])

    min_value, max_value = min(array), max(array)
    bucket_range = (max_value - min_value) // num_buckets + 1

    for j in array:
        index_b = int(bucket_range * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        print(insertion_sort(bucket[i]))
        bucket[i] = insertion_sort(bucket[i])
       
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = []
for i in range(200000):
    array.append(round(random.random(),3))
print("Sorted Array in descending order is")
print(bucketSort(array))

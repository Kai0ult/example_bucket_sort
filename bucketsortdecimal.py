import random
import time
from datetime import datetime

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
    bucket_range = (max_value - min_value) / num_buckets + 1

    for j in array:
        index_b = int((j - min_value) / bucket_range)
        bucket[index_b].append(j)

    for i in range(num_buckets):
        bucket[i] = insertion_sort(bucket[i])
        #print(bucket[i])
       
    k = 0
    for i in range(num_buckets): 
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    print("Array final ordendado: ", array)
    

array = []
for i in range(200000):
    array.append(round(random.random(),3))
    
start_time = time.time()
bucketSort(array)
end_time = time.time()

time_seg = datetime.fromtimestamp(end_time - start_time)

print(time_seg.strftime('%M:%S'))
print(f"Ordenação concluída em {end_time - start_time:.5f} segundos!")


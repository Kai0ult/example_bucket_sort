import random
import time
from datetime import datetime

def bucket_sort_recursive(bucket, depth=0, max_depth=10):
    if len(bucket) <= 1 or depth >= max_depth:
        return bucket  
    
    num_buckets = 10
    min_value, max_value = min(bucket), max(bucket)
    bucket_range = (max_value - min_value) / num_buckets if max_value != min_value else 1

    sub_buckets = [[] for _ in range(num_buckets)]

    for num in bucket:
        index_b = int((num - min_value) / bucket_range)
        if index_b == num_buckets:  
            index_b -= 1
        sub_buckets[index_b].append(num)

    sorted_bucket = []
    for sub_bucket in sub_buckets:
        sorted_bucket.extend(bucket_sort_recursive(sub_bucket, depth + 1, max_depth))

    return sorted_bucket

def bucket_sort(array, num_buckets=10):
    
    if len(array) == 0:
        return array
  
    buckets = [[] for _ in range(num_buckets)]
 
    min_value, max_value = min(array), max(array)
    bucket_range = (max_value - min_value) / num_buckets if max_value != min_value else 1
 
    for num in array:
        index_b = int((num - min_value) / bucket_range)
        if index_b == num_buckets:  
            index_b -= 1
        buckets[index_b].append(num)
 
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket_sort_recursive(bucket))

    print("Array final ordenado: ", sorted_array)
    return sorted_array


array = random.sample(range(9223372036854775807), 200000)

start_time = time.time()
sorted_array = bucket_sort(array)
end_time = time.time()

time_seg = datetime.fromtimestamp(end_time - start_time)

print(time_seg.strftime('%M:%S'))
print(f"Ordenação concluída em {end_time - start_time:.5f} segundos!")

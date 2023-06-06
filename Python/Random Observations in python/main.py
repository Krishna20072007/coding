import random
import time
from collections import Counter

n = int(input("Enter a number: "))

num = [random.randint(1, 100) for _ in range(n)]

start_time = time.time()

mode_count = Counter(num).most_common(1)[0][1]

average = sum(num) / n

end_time = time.time()
execution_time = end_time - start_time

print(f"Total Numbers: {n}")
print(f"Average: {average}")
print(f"Mode count: {mode_count}")
print(f"Execution Time: {execution_time} seconds")

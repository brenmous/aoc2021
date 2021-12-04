import numpy as np

with open('input.txt', 'r') as f:
    numbers = [int(line) for line in f.readlines()]

count = np.where(np.diff(numbers) > 0)[0].size
print(count)

count = 0
for i, n in enumerate(numbers):
    if i == len(numbers) - 1:
        break
    elif numbers[i + 1] - n > 0:
        count += 1
print(count)

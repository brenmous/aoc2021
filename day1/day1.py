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

prev = None
count = 0
for i in range(len(numbers)):
    s = sum(numbers[i: i + 3])
    if prev is not None and s > prev:
        count += 1
    prev = s
print(count)

count = 0
for i in range(len(numbers)):
    try:
        if numbers[i + 3] > numbers[i]:
            count += 1
    except IndexError:
        continue
print(count)


print(len([n for i, n in enumerate(numbers) if i < len(numbers) - 3 and numbers[i + 3] > numbers[i]]))

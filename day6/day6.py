from collections import defaultdict
from functools import lru_cache

with open("input.txt", "r") as f:
    fishes = [int(x) for x in f.read().split(',')]


@lru_cache
def simulate(fish, day):
    if day == 0:
        return 1
    elif fish == 0:
        return simulate(6, day - 1) + simulate(8, day - 1)
    else:
        return simulate(fish - 1, day - 1)


cycles = 256
fish_count = defaultdict(int)
for fish in fishes:
    fish_count[fish] += 1
unique_fish = list(set(fishes))
total = []
for fish in unique_fish:
    total.append(simulate(fish, cycles) * fish_count[fish])
print(sum(total))

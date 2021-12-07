from collections import defaultdict
import sys

with open("input.txt", "r") as f:
    crabs = [int(x) for x in f.read().split(',')]

def brute(crabs):
    num_crabs = defaultdict(int)
    for crab in crabs:
        num_crabs[crab] += 1
    possible_positions = range(1, max(crabs) + 1)
    unique_crabs = sorted(list(set(crabs)))
    best_cost = sys.maxsize
    best_pos = 0
    for pos in possible_positions:
        fuel = 0
        for crab in unique_crabs:
            fuel += abs(crab - pos) * num_crabs[crab]
            if fuel >= best_cost:
                break
        if fuel < best_cost:
            best_cost = fuel
            best_pos = pos

    return best_pos, best_cost

#print(brute(crabs))

def brute_2(crabs):
    num_crabs = defaultdict(int)
    for crab in crabs:
        num_crabs[crab] += 1
    possible_positions = range(1, max(crabs) + 1)
    unique_crabs = sorted(list(set(crabs)))
    best_cost = sys.maxsize
    best_pos = 0
    for pos in possible_positions:
        fuel = 0
        for crab in unique_crabs:
            moves = range(1, abs(crab - pos) + 1)
            fuel += sum(moves) * num_crabs[crab]
            if fuel >= best_cost:
                break
        if fuel < best_cost:
            best_cost = fuel
            best_pos = pos

    return best_pos, best_cost

#print(brute_2(crabs))

import statistics

def fuel_for_pos(crabs, pos):
    return sum([abs(crab - pos) for crab in crabs])

print(fuel_for_pos(crabs, int(statistics.median(crabs))))

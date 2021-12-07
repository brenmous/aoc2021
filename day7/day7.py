from collections import defaultdict

with open("test_input.txt", "r") as f:
    crabs = [int(x) for x in f.read().split(',')]

def brute(crabs):
    num_crabs = defaultdict(int)
    for crab in crabs:
        num_crabs[crab] += 1
    fuel_costs = defaultdict(int)
    possible_positions = range(1, max(crabs) + 1)
    unique_crabs = sorted(list(set(crabs)))
    for pos in possible_positions:
        fuel = 0
        for crab in unique_crabs:
            fuel += abs(crab - pos) * num_crabs[crab]
        fuel_costs[pos] += fuel
    return fuel_costs

def brute_2(crabs):
    num_crabs = defaultdict(int)
    for crab in crabs:
        num_crabs[crab] += 1
    fuel_costs = defaultdict(int)
    possible_positions = range(1, max(crabs) + 1)
    unique_crabs = sorted(list(set(crabs)))
    for pos in possible_positions:
        fuel = 0
        for crab in unique_crabs:
            moves = range(1, abs(crab - pos) + 1)
            fuel += sum(moves) * num_crabs[crab]
        fuel_costs[pos] += fuel
    return fuel_costs

print(min(brute_2(crabs).values()))


def simulate(current_state):
    new_state = []
    for fish in current_state:
        if fish == 0:
            new_state.append(6)
            new_state.append(8)
        else:
            new_state.append(fish - 1)
    return new_state


with open("input.txt", "r") as f:
    state = [int(x) for x in f.read().split(',')]
cycles = 80


for day in range(cycles):
    # print(f"Day {day}: {state}")
    state = simulate(state)
print(len(state))


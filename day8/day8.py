with open("input.txt", "r") as f:
    signals = []
    outputs = []
    for line in f.readlines():
        signal, output = line.split("|")
        signals.append([s.strip() for s in signal.strip().split(" ")])
        outputs.append([o.strip() for o in output.strip().split(" ")])

def part1(outputs):
    count = 0
    for output in outputs:
        for digit in output:
            if len(digit) in (2, 4, 3, 7):
                count += 1
    return count

print(part1(outputs))

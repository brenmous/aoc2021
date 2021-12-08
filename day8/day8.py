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

def to_bin(s):
    mask = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    binary = ''.join(['1' if x in s else '0' for x in mask])
    return int(binary, 2)

# Uses the provided solved input
# example_signal_nums = [8, 5, 2, 3, 7, 9, 6, 4, 0, 1]
# decoded = {}
# for num, signal in zip(example_signal_nums, signals[0]):
#     decoded[num] = to_bin(signal)
#
# for i in [1, 4, 7]:
#     print("five segment")
#     for j in [2, 3, 5]:
#         print(f"{i} & {j} = {bin(decoded[i] & decoded[j]).count('1')}")
#     print("six segment")
#     for j in [0, 6, 9]:
#         print(f"{i} & {j} = {bin(decoded[i] & decoded[j]).count('1')}")

# 5 segments
# 1 & x == 2 set, x = 3
# 4 & y == 2 set, y = 2
# z = 5

# 6 segments
# 1 & x = 1 set, x = 6
# 4 & y = 4 set, y = 9
# z = 0

def decode_signal(signal):
    one = next(x for x in signal if len(x) == 2)
    four = next(x for x in signal if len(x) == 4)
    seven = next(x for x in signal if len(x) == 3)
    eight = next(x for x in signal if len(x) == 7)
    for fiver in [x for x in signal if len(x) == 5]:
        if bin(to_bin(one) & to_bin(fiver)).count('1') == 2:
            three = fiver
        elif bin(to_bin(four) & to_bin(fiver)).count('1') == 2:
            two = fiver
        else:
            five = fiver
    for sixer in [x for x in signal if len(x) == 6]:
        if bin(to_bin(one) & to_bin(sixer)).count('1') == 1:
            six = sixer
        elif bin(to_bin(four) & to_bin(sixer)).count('1') == 4:
            nine = sixer
        else:
            zero = sixer

    return {zero: '0', one: '1', two: '2', three: '3', four: '4',
            five: '5', six: '6', seven: '7', eight: '8', nine: '9'}

def parse_output(output, decoded):
    return int(''.join([decoded[o] for o in output]))

all_digits = []
for signal, output in zip(signals, outputs):
    signal = [''.join(sorted(x)) for x in signal]
    output = [''.join(sorted(x)) for x in output]
    decoded = decode_signal(signal)
    all_digits.append(parse_output(output, decoded))
print(sum(all_digits))

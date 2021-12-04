with open("input.txt", "r") as f:
    numbers = [f.strip() for f in f.readlines()]

num_bits = len(numbers[0])
gamma = ''
# there's a clever bitwise way to do this properly and I'm just a fucking gronk
for n in range(num_bits):
    bitsum = sum([int(num[n]) for num in numbers])
    if bitsum >= len(numbers) / 2:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)
epsilon = ~gamma
epsilon += 2**num_bits
print(gamma * epsilon)

def fun(numbers, invert=False):
    comp = '1' if invert else '0'
    nmb = numbers.copy()
    for n in range(num_bits):
        ones = sum([int(num[n]) for num in nmb])
        if ones >= len(nmb) / 2:
            nmb = [x for x in nmb if x[n] == comp]
        else:
            nmb = [x for x in nmb if not x[n] == comp]
        if len(nmb) == 1:
            return int(nmb[0], 2)
    raise Exception("ya dun goofed")

co2 = fun(numbers)
oxy = fun(numbers, invert=True)
print(co2 * oxy)

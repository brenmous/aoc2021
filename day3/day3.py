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

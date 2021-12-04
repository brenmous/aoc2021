with open("input.txt", "r") as f:
    xy = []
    z = []
    for cmd in f.readlines():
        if cmd.startswith("forward"):
            xy.append(int(cmd.replace("forward ", "")))
        elif cmd.startswith("down"):
            z.append(int(cmd.replace("down ", "")))
        elif cmd.startswith("up"):
            z.append(int(cmd.replace("up ", "-")))

print(sum(xy) * sum(z))

aim = 0
pos = 0
depth = 0
with open("input.txt", "r") as f:
    xy = []
    z = []
    for cmd in f.readlines():
        if cmd.startswith("forward"):
            f = int(cmd.replace("forward", ""))
            pos += f
            depth += f * aim
        elif cmd.startswith("down"):
            aim += int(cmd.replace("down ", ""))
        elif cmd.startswith("up"):
            aim += int(cmd.replace("up ", "-"))
print(pos * depth)

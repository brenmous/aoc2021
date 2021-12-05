from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

xs = []
ys = []
for line in lines:
    xy1, xy2 = line.split('->')
    x1, y1 = xy1.split(',')
    x2, y2 = xy2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 == x2 or y1 == y2:
        xs.append(list(range(min(x1, x2), max(x1, x2) + 1)))
        ys.append(list(range(min(y1, y2), max(y1, y2) + 1)))

points = defaultdict(int)
for i in range(len(xs)):
    for x in xs[i]:
        for y in ys[i]:
            points[(x, y)] += 1
print(sum([1 for p in points.values() if p > 1]))

with open("input.txt", "r") as f:
    lines = f.readlines()

xs = []
ys = []
for line in lines:
    xy1, xy2 = line.split('->')
    x1, y1 = xy1.split(',')
    x2, y2 = xy2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    x = list(range(min(x1, x2), max(x1, x2) + 1))
    y = list(range(min(y1, y2), max(y1, y2) + 1))
    if x1 == x2:
        x = [x[0] for _ in range(len(y))]
    elif y1 == y2:
        y = [y[0] for _ in range(len(x))]
    if x2 > x1:
        x.reverse()
    if y2 > y1:
        y.reverse()
    xs.append(x)
    ys.append(y)


points = defaultdict(int)
for i in range(len(xs)):
    for x, y in zip(xs[i], ys[i]):
        points[(x, y)] += 1
print(sum([1 for p in points.values() if p > 1]))

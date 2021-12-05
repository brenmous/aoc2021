from itertools import chain

with open("input.txt", "r") as f:
    lines = f.readlines()
    board_rows = []
    rows = []
    for i, line in enumerate(lines):
        if i == 0:
            draws = [int(x) for x in line.split(',')]
        elif line == '\n':
            if rows:
                board_rows.append(rows)
            rows = []
        else:
            rows.append([int(x.strip()) for x in line.split(' ') if x != ''])
    board_rows.append(rows)


board_cols = []
for rows in board_rows:
    cols = []
    for i in range(5):
        col = []
        for row in rows:
            col.append(row[i])
        cols.append(col)
    board_cols.append(cols)


def search_part1():
    for d in draws:
        for rows, cols in zip(board_rows, board_cols):
            for i in range(5):
                rows[i] = [x for x in rows[i] if x != d]
                cols[i] = [x for x in cols[i] if x != d]
                if not rows[i] or not cols[i]:
                    return d, rows, cols

def search_part2():
    winners = {}
    for d in draws:
        for board, (rows, cols) in enumerate(zip(board_rows, board_cols)):
            if winners.get(board, False):
                continue
            for i in range(5):
                rows[i] = [x for x in rows[i] if x != d]
                cols[i] = [x for x in cols[i] if x != d]
                if not rows[i] or not cols[i]:
                    winners[board] = True
            if len(list(winners.keys())) == len(board_rows):
                return d, rows, cols

#d, rows, cols = search_part1()
d, rows, cols = search_part2()
board_sum = sum(set(chain.from_iterable(rows)))
print(f"{board_sum} * {d} = {board_sum * d}")

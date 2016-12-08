translate = {
    'U': [-1, 0],
    'L': [0, -1],
    'R': [0, 1],
    'D': [1, 0],
}

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
B = '0'
grid = [
    [B,     B, '1',   B,   B],
    [B,   '2', '3', '4',   B],
    ['5', '6', '7', '8', '9'],
    [B,   'A', 'B', 'C',   B],
    [B,     B, 'D',   B,   B]
]


def main():
    instructions = [line.strip('\n') for line in open('input.txt')]

    code = ''
    position = [1, 1]
    for i in instructions:
        for j in i:
            new_position = [
                sum(a) if (sum(a) < 5 and sum(a) >= 0) else a[0] for a in zip(
                    position, translate[j]
                )
            ]
            if grid[new_position[0]][new_position[1]] != B:
                position = new_position
        code += str(grid[position[0]][position[1]])

    print code

if __name__ == '__main__':
    main()

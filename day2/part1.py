translate = {
    'U': [-1, 0],
    'L': [0, -1],
    'R': [0, 1],
    'D': [1, 0],
}

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def main():
    instructions = [line.strip('\n') for line in open('input.txt')]

    code = ''
    position = [1, 1]
    for i in instructions:
        for j in i:
            position = [
                sum(a) if (sum(a) < 3 and sum(a) >= 0) else a[0] for a in zip(
                    position, translate[j]
                )
            ]
        code += str(grid[position[0]][position[1]])

    print code

if __name__ == '__main__':
    main()

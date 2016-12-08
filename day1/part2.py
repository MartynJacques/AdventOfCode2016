translations = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

turn = {
    'R': 1,
    'L': -1
}


def main():
    instructions = [
        line.strip('\n') for line in open('input.txt')
    ][0].split(", ")  # meh

    direction_index = 0
    position = [0, 0]
    visited_positions = []

    for i in instructions:
        direction_index = (direction_index + turn[i[0]]) % 4
        for _ in range(int(i[1:])):
            visited_positions.append(list(position))
            position = [
                sum(a) for a in zip(position, translations[direction_index])
            ]
            if position in visited_positions:
                print sum([abs(p) for p in position])
                exit()


if __name__ == '__main__':
    main()

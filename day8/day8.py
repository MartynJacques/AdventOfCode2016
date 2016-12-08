import argparse
import numpy as np
from collections import deque
import os
import time


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('part')
    return parser


def rotate(n, rot_num):
    d = deque(n)
    d.rotate(rot_num)
    return list(d)


def print_grid(grid):
    os.system('clear')
    for g in grid:
        print ''.join(g)


def add_hashes(grid, x_len, y_len):
    for x in range(x_len):
        for y in range(y_len):
            grid[y][x] = '#'


def rotate_column(grid, col_num, rot_num):
    column = rotate([x[col_num] for x in grid], rot_num)
    x = 0
    for g in grid:
        g[col_num] = column[x]
        x += 1


def rotate_row(grid, row_num, rot_num):
    grid[row_num] = rotate(grid[row_num], rot_num)


def parse_rect(rect):
    xy = rect[1].split('x')
    return int(xy[0]), int(xy[1])


def parse_rotation(rotation):
    is_col = rotation[1] == 'column'
    axis = rotation[2][0]
    index = int(rotation[2][2:])
    rot_val = int(rotation[4])
    return is_col, index, rot_val


def display(instructions, animate):
    grid = [[' ']*50 for _ in range(6)]
    for i in instructions:
        if i[0] == 'rect':
            x_len, y_len = parse_rect(i)
            add_hashes(grid, x_len, y_len)
        else:
            is_col, axis, rot_val = parse_rotation(i)
            if is_col:
                rotate_column(grid, axis, rot_val)
            else:
                rotate_row(grid, axis, rot_val)
        if animate:
            time.sleep(0.02)  # sleep for animation
            print_grid(grid)  # for animation
    return grid


def main(args):
    instructions = [line.strip('\n').split() for line in open("input.txt")]

    if args.part == 'part1':
        grid = display(instructions, False)
        print sum(g.count('#') for g in grid)
    else:
        grid = display(instructions, True)

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert (
        args.part == 'part1' or args.part == 'part2'
    ), 'Please sepcify part1 or part2.'
    main(args)

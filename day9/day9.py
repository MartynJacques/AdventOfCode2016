import re
import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('part')
    return parser


def main(args):
    compressed_strings = [line.strip('\n') for line in open("input.txt")]

    results = []
    for c in compressed_strings:
        i = 0
        result = ''
        while i != len(c):
            if c[i] == '(':
                compression_data = c[i+1:].split(')', 1)
                rest_of_string = compression_data[1]
                compression_string = compression_data[0].split('x')
                repeats = compression_string[1]
                string_to_repeat = rest_of_string[:int(compression_string[0])]
                for j in range(int(repeats)):
                    result += string_to_repeat
                i += len(compression_data[0]) + len(string_to_repeat) + 2
            else:
                result += c[i]
                i += 1

        print len(result)

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert (
        args.part == 'part1' or args.part == 'part2'
    ), 'Please sepcify part1 or part2.'
    main(args)

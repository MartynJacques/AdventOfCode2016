import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('part')
    return parser

def main(args):
    if args.part == 'part1':
        pass
    else:
        pass


if __name__ == '__main__':
    args = build_parser().parse_args()
    assert (
        args.part == 'part1' or args.part == 'part2'
    ), 'Please sepcify part1 or part2.'
    main(args)

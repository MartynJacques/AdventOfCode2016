import operator


def main():
    lines = [line.strip('\n') for line in open('input.txt')]
    error_corrected_msg = []
    for x in range(0, len(lines[0])):
        column = [row[x] for row in lines]

        count = []
        for n in set(column):
            count.append((n, column.count(n)))

        sort = sorted(count, key=operator.itemgetter(1))
        error_corrected_msg.append(sort[-1][0])

    print ''.join(error_corrected_msg)

if __name__ == '__main__':
    main()

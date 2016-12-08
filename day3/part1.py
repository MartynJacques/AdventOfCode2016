def main():
    triangles = [line.strip('\n').split() for line in open('input.txt')]

    num = 0
    for t in triangles:
        t = map(int, t)
        if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
            num += 1

    print num

if __name__ == '__main__':
    main()

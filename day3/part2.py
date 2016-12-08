import numpy as np


def main():
    triangles = [line.strip('\n').split() for line in open('input.txt')]
    oned_np_array = np.array(triangles).reshape(-1)
    reshaped_array = np.array(oned_np_array).reshape(len(oned_np_array)/3, 3)
    proper_triangles = np.transpose(
        reshaped_array
    ).reshape(len(oned_np_array)/3, 3)

    num = 0
    for t in proper_triangles:
        t = map(int, t)
        if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
            num += 1

    print num

if __name__ == '__main__':
    main()

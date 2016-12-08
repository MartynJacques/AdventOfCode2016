import hashlib


def main():
    door_id = 'abc'
    xList = []
    passwordList = []
    hashValue = None
    for x in range(0, 100000000):
        hashValue = hashlib.md5(door_id + str(x)).hexdigest()
        if hashValue[:5] == '00000':
            xList.append(x)
            passwordList.append(hashValue[5])
            if len(passwordList) == 8:
                print ''.join(passwordList)
                exit()


if __name__ == '__main__':
    main()

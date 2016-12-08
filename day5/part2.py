import hashlib


def main():
    door_id = 'ugkcyxxp'
    passwordList = ['_', '_', '_', '_', '_', '_', '_', '_']
    hashValue = None
    for x in range(0, 100000000):
        hashValue = hashlib.md5(door_id + str(x)).hexdigest()
        if hashValue[:5] == '00000':
            index = int(hashValue[5], 16)
            value = hashValue[6]
            if index < 8:
                if passwordList[index] == '_':
                    passwordList[index] = value
                print ''.join(passwordList)
                if passwordList.count('_') == 0:
                    exit()

if __name__ == '__main__':
    main()

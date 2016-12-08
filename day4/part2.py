import re
import operator


def parse_room(roomname):
    roomname = roomname.split('-')
    end = re.search(r"(.*)\[(.*)\]", roomname[-1])
    checksum = end.group(2)
    number = end.group(1)
    encrypted_name = roomname[:-1]
    return encrypted_name, number, checksum


def get_checksum(encrypted_name):
    encrypted_name = ''.join(encrypted_name)
    count = []
    for n in list(set(encrypted_name)):
        count.append((n, encrypted_name.count(n)))
    alpha_sort = sorted(count, key=operator.itemgetter(0))
    number_sort = sorted(alpha_sort, key=operator.itemgetter(1), reverse=True)
    return ''.join([x[0] for x in number_sort[:5]])


def decipher(c, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    current_index = alphabet.index(c)
    new_index = (current_index + n) % 26
    new_char = alphabet[new_index]
    return new_char


def main():
    lines = [line.strip() for line in open('input.txt')]

    for l in lines:
        encrypted_name, number, checksum = parse_room(l)
        if get_checksum(encrypted_name) == checksum:
            decrypted_name = []
            for c in encrypted_name:
                decrypted_word = ''
                for d in c:
                    decrypted_word += decipher(d, int(number))
                decrypted_name.append(decrypted_word)
            if 'northpole' in decrypted_name:
                print number
                exit()

if __name__ == '__main__':
    main()

import re


def is_abba(n):
    for i in range(len(n)-3):
        first_half = [n[i], n[i+1]]
        second_half = [n[i+2], n[i+3]]
        if (first_half == list(reversed(second_half)) and
                first_half[0] != first_half[1]):
            return True
    return False


def supports_tls(ip_addr):
    hypernet_seqs = re.findall(r"\[(.*?)\]", ip_addr)
    non_hypernet_seqs = [
        x for x in re.findall(r"[\w']+", ip_addr) if x not in hypernet_seqs
    ]

    if (not sum(is_abba(h) for h in hypernet_seqs) and
            sum(is_abba(nh) for nh in non_hypernet_seqs)):
        return True
    return False  # meh


def main():
    ip_addresses = [l.strip('\n') for l in open("input.txt")]
    print sum(supports_tls(ip) for ip in ip_addresses)

if __name__ == '__main__':
    main()

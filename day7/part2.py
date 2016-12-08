import re


def contains_abba(n):  # should loop elsewhere
    for i in range(len(n)-3):
        first_half = [n[i], n[i+1]]
        second_half = [n[i+2], n[i+3]]
        if (first_half == list(reversed(second_half)) and
                first_half[0] != first_half[1]):
            return True
    return False


def find_abas(n):
    abas = []
    for i in range(len(n) - 2):
        if n[i] == n[i+2]:
            aba = ''.join([n[i], n[i+1], n[i+2]])
            abas.append(aba)
    return abas


def aba_to_bab(aba):
    return ''.join([aba[1], aba[0], aba[1]])


def parse_ipv7(ip_addr):
    hypernet_seqs = re.findall(r"\[(.*?)\]", ip_addr)
    supernet_seqs = [
        x for x in re.findall(r"[\w']+", ip_addr) if x not in hypernet_seqs
    ]
    return hypernet_seqs, supernet_seqs


def supports_tls(ip_addr):
    hypernet_seqs, supernet_seqs = parse_ipv7(ip_addr)

    if (not sum(contains_abba(h) for h in hypernet_seqs) and
            sum(contains_abba(s) for s in supernet_seqs)):
        return True
    return False  # meh


def support_ssl(ip_addr):
    hypernet_seqs, supernet_seqs = parse_ipv7(ip_addr)

    for s in supernet_seqs:
        for aba in find_abas(s):
            for h in hypernet_seqs:
                if aba_to_bab(aba) in h:
                    return True

    return False


def main():
    ip_addresses = [l.strip('\n') for l in open("input.txt")]
    print sum(support_ssl(ip) for ip in ip_addresses)

if __name__ == '__main__':
    main()

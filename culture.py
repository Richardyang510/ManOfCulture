english_vocab = set(open('google-10000-english.txt').read().split())
found = set()

ignore_duplicate = True


def kth_bit_set(b, k):
    if (b >> (k-1)) & 1:
        return True
    else:
        return False


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def spaces_not_masked(s, spaces, i):
    for idx in spaces:
        loc = len(s) - idx
        if kth_bit_set(i, loc):
            return False
    return True


def get_masked_word(s, b):
    mask = [int(d) for d in str(b)]
    out = ""
    if not len(mask) == len(s):
        print("length mismatch")
        exit(0)

    for i in range(len(mask)):
        if mask[i] == 1:
            out += s[i]
        else:
            out += "*"

    return out


def str_is_sentence(s):
    s_filter = s.replace("*", "")
    if ignore_duplicate:
        if s_filter in found:
            return False
        found.add(s_filter)

    return s_filter in english_vocab


def main():
    s = input()
    print(len(s))
    n_mask = 2**(len(s))
    print(n_mask)
    spaces = find(s, ' ')
    print(spaces)
    bin_prefix = "{0:0" + str(len(s)) + "b}"

    for i in range(n_mask):
        i_bin = bin_prefix.format(i)

        if not spaces_not_masked(s, spaces, i):
            continue

        s_masked = get_masked_word(s, i_bin)

        if str_is_sentence(s_masked):
            print(s_masked + " " + s_masked.replace("*", ""))


if __name__ == "__main__":
    main()


import copy


def binaryRepresent(val, formatdigits):
    if val < 0:
        raise ValueError
    elif val == 0:
        return formatdigits * [0]

    # to format binary
    need_digits = 0
    for i in range(129):
        if (val < 2 ** i and val >= 2 ** (i -1)):
            need_digits = i

    binary_ret = need_digits * [0]

    index =  need_digits - 1
    rest = val
    while True:
        if index < 0:
            break

        if (rest - 2 ** index >= 0):
            rest = rest - 2 ** index
            binary_ret[index] = 1
            if rest == 0:
                break

        index -= 1

    fmt_ret = formatdigits * [0]
    copy_num = len(binary_ret);
    if (formatdigits > copy_num):
        formatdigits = copy_num

    for i in range(formatdigits):
        fmt_ret[i] = binary_ret[i]

    return fmt_ret


count_num3 = 0
for i in range(64):

    x = binaryRepresent(i, 6)
    val = x.count(1)
    if (val == 3):
        count_num3 += 1
    print(x)

print("count_num3=", count_num3)
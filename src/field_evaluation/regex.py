import re

def split_ignoring_escaped(string):
    splits = []

    for i in range(0, len(string)):
        if string[i] == '/':
            split = True
            j = 1
            while i - j >= 0 and string[i-j] == "\\":
                split = not split
                j += 1

            if split:
                splits.append(i)

    retval = []
    for split in reversed(splits):
        retval.append(string[split:][1:])
        string = string[:split]

    retval.append(string)

    retval.reverse()
    return retval


def regex(string):
    string = split_ignoring_escaped(string)

    if len(string) > 3:
        if (string[3] == "g"):
            return re.sub(string[1], string[2], string[0][:-1])

    return re.sub(string[1], string[2], string[0][:-1], 1)


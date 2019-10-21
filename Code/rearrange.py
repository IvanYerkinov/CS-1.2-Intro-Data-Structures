import sys
import random


def swapArgs(args):
    if len(args) <= 2:
        print('Please enter a list of words to swap.\n')
        return
    relist = args[1:]
    for i in range(0, len(relist)):
        index = random.randint(0, len(relist) - 1)
        relist[i], relist[index] = relist[index], relist[i]

    return relist


if __name__ == '__main__':
    print(swapArgs(sys.argv))

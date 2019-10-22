import random
import sys


def get_words():
    with open('/usr/share/dict/words', 'r') as f:
        wordlist = []
        for line in f:
            line = line.rstrip()
            wordlist.append(line)
        return wordlist


def grab_random(num):
    wordlist = get_words()
    leng = len(wordlist)
    grabbedwords = []
    for i in range(0, num):
        grabbedwords.append(wordlist[random.randint(0, leng)])
    return grabbedwords


if __name__ == '__main__':
    num = int(sys.argv[1])

    if isinstance(num, int):
        grab_words = grab_random(num)
        print(" ".join(grab_words))

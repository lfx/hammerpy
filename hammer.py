#!/usr/bin/env python3
import random
import sys

lines = open(sys.argv[1]).readlines()
random.shuffle(lines)

if __name__ == "__main__":
    total = 0
    good = 0
    bad = 0
    for line in lines:
        total+=1
        en = line.split(";")[0]
        lt = line.split(";")[1]
        print("{0} {1}".format(total, lt))
        r = input("en: ")
        if(en == r):
            good+=1
            print("Correct!")
        else:
            bad+=1
            print("Wrong! Should be - ", en)
            lines.append(line)
            while True:
                rr = input("again: ")
                if(en == rr):
                    break
    percent = good/total * 100
    print("Stat: total: {0}, good: {1}, bad: {2}. - {3:.0f}% to be correct!".format(total, good, bad, percent))

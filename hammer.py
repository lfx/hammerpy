#!/usr/bin/env python3
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_filename')
parser.add_argument('--out', '-o', help='records mistaken words to other file')
args = parser.parse_args()

lines = open(args.input_filename).readlines()
random.shuffle(lines)

record_mistakes = False
if args.out:
    record_mistakes = True
    mistakes_list = []

def record(word):
    if record_mistakes:
        with open(args.out, "a") as tmp:
            tmp.write(word)

def footer():
    percent = good/total * 100
    print("\nStat: total: {0}, good: {1}, bad: {2}. - {3:.0f}% to be correct!".format(total, good, bad, percent))


if __name__ == "__main__":
    total = 0
    good = 0
    bad = 0
    try:
        for line in lines:
            total+=1
            en = line.split(";")[0]
            lt = line.split(";")[1]
            print("{0} {1}".format(total, lt))
            candidate = input("en: ")
            if(en == candidate):
                good+=1
                print("Correct!")
            else:
                bad+=1
                record(line)
                print("Wrong! Should be - ", en)
                lines.append(line)
                while True:
                    repeat_candidate = input("again: ")
                    if(en == repeat_candidate):
                        break

    except KeyboardInterrupt:
        pass
    finally:
        footer()

    # percent = good/total * 100
    # print("Stat: total: {0}, good: {1}, bad: {2}. - {3:.0f}% to be correct!".format(total, good, bad, percent))

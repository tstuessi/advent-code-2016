# Part 1 of day 6
#
# Frequency counter
# Tyler Stuessi

from collections import defaultdict
from operator import itemgetter

def frequency_counter():
    input_list = []
    message = ""
    with open("input.txt", "r") as f:
        input_list = f.read().split("\n")
        del input_list[-1]
    
    dicts = []
    for i in range(len(input_list[0])):
        dicts.append(defaultdict(int))
    for x in input_list:
        for i in range(len(x)):
            dicts[i][x[i]] += 1

    for d in dicts:
        message += max(d.items(), key=itemgetter(1))[0]

    return message




if __name__ == "__main__":
    print(frequency_counter())

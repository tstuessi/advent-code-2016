# Day 1 of Advent of code 
# 
# Tyler Stuessi

# main function
def find_dist():
    # read the input
    raw = input()
    steps = raw.split(", ")

    i = 0
    # dirs: N  E  S  W
    dirs = [0, 0, 0, 0]

    for step in steps:
        if step[0] == "R":
            dirs[(i+1) % 4] += int(step[1:])
            i = (i+1) % 4
        else:
            dirs[(i-1) % 4] += int(step[1:])
            i = (i-1) % 4

    return abs(dirs[0]-dirs[2]) +  abs(dirs[1]-dirs[3])



if __name__ == "__main__":
    print(find_dist())



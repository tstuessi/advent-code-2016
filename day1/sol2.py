# Part 2 of day 1 in advent of code
# I essentially solve this by walking along a graph
# might be overkill, but it works
# 
# Tyler Stuessi

from collections import defaultdict

def get_coords(dirs):
    return (dirs[1]-dirs[3], dirs[0]-dirs[2])

def manh_dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1]-y[1])

def find_first_twice():
    raw = input()
    steps = raw.split(', ')

    i = 0
    # dirs  N  E  S  W
    dirs = [0, 0, 0, 0]

    visited = defaultdict(bool)
    for step in steps:
        for j in range(int(step[1:])):
            if step[0] == "R":
                dirs[(i+1)%4] += 1
            if step[0] == "L":
                dirs[(i-1)%4] += 1
            coords = get_coords(dirs)
            if visited[coords]:
                return manh_dist(coords, (0,0))
            else:
                visited[coords] = True
        i = (i+1)%4 if step[0] == "R" else (i-1)%4

    return -1

if __name__ == "__main__":
    print(find_first_twice())





# Part 1 of day 3 of advent of code
#
# Determining valid triangles
# Tyler Stuessi

def is_valid_triangle(tri):
    tot = sum(tri)
    for val in tri:
        if 2*val >= tot:
            return False
    return True

def count_valid_triangles():
    # get input
    pairs = []
    with open("input.txt", "r") as f:
        for line in f.read().split('\n'):
            pairs.append([int(x) for x in line.split()])
    # don't know why this does this
    del pairs[-1]

    count = 0
    for tri in pairs:
        if is_valid_triangle(tri):
            count += 1

    return count

if __name__ == "__main__":
    print(count_valid_triangles())


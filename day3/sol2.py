# Part 2 of day 3 of advent of code
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
        lines = f.read().split('\n')
        for i in range(0, len(lines)-1, 3):
            for j in range(3):
                pairs.append([int(lines[i+k].split()[j]) for k in range(3)])
    print(pairs[0])





    count = 0
    for tri in pairs:
        if is_valid_triangle(tri):
            count += 1

    return count

if __name__ == "__main__":
    print(count_valid_triangles())


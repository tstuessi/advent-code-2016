# Part 2 on day 2 on advent of code
#
# Tyler Stuessi

def get_bathroom_code():
    # get input

    code = ""

    keypaths = []
    try:
        while True:
            raw = input()
            keypaths.append(raw)
    except EOFError:
        pass

    # hard code the grid
    grid = [["0", "0", "1", "0", "0"],
            ["0", "2", "3", "4", "0"],
            ["5", "6", "7", "8", "9"],
            ["0", "A", "B", "C", "0"],
            ["0", "0", "D", "0", "0"]]

    row = 2
    col = 2
    for path in keypaths:
        for c in path:
            if c == "L" and col !=  0 and grid[row][col-1] != "0":
                col -= 1
            elif c == "U" and row != 0 and grid[row-1][col] != "0":
                row -= 1
            elif c == "D" and row != len(grid)-1 and grid[row+1][col] != "0":
                row += 1
            elif c == "R" and col != len(grid[row])-1 and grid[row][col+1] != "0":
                col += 1
        code += grid[row][col]

    return code


if __name__ == "__main__":
    print(get_bathroom_code())
